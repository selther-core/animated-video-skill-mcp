# Installation

The canonical skill lives in `.agents/skills/cinematic-narrative-video/`. Its `SKILL.md`, references, examples, original example assets and reference stills form one self-contained directory. The optional server is at `mcp/server.py` in the **repository**, not inside a skill-only copy.

## Skill-capable agents

Use the host's documentation to identify its skill-discovery directory; it varies between Claude Code, Codex, OpenCode, Antigravity and versions. Keep all supporting folders together. This repository can already be used as project context by agents that discover `.agents/skills/` automatically; actual discovery depends on the host.

From the repository root, use the optional Python 3.9+ installer with an **existing** host skills directory:

```sh
# Preview only; substitute the actual documented skills directory.
python3 scripts/install_skill.py --skills-dir /absolute/path/to/skills

# After reviewing the plan, actually copy the skill.
python3 scripts/install_skill.py --skills-dir /absolute/path/to/skills --apply
```

The placeholder path must be replaced. The installer copies into `<skills-dir>/cinematic-narrative-video`, refuses to overwrite an existing directory, and does not alter agent configuration, configure MCP, download tools or install a renderer. It does not create a missing parent directory. Reload the host as needed and verify skill discovery in the host; a successful copy alone does not prove the host loaded it. The skill includes third-party reference stills: see its `reference-frames/README.md` before redistributing.

If you only copy the skill folder, retain the separate repository if you want to use its MCP server later. The standalone skill works without MCP.

## Agents without native skill support

Provide `.agents/skills/cinematic-narrative-video/SKILL.md` and its neighboring folders as ordinary project context. An agent that can clone or fetch files can load the repository itself; otherwise attach the ZIP or paste the needed instructions. The host still needs its own art, speech and rendering capabilities to produce a video. A text-only agent can prepare a plan and scripts, but cannot honestly claim to have rendered or reviewed a video.

## Optional MCP server

Follow [the MCP setup guide](../mcp/README.md) for Claude Code, Codex, OpenCode, Antigravity and other local stdio clients. Register it separately only when the agent supports MCP and the user approves the configuration. The server is local, requires Python 3.9+, and provides instructions, project scaffolding, basic timing/subtitle checks and optional `ffprobe` metadata; it does not generate video, images or speech.

## Verify

```sh
python3 tests/test_mcp.py
```

The tests exercise stdio requests and file paths as well as the installer. They do not establish that every agent host supports skill discovery, that MCP is connected in your installation, or that actual audiovisual production is possible. Use your agent's own status interface and perform an end-to-end media test when those capabilities are available.
