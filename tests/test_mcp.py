#!/usr/bin/env python3
"""End-to-end smoke tests for the server's stdio JSON-RPC interface."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / "mcp" / "server.py"
SKILL_ROOT = ROOT / ".agents" / "skills" / "cinematic-narrative-video"

def req(ident, method, params=None):
    return {"jsonrpc": "2.0", "id": ident, "method": method, "params": params or {}}

def run_server(messages):
    data = "".join(json.dumps(m) + "\n" for m in messages)
    p = subprocess.run([sys.executable, str(SERVER)], input=data, text=True, capture_output=True, timeout=30, check=True)
    if p.stderr:
        raise AssertionError(f"Unexpected stderr: {p.stderr}")
    return [json.loads(line) for line in p.stdout.splitlines()]

def call(ident, name, arguments):
    return req(ident, "tools/call", {"name": name, "arguments": arguments})

def tool_data(response):
    assert not response["result"]["isError"], response
    return json.loads(response["result"]["content"][0]["text"])

class MCPTests(unittest.TestCase):
    def test_handshake_discovery_resources_and_prompt(self):
        msgs = [req(1, "initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "smoke", "version": "1"}}),
                {"jsonrpc": "2.0", "method": "notifications/initialized"}, req(2, "tools/list"), req(3, "resources/list"),
                req(4, "resources/read", {"uri": "cinematic://guide/niche"}), req(5, "prompts/list"),
                req(6, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "bread", "niche": "business"}})]
        out = run_server(msgs)
        self.assertEqual(len(out), 6)
        self.assertEqual(out[0]["result"]["protocolVersion"], "2025-06-18")
        self.assertEqual(len(out[1]["result"]["tools"]), 6)
        self.assertTrue(out[2]["result"]["resources"])
        self.assertIn("any niche", out[3]["result"]["contents"][0]["text"].lower())
        self.assertEqual(out[4]["result"]["prompts"][0]["name"], "create_niche_video")
        self.assertIn("bread", out[5]["result"]["messages"][0]["content"]["text"])

    def test_extracted_frame_guide_and_images(self):
        reply = run_server([call(1, "read_skill_guide", {"guide": "visual"})])[0]
        guide = tool_data(reply)
        self.assertIn("reference-frames", guide["content"])
        self.assertEqual(len(list((SKILL_ROOT / "reference-frames").glob("*.jpg"))), 10)
        self.assertTrue((SKILL_ROOT / "reference-frames" / "08-field.jpg").is_file())
        self.assertFalse((SKILL_ROOT / "reference-frames" / "00-02-street-character.jpg").exists())
        self.assertIn("rights", (SKILL_ROOT / "reference-frames" / "README.md").read_text().lower())

    def test_agent_compatibility_and_quickstart(self):
        reply = run_server([call(1, "read_skill_guide", {"guide": "compatibility"})])[0]
        guide = tool_data(reply)
        self.assertIn("Text-only agent", guide["content"])
        readme = (ROOT / "README.md").read_text()
        self.assertIn("# Installation", readme)
        self.assertIn("Install the cinematic-narrative-video skill", readme)
        self.assertIn("MCP is optional", readme)
        installation_prompt = readme.split("```text", 1)[1].split("```", 1)[0].strip()
        self.assertLess(len(installation_prompt), 250)
        self.assertIn("https://github.com/selther-core/animated-video-skill-mcp", installation_prompt)
        self.assertNotIn("Do not create a video", installation_prompt)
        resources = run_server([req(1, "resources/list")])[0]["result"]["resources"]
        self.assertIn("cinematic://guide/compatibility", [r["uri"] for r in resources])

    def test_american_voice_guide_and_prompt(self):
        responses = run_server([
            call(1, "read_skill_guide", {"guide": "voice"}),
            req(2, "resources/read", {"uri": "cinematic://guide/voice"}),
            req(3, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "bread", "niche": "business"}}),
        ])
        guide = tool_data(responses[0])["content"]
        self.assertIn("All spoken voices in this skill must use an American accent", guide)
        self.assertIn("en-US", guide)
        self.assertIn("Voice types to use for each niche", guide)
        self.assertIn("Topic scripts and voice examples", guide)
        self.assertIn("energetic, confidently projected, clear and engaging", guide)
        self.assertIn("Loud does not mean shouting, clipping", guide)
        self.assertIn("The bakery queue", guide)
        self.assertEqual(responses[1]["result"]["contents"][0]["text"], guide)
        prompt = responses[2]["result"]["messages"][0]["content"]["text"]
        self.assertIn("All spoken voices must use an American accent", prompt)

    def test_code_animation_guide_and_demo(self):
        out = run_server([
            call(1, "read_skill_guide", {"guide": "animation"}),
            req(2, "resources/read", {"uri": "cinematic://guide/animation"}),
            req(3, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "oil", "niche": "education"}}),
        ])
        guide = tool_data(out[0])["content"]
        self.assertIn("do not call an image-generation model", guide.lower())
        self.assertIn("What was inspected—and what cannot be known", guide)
        self.assertEqual(out[1]["result"]["contents"][0]["text"], guide)
        prompt = out[2]["result"]["messages"][0]["content"]["text"]
        self.assertIn("do not use image generation", prompt)
        self.assertIn("style test", prompt)
        demo = (SKILL_ROOT / "examples" / "backyard-vector-demo.html").read_text()
        self.assertIn("window.seek=seek", demo)
        self.assertIn('id="person"', demo)
        self.assertIn('id="diagram-scene"', demo)
        self.assertNotIn("<img", demo.lower())
        self.assertTrue((SKILL_ROOT / "examples" / "render_vector_demo.py").is_file())

    def test_staging_and_current_rig(self):
        replies = run_server([
            call(1, "read_skill_guide", {"guide": "staging"}),
            req(2, "resources/read", {"uri": "cinematic://guide/staging"}),
            call(3, "read_skill_guide", {"guide": "rig"}),
        ])
        guide = tool_data(replies[0])["content"]
        self.assertIn("lighting", guide.lower())
        self.assertIn("cutaway", guide.lower())
        self.assertEqual(guide, replies[1]["result"]["contents"][0]["text"])
        self.assertIn("back arm → torso → near leg → front arm", tool_data(replies[2])["content"])
        demo = (SKILL_ROOT / "examples" / "staging-rig-demo.html").read_text()
        self.assertIn("window.seek=seek", demo)
        self.assertIn('class="backArm"', demo)
        self.assertIn('class="torso"', demo)
        self.assertIn('class="frontArm"', demo)
        self.assertLess(demo.index('class="backArm"'), demo.index('class="torso"'))
        self.assertLess(demo.index('class="torso"'), demo.index('class="frontArm"'))
        self.assertNotIn("<img", demo.lower())
        self.assertNotIn("<audio", demo.lower())

    def test_story_structure_guides_and_example_plan(self):
        plan = json.loads((SKILL_ROOT / "examples" / "story-beat-template.json").read_text())
        out = run_server([
            call(1, "read_skill_guide", {"guide": "structure"}),
            req(2, "resources/read", {"uri": "cinematic://guide/structure"}),
            call(3, "read_skill_guide", {"guide": "audit"}),
            call(4, "check_story_plan", {"plan": plan}),
        ])
        guide = tool_data(out[0])["content"]
        self.assertIn("BEFORE", guide)
        self.assertIn("unknown", guide.lower())
        self.assertEqual(guide, out[1]["result"]["contents"][0]["text"])
        self.assertIn("WWII cut", tool_data(out[2])["content"])
        result = tool_data(out[3])
        self.assertTrue(result["fields_valid"], result)
        self.assertIn("does not inspect media", " ".join(result["warnings"]))
        demo = (SKILL_ROOT / "examples" / "progressive-scene-demo.html").read_text()
        self.assertIn("window.seek=seek", demo)
        self.assertIn('id="queue"', demo)
        self.assertIn('id="pickup-zone"', demo)
        self.assertIn('id="route"', demo)
        self.assertNotIn("<audio", demo.lower())
        self.assertNotIn("<img", demo.lower())

    def test_prompt_first_and_scene_selection(self):
        replies = run_server([
            call(1, "read_skill_guide", {"guide": "intake"}),
            req(2, "resources/read", {"uri": "cinematic://guide/selection"}),
            req(3, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "a fox finds a kite"}}),
        ])
        guide = tool_data(replies[0])["content"].lower()
        for phrase in ("installation is not production", "backgrounds", "length", "video type", "niche", "voice"):
            self.assertIn(phrase, guide)
        selection = replies[1]["result"]["contents"][0]["text"].lower()
        self.assertIn("wardrobe", selection)
        self.assertIn("continuity", selection)
        prompt = replies[2]["result"]["messages"][0]["content"]["text"].lower()
        self.assertIn("then ask", prompt)
        self.assertIn("backgrounds", prompt)
        self.assertIn("after answers, start production", prompt)
        source = (SKILL_ROOT / "examples" / "ww2-seekable-scene.html").read_text()
        self.assertIn("window.seek=seek9", source)
        self.assertNotIn("<audio", source.lower())
        self.assertNotIn("<img", source.lower())

    def test_progressive_disclosure_and_cross_niche(self):
        core = (SKILL_ROOT / "SKILL.md").read_text()
        self.assertLess(len(core.encode()), 12000)
        for text in ("references/production-manual.md", "character-free", "voice-free", "American accent", "Do not use image-generation"):
            self.assertIn(text, core)
        response = run_server([
            call(1, "read_skill_guide", {"guide": "production"}),
            req(2, "resources/read", {"uri": "cinematic://guide/production"}),
            call(3, "read_skill_guide", {"guide": "niche"}),
            req(4, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "silent software tutorial"}}),
        ])
        manual = tool_data(response[0])["content"]
        self.assertIn("Timeline contract", manual)
        self.assertIn("ffmpeg", manual)
        self.assertIn("Quality gate", manual)
        self.assertEqual(manual, response[1]["result"]["contents"][0]["text"])
        niche = tool_data(response[2])["content"]
        self.assertIn("Adapt an unfamiliar or mixed niche", niche)
        self.assertIn("If it has no speech, omit TTS", niche)
        prompt = response[3]["result"]["messages"][0]["content"]["text"]
        self.assertIn("voice only if requested", prompt)
        self.assertIn("no character rig for character-free videos", prompt)
        example = (SKILL_ROOT / "examples" / "cross-niche-scripts.md").read_text()
        self.assertIn("Silent software tutorial", example)
        self.assertIn("Fictional product promotion", example)

    def test_scaffold_requires_intake_fields_before_creating(self):
        with tempfile.TemporaryDirectory() as parent:
            folder = str(Path(parent) / "video")
            args = {"directory": folder, "topic": "Fox", "niche": "Fiction", "audience": "Family", "length": "one minute", "format": "16:9"}
            response = run_server([call(1, "create_video_project", args)])[0]
            self.assertTrue(response["result"]["isError"])
            self.assertFalse(Path(folder).exists())

    def test_story_plan_invalid_and_intentional_hold(self):
        beat = {"id":"one", "start":0, "end":3, "purpose":"quiet moment", "before":"arrival", "action":"hold", "after":"attention", "hold":"two seconds", "source_or_fiction":"fiction", "events":[], "intentional_hold":True}
        p = {"duration_seconds": 3, "beats": [beat]}
        invalid = {"duration_seconds": 3, "beats": [{**beat, "events": [{"time": 4, "change":"", "meaning":""}]}]}
        out = run_server([call(1, "check_story_plan", {"plan": p}), call(2, "check_story_plan", {"plan": invalid})])
        good, bad = tool_data(out[0]), tool_data(out[1])
        self.assertTrue(good["fields_valid"])
        self.assertFalse(any("no planned visual events" in w for w in good["warnings"]))
        self.assertFalse(bad["fields_valid"])
        self.assertTrue(any(".time" in e for e in bad["issues"]))
        self.assertTrue(any(".change" in e for e in bad["issues"]))
        self.assertTrue(any(".meaning" in e for e in bad["issues"]))

    def test_create_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as parent:
            folder = str(Path(parent) / "video")
            args = {"directory": folder, "topic": "Forest", "niche": "Fiction", "audience": "Families", "length": "1 minute", "format": "16:9", "backgrounds": "forest and clearing", "video_type": "fiction story", "voice": "warm American narrator"}
            first, second = run_server([call(1, "create_video_project", args), call(2, "create_video_project", args)])
            self.assertEqual(tool_data(first)["status"], "draft_scaffold_created")
            self.assertTrue(second["result"]["isError"])
            self.assertEqual(json.loads((Path(folder)/"brief.json").read_text())["niche"], "Fiction")
            self.assertTrue((Path(folder)/"timeline.json").is_file())
            self.assertTrue((Path(folder)/"story-beats.json").is_file())
            self.assertTrue((Path(folder)/"scene-wardrobe.md").is_file())
            brief = json.loads((Path(folder)/"brief.json").read_text())
            self.assertEqual(brief["backgrounds"], "forest and clearing")
            self.assertEqual(brief["video_type"], "fiction story")
            self.assertEqual(brief["voice"], "warm American narrator")
            self.assertIn("Do not use AI image generation", (Path(folder)/"storyboard.md").read_text())
            self.assertIn("code-drawn style test reviewed and corrected, with voice if requested", (Path(folder)/"quality_report.md").read_text())

    def test_timeline_and_srt(self):
        good = {"duration_seconds": 10, "shots": [{"start": 0, "end": 4}, {"start": 4, "end": 10}]}
        bad = {"duration_seconds": 10, "shots": [{"start": 0, "end": 4}, {"start": 5, "end": 10}]}
        o = run_server([call(1,"validate_timeline", {"timeline":good}), call(2,"validate_timeline", {"timeline":bad}),
                        call(3,"make_srt", {"cues":[{"start":1.25,"end":2.5,"text":"Hello."}]}),
                        call(4,"make_srt", {"cues":[{"start":2,"end":1,"text":"Bad."}]})])
        self.assertTrue(tool_data(o[0])["timing_valid"])
        self.assertFalse(tool_data(o[1])["timing_valid"])
        self.assertIn("00:00:01,250 --> 00:00:02,500", tool_data(o[2])["srt"])
        self.assertTrue(o[3]["result"]["isError"])

    def test_invalid_tool_and_absent_video(self):
        out = run_server([call(1, "bad_tool", {}), call(2, "inspect_video", {"path": "/path-that-does-not-exist"})])
        self.assertTrue(out[0]["result"]["isError"])
        self.assertTrue(out[1]["result"]["isError"])

if __name__ == "__main__":
    unittest.main()
