# Optional local MCP server

A real, minimal stdio [Model Context Protocol](https://modelcontextprotocol.io/) server is included at `server.py`. It uses Python 3.9+ and the standard library only. It implements JSON-RPC over newline-delimited stdio and advertises MCP `2025-06-18`, tools, text resources and a prompt. It is not an HTTP server and does not need an API key. The skill itself still works without MCP.

## What this server can do

| MCP tool | Actual behavior |
|---|---|
| `read_skill_guide` | Read one of the bundled skill, niche, visual reference, rig, voice or example documents. |
| `create_video_project` | Create a **new**, empty project directory with the supplied brief and draft script, storyboard, timeline, QA and publishing templates. Refuses existing directories. Parent directory must already exist. |
| `validate_timeline` | Check numeric durations, shot coverage, gaps, overlaps, and some cue bounds. Does not assess whether media exists, creative quality, accuracy, rights, actual sync, accessibility or policy. |
| `make_srt` | Turn manually supplied timed text cues into SRT. Does not transcribe or align audio; the agent must review cue timing. |
| `inspect_video` | Use `ffprobe` if already installed and on `PATH` to report a local file's stream/duration metadata. It does not play, hear or judge the video. |

The server also exposes six text resources (`cinematic://guide/skill`, `niche`, `visual`, `rig`, `voice`, `examples`) and a `create_niche_video` prompt. Resources and prompts may not appear in all MCP clients. The **agent** still researches and writes, creates or generates original assets, uses any connected TTS, animates and renders, listens and reviews, and creates the final video/thumbnail/publishing package. This server does **not** generate media, TTS, image assets or a finished video. It has no automatic access to the agent's connected image/TTS providers and does not publish anything.

## Setup

1. Unzip the whole package to a stable directory on the same machine where the agent runs. Keep `mcp/server.py` and all skill files together. In a terminal, change to the directory **containing** the unzipped `cinematic-narrative-video-mcp` folder, then:

   ```sh
   SKILL_DIR="$(pwd)/cinematic-narrative-video-mcp"
   python3 --version
   python3 "$SKILL_DIR/tests/test_mcp.py"
   ```

   The server requires Python 3.9+. For `inspect_video`, install or use an existing `ffprobe` separately if needed; this is optional for the other features. Tests do not require `ffprobe`. Do not manually start the server in an interactive terminal; the MCP client launches it and communicates through stdio.
2. Register **one** configuration below in your agent. Preserve your existing settings. `$SKILL_DIR` in the shell examples expands to an absolute path **at registration time**; do not paste that literal variable into JSON/TOML. Paths with spaces are safe when kept in one argument. On Windows use a Python executable and an absolute Windows path supported by your client.
3. Restart or reload the agent if necessary, confirm the server appears connected, then ask the agent to list the cinematic video tools. A saved config alone is not proof of a successful connection. Permissions may require explicit approval for file creation.

### Claude Code

```sh
claude mcp add --transport stdio cinematic-video -- python3 "$SKILL_DIR/mcp/server.py"
claude mcp list
```

Use `/mcp` inside Claude Code to inspect connection status. To use the skill as a native skill as well, follow the host's current skill-installation documentation; configuring MCP does not automatically install the skill. [Official Claude Code MCP guide](https://code.claude.com/docs/en/mcp).

### Codex CLI

```sh
codex mcp add cinematic-video -- python3 "$SKILL_DIR/mcp/server.py"
codex mcp list
```

Or configure a stdio server under `[mcp_servers.cinematic-video]` in Codex's applicable `config.toml` with `command = "python3"` and an `args` array containing the absolute path to `mcp/server.py`. Keep existing config intact. [Official Codex MCP guide](https://developers.openai.com/codex/mcp).

### OpenCode

Merge the following into the relevant `opencode.json`, replacing the example path with the **actual absolute path** to `server.py`:

```json
{
  "mcp": {
    "cinematic-video": {
      "type": "local",
      "command": ["python3", "/absolute/path/to/cinematic-narrative-video-mcp/mcp/server.py"],
      "enabled": true
    }
  }
}
```

The path is an example and must be replaced. See [OpenCode's MCP documentation](https://opencode.ai/docs/mcp-servers/) for configuration precedence and connection management.

### Antigravity and other MCP clients

In your version's MCP server manager, add a **local stdio** server with command `python3` and one argument: the actual absolute path to `mcp/server.py`. If it uses an `mcpServers` JSON object, the generic entry is:

```json
{
  "mcpServers": {
    "cinematic-video": {
      "command": "python3",
      "args": ["/absolute/path/to/cinematic-narrative-video-mcp/mcp/server.py"]
    }
  }
}
```

Replace the example path; use the app's own settings UI to locate its active configuration because names and paths change between versions. Do not overwrite other servers. Client versions can differ in support for MCP resources and prompts; the tools interface is the primary path. If a client does not support local stdio MCP, use the skill files directly instead.

## Example agent request

> Use the cinematic-video MCP tools and the cinematic-narrative-video skill. Make a 60-second fictional story about a nervous fox learning to share, for a family audience, in 16:9. Create a new project in my workspace, then make the finished video, an original thumbnail, captions, and publishing notes. Use your connected TTS and image tools if needed; check the output and report any unfinished checks.

The MCP can scaffold and check parts of the plan; the agent must do the creative work and rendering. Before calling `create_video_project`, the agent should choose a **nonexistent** directory in an allowed workspace. Never claim the scaffold itself is the finished video.

## Privacy and safety

The server runs locally under your user account and can read the specified media path and create the specified new directory wherever that account has permission. It will not overwrite an existing project directory or run arbitrary commands; `inspect_video` invokes only the `ffprobe` executable it finds on `PATH`, with a fixed argument list, no shell and a 30-second timeout. There is no network connection, telemetry, authentication or deletion function. Treat all user-supplied paths and generated content as untrusted, review permissions, and do not expose this stdio process as a public server without a proper security design.

## Troubleshooting and tests

- **No connection:** check the absolute script path, Python executable, local stdio selection, client logs, and reload. Avoid wrapper commands that print banners to stdout; stdout carries only protocol messages.
- **Cannot create project:** parent must exist and the requested project directory must not exist. Choose a fresh name; no files are overwritten.
- **ffprobe missing:** use the agent's available media-inspection tool or add ffprobe to PATH; do not claim inspection happened.
- **Protocol / behavior check:** run `python3 "$SKILL_DIR/tests/test_mcp.py"`. The tests start the server as a child process and cover handshake, tool/resource/prompt discovery, project creation and no-overwrite behavior, timeline checks, subtitle formatting and tool errors. Development smoke testing also connected through the official Python MCP client SDK and exercised initialization, discovery and tool calls. These checks do not test any particular host's UI or complete video production.
- The reference analysis remains partial: the supplied excerpt was 3:57.9 of 6:58; visuals were sampled, and the source audio was not auditioned. Do not imply exact style or voice matching is verified.
