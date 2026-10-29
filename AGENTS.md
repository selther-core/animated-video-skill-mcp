# Repository guidance

- The canonical skill is `.agents/skills/cinematic-narrative-video/`; keep `SKILL.md` and its supporting files together. Edit this source rather than maintaining duplicate copies.
- `mcp/server.py` provides optional local MCP integration; `scripts/install_skill.py` copies the skill only; see `docs/installation.md` and `mcp/README.md` for their limitations.
- Preserve the evidence boundary: source visuals were sampled from a 3:57.9 excerpt, only four selected seconds were inspected frame by frame, and reference audio and the ending were not auditioned or visually reviewed. Do not claim exact audio or full-video fidelity.
- Treat `reference-frames/` inside the skill as third-party reference material with its own source and rights notice; `assets/` contains separate original examples.
- For changes, run `python3 tests/test_mcp.py`; test installer and path changes as well as MCP. Do not store tokens, secrets, source videos, extracted audio, build output or temporary tools in this repository.
- Do not overwrite user files, alter global agent settings or publish media without appropriate authorization. Report actual limitations and tests rather than promising universal compatibility.
