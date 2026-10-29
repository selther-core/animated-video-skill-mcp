# Cinematic narrative video — cross-niche skill + MCP package

This package includes an optional **local MCP server**. See [MCP setup and capabilities](mcp/README.md) for Claude Code, Codex, OpenCode, Antigravity and other stdio MCP clients. The server provides guides, project scaffolding and basic validation; it does not itself generate video, audio or images. The agent uses its own capabilities for those tasks.

## Contents

- `SKILL.md` — entry point, observation notes, workflow and quality gates.
- `mcp/server.py` and `mcp/README.md` — local stdio MCP server and integration instructions.
- `tests/test_mcp.py` — protocol and tool smoke tests.
- `references/visual-reference.md` and `reference-frames/` — analysis and eight actual stills extracted from the supplied excerpt. See the frames README for source, limits and redistribution caveats.
- `references/niche-adaptation.md` — apply the style across niches and genres.
- `examples/cross-niche-scripts.md` — sample briefs, scripts and storyboards across different niches.
- `references/character-rig.md` — proposed joint structure and pose library.
- `references/voice-direction.md` — written voice profiles, audition text and sound workflow. There are no voice samples.
- `examples/example-script-and-board.md` — original sample narration, TTS lines and scene plan.
- `examples/example-timeline.json` — original timing and scene-plan example.
- `examples/puppet-demo.html` — silent self-contained animated visual demonstration.
- `assets/` — three original SVG illustrations and PNG previews, with a usage README.

## Use with a skill-capable agent

Unzip the complete `cinematic-narrative-video-mcp` directory into a skill location supported by your agent (rename the folder to `cinematic-narrative-video` if your host requires the folder name to match the skill name). Keep `SKILL.md`, `mcp`, `references`, `examples` and `assets` together. Ask the agent to load the `cinematic-narrative-video` skill and give it your topic, niche, audience, intended length, language and any other requirements. Check the agent's current documentation for its exact path and whether a restart or enabling action is required; skill support differs by tool. Merely copying the file does not guarantee activation.

## Use with an agent without native skills

Provide the folder as project context or attach `SKILL.md` and whichever referenced files your agent can read. Ask it: “Read `SKILL.md`, then use the supporting examples to create an original video for [topic and requirements].” If it cannot access files, paste the skill and the needed reference text directly. Native image and TTS tools should be used when available; no particular outside provider or web service is required by this package.

## Important limits

The reference video was only available as a 3:57.9 excerpt of a 6:58 original. Its visuals were sampled once per second, with four selected seconds inspected frame by frame; the audio was not auditioned. The rest of the original video, the reference's exact sounds and production techniques, and the original character rigs remain unknown. The voice details in this package are original recommendations, not an analysis of how the source narrator sounds. The illustrations in `assets/` and the demo are original examples, not final thumbnails or a finished animation renderer. The separate `reference-frames/` folder contains extracted source stills; check the rights needed before redistributing them.
