# Optional local MCP server

A real, minimal stdio [Model Context Protocol](https://modelcontextprotocol.io/) server is included at `server.py`. It uses Python 3.9+ and the standard library only. It implements JSON-RPC over newline-delimited stdio and advertises MCP `2025-06-18`, tools, text resources and a prompt. It is not an HTTP server and does not need an API key. The skill itself still works without MCP.

## What this server can do

| MCP tool | Actual behavior |
|---|---|
| `read_skill_guide` | Read one of the bundled skill, intake, scene/wardrobe selection, niche, detailed production manual, compatibility, visual, animation, rig, staging, structure, example breakdown, voice or example documents. |
| `create_video_project` | After the agent has completed intake, create a **new** project directory with the resolved backgrounds, video type, niche, length, voice and other brief fields and draft script, storyboard, timeline, QA and publishing templates. Refuses existing directories. Parent directory must already exist. |
| `validate_timeline` | Check numeric durations, shot coverage, gaps, overlaps, and some cue bounds. Does not assess whether media exists, creative quality, accuracy, rights, actual sync, accessibility or policy. |
| `check_story_plan` | Check manually supplied beat fields and event time bounds; does not inspect the video, verify sources or judge quality. |
| `make_srt` | Turn manually supplied timed text cues into SRT. Does not transcribe or align audio; the agent must review cue timing. |
| `inspect_video` | Use `ffprobe` if already installed and on `PATH` to report a local file's stream/duration metadata. It does not play, hear or judge the video. |

The server also exposes fourteen text resources (`cinematic://guide/skill`, `niche`, `production`, `intake`, `selection`, `compatibility`, `visual`, `animation`, `rig`, `staging`, `structure`, `audit`, `voice`, `examples`) and a `create_niche_video` prompt. Resources and prompts may not appear in all MCP clients. The **agent** still researches and writes, authors original assets, uses connected TTS when requested, animates and renders, listens and reviews when possible, and creates the requested deliverables. This server does **not** generate media, TTS, image assets or a finished video. It has no automatic access to the agent's connected image/TTS providers and does not publish anything.

## Setup

1. Clone or unzip the whole repository to a stable directory on the same machine where the agent runs. Keep `mcp/server.py` and `.agents/skills/cinematic-narrative-video/` in their original relative locations. In a terminal, **change into the repository root** (the folder containing `mcp/`), then:

   ```sh
   python3 --version
   python3 tests/test_mcp.py
   ```

   The server requires Python 3.9+. For `inspect_video`, install or use an existing `ffprobe` separately if needed; this is optional for the other features. Tests do not require `ffprobe`. Do not manually start the server in an interactive terminal; the MCP client launches it and communicates through stdio.
2. Register **one** configuration below in your agent. Run the shell commands from the repository root and preserve existing settings. The commands use `$(pwd)` to record the actual absolute path at registration time. On Windows use a Python executable and an absolute Windows path supported by your client.
3. Restart or reload the agent if necessary, confirm the server appears connected, then ask the agent to list the cinematic video tools. A saved config alone is not proof of a successful connection. Permissions may require explicit approval for file creation.

### Claude Code

```sh
claude mcp add --transport stdio cinematic-video -- python3 "$(pwd)/mcp/server.py"
claude mcp list
```

Use `/mcp` inside Claude Code to inspect connection status. To use the skill as a native skill as well, follow the host's current skill-installation documentation; configuring MCP does not automatically install the skill. [Official Claude Code MCP guide](https://code.claude.com/docs/en/mcp).

### Codex CLI

```sh
codex mcp add cinematic-video -- python3 "$(pwd)/mcp/server.py"
codex mcp list
```

Or configure a stdio server under `[mcp_servers.cinematic-video]` in Codex's applicable `config.toml` with `command = "python3"` and an `args` array containing the absolute path to `mcp/server.py`. Keep existing config intact. [Official Codex MCP guide](https://developers.openai.com/codex/mcp).

### OpenCode

In the relevant `opencode.json`, add a `cinematic-video` entry under `mcp`. Set its `type` to `local`, its `command` array to `python3` followed by the actual absolute path to `mcp/server.py`, and `enabled` to `true`. Merge it with existing entries rather than replacing them. See [OpenCode's MCP documentation](https://opencode.ai/docs/mcp-servers/) for the configuration format and connection management.

### Antigravity and other MCP clients

In your client's MCP server manager, add a **local stdio** server named `cinematic-video`, using `python3` as the command and the actual absolute path to `mcp/server.py` as its single argument. Use the app's documentation to locate its active configuration; names and paths change between versions. Do not overwrite other servers. Client support for resources and prompts varies; tools are the primary interface. If the client does not support local stdio MCP, use the skill files directly instead.

## Example agent request

> Use the cinematic-video MCP tools and the cinematic-narrative-video skill. Make a 60-second fictional story about a nervous fox learning to share, for a family audience, in 16:9. Create a new project in my workspace, then make the finished video, an original thumbnail, captions, and publishing notes. Use code-drawn visuals and connected TTS if needed; do not use image generation; check the output and report any unfinished checks.

The MCP can scaffold and check parts of the plan; the agent must do the creative work and rendering. Before calling `create_video_project`, the agent should choose a **nonexistent** directory in an allowed workspace. Never claim the scaffold itself is the finished video.

## Privacy and safety

The server runs locally under your user account and can inspect a supplied media path and create a new directory wherever that account has permission. It refuses an existing project directory, although a failed creation can leave partial files. `inspect_video` runs the `ffprobe` found on `PATH`, with fixed arguments, no shell and a 30-second timeout; use a trusted executable and avoid untrusted media. The server does not itself explicitly upload files or include telemetry, authentication or a deletion function. It does not sandbox `ffprobe` or block network access by subprocesses, the MCP client or other tools. Treat paths and content as untrusted, review permissions, and do not expose stdio publicly without a separate security design. See [SECURITY.md](../SECURITY.md).

## Troubleshooting and tests

- **No connection:** check the absolute script path, Python executable, local stdio selection, client logs, and reload. Avoid wrapper commands that print banners to stdout; stdout carries only protocol messages.
- **Cannot create project:** parent must exist and the requested project directory must not exist. Choose a fresh name; no files are overwritten.
- **ffprobe missing:** use the agent's available media-inspection tool or add ffprobe to PATH; do not claim inspection happened.
- **Protocol / behavior check:** run `python3 tests/test_mcp.py` from the repository root. The tests start the server as a child process and cover handshake, tool/resource/prompt discovery, project creation and no-overwrite behavior, timeline checks, subtitle formatting and tool errors. Development smoke testing also connected through the official Python MCP client SDK and exercised initialization, discovery and tool calls. These checks do not test any particular host's UI or complete video production.
- The current project-authored example was sampled visually and decoded, but full-speed subjective motion and direct audio audition remain unverified. No video or audio is included in the skill package.
