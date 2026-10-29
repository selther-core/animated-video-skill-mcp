#!/usr/bin/env python3
"""Small local MCP server for the cinematic narrative video skill.

Transport: newline-delimited JSON-RPC 2.0 on stdio. Python standard library only.
No network, no arbitrary shell commands, and no implicit video/voice generation.
"""
from __future__ import annotations
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = ROOT / ".agents" / "skills" / "cinematic-narrative-video"
VERSION = "2025-06-18"
DOCS = {
    "skill": ("SKILL.md", "Complete skill and production workflow"),
    "niche": ("references/niche-adaptation.md", "Adapting the style to any niche"),
    "compatibility": ("references/agent-compatibility.md", "Using the skill with different kinds of agents"),
    "visual": ("references/visual-reference.md", "Analysis of extracted reference frames"),
    "animation": ("references/code-animation.md", "Reference comparison and code-drawn animation workflow"),
    "rig": ("references/character-rig.md", "Long-body character construction, layering and rig QA"),
    "staging": ("references/cinematic-staging.md", "Backgrounds, lighting, animation and cinematic cutaways"),
    "structure": ("references/story-structure.md", "Reference-informed story beats, visual progression and evidence-tagged review"),
    "audit": ("references/case-study-reference-vs-ww2.md", "Reference excerpt and WWII cut visual comparison"),
    "voice": ("references/voice-direction.md", "American-accent voice direction by niche, sample scripts, and TTS workflow"),
    "examples": ("examples/cross-niche-scripts.md", "Cross-niche script and storyboard examples"),
}

def schema(properties, required=()):
    return {"type": "object", "properties": properties, "required": list(required), "additionalProperties": False}

def field(description):
    return {"type": "string", "description": description, "minLength": 1}

TOOLS = [
    {"name": "read_skill_guide", "description": "Read an included skill guide. These are general instructions, not evidence of the reference's unreviewed audio or ending.",
     "inputSchema": schema({"guide": {"type": "string", "enum": list(DOCS), "description": "Select skill, niche, compatibility, visual, animation, rig, staging, structure, audit, voice, or examples."}}, ["guide"])},
    {"name": "create_video_project", "description": "Create a NEW local project folder with a user brief and clearly marked draft production templates. Does not create a video, voice, art, or thumbnail. Refuses to overwrite an existing folder.",
     "inputSchema": schema({"directory": field("Path to a new directory to create; use an absolute path for predictable results."), "topic": field("Video subject."), "niche": field("Content niche."), "audience": field("Intended audience."), "length": field("Requested length or range, for example 4-6 minutes."), "format": field("Format, for example 16:9 YouTube or 9:16 Short."), "requirements": {"type": "string", "description": "Other requirements; can be empty."}}, ["directory", "topic", "niche", "audience", "length", "format"])},
    {"name": "validate_timeline", "description": "Validate basic timing consistency of a proposed timeline JSON object; does not assess factual accuracy, creative quality, audio sync, or a finished video.",
     "inputSchema": schema({"timeline": {"type": "object", "description": "Object with numeric duration_seconds or duration and array shots containing numeric start/end. May include voice_cues and audio_events arrays."}}, ["timeline"])},
    {"name": "check_story_plan", "description": "Check fields and event timing in a manually supplied story-beat plan. Does not view media, judge creative quality or prove a video matches the plan.",
     "inputSchema": schema({"plan": {"type": "object", "description": "Object with duration_seconds and beats: id, start, end, purpose, before, action, after, hold, source_or_fiction, and events with time, change, meaning. An intentional_hold=true may replace events."}}, ["plan"])},
    {"name": "make_srt", "description": "Generate SRT subtitle text from explicitly supplied timed captions. The agent must align and review timing against real audio; this tool does not transcribe or hear audio.",
     "inputSchema": schema({"cues": {"type": "array", "minItems": 1, "items": {"type": "object", "properties": {"start": {"type": "number", "minimum": 0}, "end": {"type": "number", "minimum": 0}, "text": field("Caption text")}, "required": ["start", "end", "text"], "additionalProperties": False}}}, ["cues"])},
    {"name": "inspect_video", "description": "Use a locally available ffprobe to report technical metadata for an existing local video. Does not listen to, watch, judge copyright, or verify compliance.",
     "inputSchema": schema({"path": field("Path to an existing local video file.")}, ["path"])},
]
RESOURCES = [{"uri": f"cinematic://guide/{key}", "name": title, "mimeType": "text/markdown", "description": f"Included file {path}"} for key, (path, title) in DOCS.items()]
PROMPTS = [{"name": "create_niche_video", "description": "Ask the agent to create an original reference-inspired video in any niche using the skill and available tools.", "arguments": [
    {"name": "topic", "description": "Video topic", "required": True},
    {"name": "niche", "description": "Content niche", "required": True},
    {"name": "audience", "description": "Target audience", "required": False},
    {"name": "requirements", "description": "Format, length and other requirements", "required": False},
]}]

class ToolError(Exception):
    pass

def require_string(args, key):
    value = args.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ToolError(f"{key} must be a nonempty string")
    return value.strip()

def tool_read(args):
    key = require_string(args, "guide")
    if key not in DOCS:
        raise ToolError(f"guide must be one of: {', '.join(DOCS)}")
    path, title = DOCS[key]
    return {"guide": key, "title": title, "path": str(SKILL_ROOT / path), "content": (SKILL_ROOT / path).read_text(encoding="utf-8")}

def tool_create(args):
    directory = Path(require_string(args, "directory")).expanduser().absolute()
    topic, niche, audience, length, fmt = [require_string(args, k) for k in ("topic", "niche", "audience", "length", "format")]
    extra = args.get("requirements", "")
    if not isinstance(extra, str):
        raise ToolError("requirements must be a string")
    try:
        directory.mkdir(parents=False, exist_ok=False)
    except FileExistsError:
        raise ToolError("Directory already exists; no files were changed. Choose a new directory.")
    except OSError as e:
        raise ToolError(f"Cannot create project directory (parent must already exist): {e}")
    brief = {"topic": topic, "niche": niche, "audience": audience, "length": length, "format": fmt, "requirements": extra,
             "status": "draft", "note": "No media, TTS, fact-check, playback review or platform compliance check has been completed."}
    (directory / "brief.json").write_text(json.dumps(brief, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (directory / "narration_script.md").write_text("# Narration and dialogue — DRAFT\n\nWrite original, topic-appropriate speech here. This is not generated audio.\n", encoding="utf-8")
    (directory / "storyboard.md").write_text("# Storyboard — DRAFT\n\nBuild original SVG/CSS/Canvas scenes and articulated character action. Do not use AI image generation. Create and inspect a short voiced style test first.\n\n| Cue | Story purpose | Visual / character / prop | Audio | Source if factual |\n|---|---|---|---|---|\n| 1 | TODO | TODO | TODO | TODO |\n", encoding="utf-8")
    (directory / "story-beats.json").write_text(json.dumps({"status": "draft", "duration_seconds": None, "beats": []}, indent=2) + "\n", encoding="utf-8")
    (directory / "timeline.json").write_text(json.dumps({"status": "draft", "duration_seconds": None, "shots": [], "voice_cues": [], "audio_events": []}, indent=2) + "\n", encoding="utf-8")
    (directory / "quality_report.md").write_text("# Quality report — NOT REVIEWED\n\n- [ ] Script and factual claims reviewed\n- [ ] 15–30 second voiced, code-drawn style test reviewed and corrected\n- [ ] Character/prop action and diagram reveals inspected within shots\n- [ ] No AI-generated images used\n- [ ] Video rendered and decoded\n- [ ] Full visual review completed\n- [ ] Audio listened to and synchronized\n- [ ] Caption timing checked\n- [ ] Rights and current platform requirements checked\n- [ ] Thumbnail, title, description and playlist recommendation checked\n\nDo not mark these as complete without evidence.\n", encoding="utf-8")
    (directory / "caption_and_publish.md").write_text("# Publishing package — DRAFT\n\nTitle: TODO\n\nDescription: TODO\n\nSources: TODO if factual\n\nPlaylist: recommend only when relevant; if channel is unknown, make conditional.\n\nPublishing instructions: TODO after current platform checks.\n", encoding="utf-8")
    for name in ("assets", "audio", "renders"):
        (directory / name).mkdir()
    return {"directory": str(directory), "status": "draft_scaffold_created", "files": ["brief.json", "narration_script.md", "storyboard.md", "story-beats.json", "timeline.json", "quality_report.md", "caption_and_publish.md"], "directories": ["assets", "audio", "renders"], "next": "Research and write; draw and animate original SVG/CSS/Canvas assets without image generation; create and inspect a short voiced style test; then render and review the full video. No finished media exists yet."}

def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)

def validate_timeline(args):
    t = args.get("timeline")
    if not isinstance(t, dict):
        raise ToolError("timeline must be an object")
    duration = t.get("duration_seconds", t.get("duration"))
    shots = t.get("shots")
    issues, warnings = [], []
    if not num(duration) or duration <= 0:
        issues.append("duration_seconds or duration must be a positive finite number")
        duration = None
    if not isinstance(shots, list) or not shots:
        issues.append("shots must be a nonempty array")
        shots = []
    valid_shots = []
    for i, shot in enumerate(shots):
        if not isinstance(shot, dict) or not num(shot.get("start")) or not num(shot.get("end")):
            issues.append(f"shot {i} needs numeric start and end"); continue
        start, end = shot["start"], shot["end"]
        if start < 0 or end <= start:
            issues.append(f"shot {i} has invalid time range")
        if duration is not None and end > duration + .001:
            issues.append(f"shot {i} exceeds duration")
        valid_shots.append((start, end, i))
    valid_shots.sort()
    expected = 0.0
    for start, end, i in valid_shots:
        if start > expected + .001:
            issues.append(f"gap before shot {i}: {expected:.3f} to {start:.3f}")
        elif start < expected - .001:
            issues.append(f"overlap before shot {i}: {start:.3f} vs {expected:.3f}")
        expected = max(expected, end)
    if duration is not None and valid_shots and expected < duration - .001:
        issues.append(f"shots end at {expected:.3f}, before duration {duration:.3f}")
    for kind in ("voice_cues", "audio_events", "captions"):
        cues = t.get(kind, [])
        if not isinstance(cues, list):
            issues.append(f"{kind} must be an array"); continue
        for i, cue in enumerate(cues):
            if not isinstance(cue, dict):
                issues.append(f"{kind}[{i}] must be an object"); continue
            start = cue.get("start", cue.get("nominal_start"))
            end = cue.get("end", cue.get("nominal_end"))
            if start is not None and (not num(start) or start < 0 or (duration is not None and start > duration)):
                issues.append(f"{kind}[{i}] has invalid start")
            if end is not None and (not num(end) or (num(start) and end < start) or (duration is not None and end > duration + .001)):
                issues.append(f"{kind}[{i}] has invalid end")
            if kind == "audio_events" and cue.get("asset") is None:
                warnings.append(f"{kind}[{i}] has no audio asset")
    warnings.append("Does not validate creative quality, media files, accuracy, actual audio sync, copyright, accessibility or policy compliance.")
    return {"timing_valid": not issues, "issues": issues, "warnings": warnings, "shot_count": len(shots)}

def check_story_plan(args):
    plan = args.get("plan")
    if not isinstance(plan, dict):
        raise ToolError("plan must be an object")
    duration, beats = plan.get("duration_seconds"), plan.get("beats")
    issues, warnings = [], []
    if not num(duration) or duration <= 0:
        issues.append("duration_seconds must be a positive finite number")
        duration = None
    if not isinstance(beats, list) or not beats:
        issues.append("beats must be a nonempty array")
        beats = []
    for i, beat in enumerate(beats):
        tag = f"beats[{i}]"
        if not isinstance(beat, dict):
            issues.append(f"{tag} must be an object")
            continue
        start, end = beat.get("start"), beat.get("end")
        valid_range = num(start) and num(end) and start >= 0 and end > start and (duration is None or end <= duration)
        if not valid_range:
            issues.append(f"{tag} needs a valid start/end inside duration")
        for key in ("id", "purpose", "before", "action", "after", "hold", "source_or_fiction"):
            if not isinstance(beat.get(key), str) or not beat[key].strip():
                issues.append(f"{tag}.{key} must be a nonempty string")
        events = beat.get("events")
        if not isinstance(events, list):
            issues.append(f"{tag}.events must be an array")
            continue
        if not events and beat.get("intentional_hold") is not True:
            warnings.append(f"{tag} has no planned visual events; add events or mark an intentional hold")
        for j, event in enumerate(events):
            label = f"{tag}.events[{j}]"
            if not isinstance(event, dict):
                issues.append(f"{label} must be an object")
                continue
            when = event.get("time")
            if not num(when) or (valid_range and not (start <= when < end)):
                issues.append(f"{label}.time must be finite and within the beat [start, end)")
            for key in ("change", "meaning"):
                if not isinstance(event.get(key), str) or not event[key].strip():
                    issues.append(f"{label}.{key} must be a nonempty string")
    warnings.append("Checks supplied planning fields only; does not inspect media, verify facts, speech sync, quality, sources or whether the plan was followed.")
    return {"fields_valid": not issues, "issues": issues, "warnings": warnings, "beat_count": len(beats)}

def make_srt(args):
    cues = args.get("cues")
    if not isinstance(cues, list) or not cues:
        raise ToolError("cues must be a nonempty array")
    def stamp(seconds):
        ms = round(seconds * 1000)
        hours, ms = divmod(ms, 3600000)
        minutes, ms = divmod(ms, 60000)
        secs, ms = divmod(ms, 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"
    out, previous_end = [], 0.0
    for i, cue in enumerate(cues, 1):
        if not isinstance(cue, dict): raise ToolError(f"cue {i} must be an object")
        start, end = cue.get("start"), cue.get("end")
        text = require_string(cue, "text")
        if not num(start) or not num(end) or start < 0 or end <= start:
            raise ToolError(f"cue {i} needs nonnegative start and end greater than start")
        if start < previous_end:
            raise ToolError(f"cue {i} overlaps the previous cue or is out of order")
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        if "\n\n" in text: raise ToolError(f"cue {i} text must not contain a blank line")
        out.append(f"{i}\n{stamp(start)} --> {stamp(end)}\n{text}\n")
        previous_end = end
    return {"srt": "\n".join(out), "cue_count": len(cues), "limitations": "Times are supplied by the caller, not measured from audio. Review and correct alignment."}

def inspect_video(args):
    p = Path(require_string(args, "path")).expanduser().resolve()
    if not p.is_file():
        raise ToolError("Video path is not an existing file")
    binary = shutil.which("ffprobe")
    if not binary:
        raise ToolError("ffprobe was not found on PATH. No metadata inspection was performed.")
    try:
        r = subprocess.run([binary, "-v", "error", "-show_entries", "format=duration,size:stream=codec_name,codec_type,width,height,avg_frame_rate,sample_rate,channels", "-of", "json", str(p)], capture_output=True, text=True, timeout=30, check=False)
    except (OSError, subprocess.TimeoutExpired) as e:
        raise ToolError(f"ffprobe could not complete: {e}")
    if r.returncode:
        raise ToolError("ffprobe failed: " + r.stderr[:1000])
    try:
        metadata = json.loads(r.stdout)
    except json.JSONDecodeError:
        raise ToolError("ffprobe did not return valid JSON")
    return {"path": str(p), "metadata": metadata, "limitations": "Technical metadata only. No playback, audio, factual, rights or policy assessment was performed."}

FUNCTIONS = {"read_skill_guide": tool_read, "create_video_project": tool_create, "validate_timeline": validate_timeline, "check_story_plan": check_story_plan, "make_srt": make_srt, "inspect_video": inspect_video}

def result_for_tool(name, args):
    if name not in FUNCTIONS:
        raise ToolError(f"Unknown tool: {name}")
    if not isinstance(args, dict):
        raise ToolError("arguments must be an object")
    return FUNCTIONS[name](args)

def dispatch(method, params):
    if method == "initialize":
        return {"protocolVersion": VERSION, "capabilities": {"tools": {"listChanged": False}, "resources": {"subscribe": False, "listChanged": False}, "prompts": {"listChanged": False}}, "serverInfo": {"name": "cinematic-narrative-video", "version": "1.0.0"}, "instructions": "Use this server for skill guidance, project scaffolds and basic checks. The calling agent must create media and perform real quality reviews."}
    if method == "ping": return {}
    if method == "tools/list": return {"tools": TOOLS}
    if method == "tools/call":
        try:
            data = result_for_tool(params.get("name"), params.get("arguments", {}))
            return {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False, indent=2)}], "isError": False}
        except (ToolError, OSError, ValueError) as e:
            return {"content": [{"type": "text", "text": str(e)}], "isError": True}
    if method == "resources/list": return {"resources": RESOURCES}
    if method == "resources/templates/list": return {"resourceTemplates": []}
    if method == "resources/read":
        uri = params.get("uri", "")
        key = uri.removeprefix("cinematic://guide/") if isinstance(uri, str) and uri.startswith("cinematic://guide/") else ""
        if key not in DOCS: raise ToolError("Unknown resource URI")
        path, _ = DOCS[key]
        return {"contents": [{"uri": uri, "mimeType": "text/markdown", "text": (SKILL_ROOT / path).read_text(encoding="utf-8")} ]}
    if method == "prompts/list": return {"prompts": PROMPTS}
    if method == "prompts/get":
        if params.get("name") != "create_niche_video": raise ToolError("Unknown prompt")
        args = params.get("arguments", {})
        if not isinstance(args, dict): raise ToolError("Prompt arguments must be an object")
        topic, niche = require_string(args, "topic"), require_string(args, "niche")
        audience, extra = str(args.get("audience", "general audience")), str(args.get("requirements", "Use sensible defaults."))
        text = f"Create an original animated video using the cinematic-narrative-video skill. Topic: {topic}. Niche: {niche}. Audience: {audience}. Requirements: {extra}. Read the skill, structure, animation, rig, staging, niche and voice guides. Plan visual before/action/after states for meaningful beats and evaluate the actual encoded result with evidence-tagged checks. Draw original visuals with SVG/CSS/Canvas or similar code; do not use image generation. Create and inspect a short voiced style test before a full video. All spoken voices must use an American accent; use U.S. English for English speech and disclose if the accent is unavailable or unverified. Make voices energetic, confidently projected, clear and expressive, not boring; keep them appropriate to the topic without shouting or clipping. Plan the production, use your available TTS, coding and rendering capabilities, and deliver the actual video, thumbnail, captions, publishing guidance and honest quality report. Do not present drafts as finished media."
        return {"description": "Cross-niche video production prompt", "messages": [{"role": "user", "content": {"type": "text", "text": text}}]}
    raise LookupError(f"Method not found: {method}")

def send(value):
    sys.stdout.write(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        try:
            msg = json.loads(line)
            if not isinstance(msg, dict) or msg.get("jsonrpc") != "2.0" or not isinstance(msg.get("method"), str):
                raise ValueError("Invalid JSON-RPC request")
        except (json.JSONDecodeError, ValueError) as e:
            send({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}})
            continue
        if "id" not in msg:  # notifications never get a response
            continue
        ident, params = msg["id"], msg.get("params") or {}
        try:
            if not isinstance(params, dict): raise ToolError("params must be an object")
            response = {"jsonrpc": "2.0", "id": ident, "result": dispatch(msg["method"], params)}
        except LookupError as e:
            response = {"jsonrpc": "2.0", "id": ident, "error": {"code": -32601, "message": str(e)}}
        except (ToolError, OSError, ValueError) as e:
            response = {"jsonrpc": "2.0", "id": ident, "error": {"code": -32602, "message": str(e)}}
        send(response)

if __name__ == "__main__":
    main()
