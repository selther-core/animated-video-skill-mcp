# Cinematic narrative video — cross-niche skill + MCP package

This package includes an optional **local MCP server**. See [MCP setup and capabilities](mcp/README.md) for Claude Code, Codex, OpenCode, Antigravity and other stdio MCP clients. The server provides guides, project scaffolding and basic validation; it does not itself generate video, audio or images. The agent uses its own capabilities for those tasks.

## Quick start — copy and paste into your agent

Replace the bracketed fields below, then paste the entire prompt into Claude Code, Codex, OpenCode, Antigravity, Arena Agent Mode, or another capable agent. It works for **any content niche**, not only science. The agent should do the setup and production itself when its permissions and tools allow.

```text
Use this skill to create an original animated video:
https://github.com/selther-core/animated-video-skill-mcp

Topic: [describe the video topic]
Niche and target audience: [niche and audience]
Story goal or main message: [what the video should communicate]
Length and format: [e.g. 4 minutes, 16:9 YouTube; or 60 seconds, 9:16]
Language and voice direction: [language, voice qualities, tone]
Other requirements: [characters, animals, locations, visual style, factual sources,
                   brand guidelines, accessibility needs, or “use your judgment”]

First access the repository in the way available to you: use an existing local copy,
clone/download it into the workspace if permitted, or read the files through available
web/file tools. Read SKILL.md and references/niche-adaptation.md; consult the visual
reference, character-rig, voice-direction, relevant examples and reference frames as
needed. Adapt the reference-inspired animation and visual language to my niche. Treat
the source frames as research references, not reusable production assets.

If you support native skills, use the skill in this session or install it in an
appropriate project location only if allowed. If you do not support skills, follow
SKILL.md as ordinary instructions. MCP is optional: use the included local stdio
server only if you can run and configure it and have permission. Do not treat MCP
as a substitute for your own image, speech, editing, rendering, or review tools.

Do the work, not just a plan: research factual claims when needed; write an original
script and storyboard; make original characters, settings, motion, visual assets,
thumbnail and appropriate sound; use your own available TTS/image tools directly;
render the video; and review it against the skill checklist. Revise problems you can
fix. Deliver the finished video, thumbnail, narration/TTS text, captions, title,
description with sources as appropriate, a playlist recommendation, publishing
instructions and a truthful quality report. Verify runtime and output files.

Only ask me a focused question when an essential requirement or permission is
missing. If a capability is genuinely unavailable, do as much as you can, explain
the exact blocker, and never claim an unrendered, unvoiced or unreviewed draft is a
finished video. Do not claim exact matching of the reference's unexamined ending or
audio. Do not publish or upload anything without my authorization.
```

### Arena or another agent without native skills

The same prompt above is the recommended option. If the agent can access the repository, it can read `SKILL.md` and the supporting files as ordinary project instructions—no skills feature or MCP installation is necessary. If repository access is blocked, attach the package ZIP or the relevant files, or provide the text directly. If it has built-in image generation or TTS, it should use those capabilities instead of sending you to another service. It must disclose any actual tool or rendering limits.

### Optional: add the MCP tools

Copy this into a **local MCP-capable agent** after it has access to the repository:

```text
Read mcp/README.md from https://github.com/selther-core/animated-video-skill-mcp.
If you can run a local Python stdio MCP server and have permission, configure the
included server for this project using my host's current instructions; preserve all
existing settings. Run the included tests and verify the server connects. Explain
which tools are available. If local MCP is not supported, skip installation and use
SKILL.md as ordinary instructions instead. Do not claim the MCP creates videos,
images, narration or performs a full audiovisual review by itself.
```

**Compatibility:** The skill is a portable instruction package, and the MCP server uses standard local stdio. Different agents have different capabilities and permission models: a text-only agent can follow the guidance and draft a plan, but it cannot produce a finished audiovisual file without access to appropriate media tools. The included server has been smoke-tested with the Python MCP client SDK; individual hosts, their current versions, and every possible TTS/rendering combination have not all been tested. See [MCP setup](mcp/README.md) for host-specific configuration.

## Contents

- `SKILL.md` — entry point, observation notes, workflow and quality gates.
- `mcp/server.py` and `mcp/README.md` — local stdio MCP server and integration instructions.
- `tests/test_mcp.py` — protocol and tool smoke tests.
- `references/visual-reference.md` and `reference-frames/` — analysis and eight actual stills extracted from the supplied excerpt. See the frames README for source, limits and redistribution caveats.
- `references/niche-adaptation.md` — apply the style across niches and genres.
- `references/agent-compatibility.md` — choose an execution path for skill-aware, MCP-capable, workspace and text-only agents.
- `examples/cross-niche-scripts.md` — sample briefs, scripts and storyboards across different niches.
- `references/character-rig.md` — proposed joint structure and pose library.
- `references/voice-direction.md` — written voice profiles, audition text and sound workflow. There are no voice samples.
- `examples/example-script-and-board.md` — original sample narration, TTS lines and scene plan.
- `examples/example-timeline.json` — original timing and scene-plan example.
- `examples/puppet-demo.html` — silent self-contained animated visual demonstration.
- `assets/` — three original SVG illustrations and PNG previews, with a usage README.

## Quick start from GitHub

Clone the repository using the directory name expected by the setup examples:

```sh
git clone https://github.com/selther-core/animated-video-skill-mcp.git cinematic-narrative-video-mcp
python3 cinematic-narrative-video-mcp/tests/test_mcp.py
```

Then follow [the MCP setup guide](mcp/README.md) to register the server in your client. Alternatively, read `SKILL.md` directly without MCP. You can clone into a different directory, but substitute that actual directory path in every setup command. The reference frames are third-party source material; see their [rights notice](reference-frames/README.md) before redistributing them.

## Use with a skill-capable agent

Unzip the complete `cinematic-narrative-video-mcp` directory into a skill location supported by your agent (rename the folder to `cinematic-narrative-video` if your host requires the folder name to match the skill name). Keep `SKILL.md`, `mcp`, `references`, `examples` and `assets` together. Ask the agent to load the `cinematic-narrative-video` skill and give it your topic, niche, audience, intended length, language and any other requirements. Check the agent's current documentation for its exact path and whether a restart or enabling action is required; skill support differs by tool. Merely copying the file does not guarantee activation.

## Use with an agent without native skills

Provide the folder as project context or attach `SKILL.md` and whichever referenced files your agent can read. Ask it: “Read `SKILL.md`, then use the supporting examples to create an original video for [topic and requirements].” If it cannot access files, paste the skill and the needed reference text directly. Native image and TTS tools should be used when available; no particular outside provider or web service is required by this package.

## Important limits

The reference video was only available as a 3:57.9 excerpt of a 6:58 original. Its visuals were sampled once per second, with four selected seconds inspected frame by frame; the audio was not auditioned. The rest of the original video, the reference's exact sounds and production techniques, and the original character rigs remain unknown. The voice details in this package are original recommendations, not an analysis of how the source narrator sounds. The illustrations in `assets/` and the demo are original examples, not final thumbnails or a finished animation renderer. The separate `reference-frames/` folder contains extracted source stills; check the rights needed before redistributing them.
