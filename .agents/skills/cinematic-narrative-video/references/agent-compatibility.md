# Cross-agent compatibility and capability-driven execution

This package is designed to be **usable as instructions** by different kinds of agents; the agent's actual abilities still determine which outputs it can produce. A skill file and an MCP server do not give a text-only agent a video renderer, image generator, TTS model, internet access, or permission to upload files. Never promise compatibility with every host/version or claim a successful media render or review without checking.

## 1. Pick the host integration that actually exists

| Agent capabilities | How to use the package |
|---|---|
| Native skill support | Load `SKILL.md` with its `references/`, `examples/`, `assets/` and `reference-frames/` folders available. If installing, use the host's documented discovery location and permissions. Loading a skill and registering MCP are separate actions. |
| File-reading/project context, but no native skills | Read `SKILL.md` as ordinary instructions and consult the relative supporting files. No installation or MCP server is required. |
| Agent with workspace tools | Clone/download the public repository if permitted and available; or read repository files using web tools; or use an attached ZIP. Read the entry point and relevant supporting documents. Use built-in image, speech, workspace and process tools directly if actually available. Do not assume another agent has the same tools. |
| Local stdio MCP support plus Python | Optionally register `mcp/server.py` as documented in `mcp/README.md`. Use it to retrieve guides, scaffold a new project and perform basic timeline, SRT and metadata checks. Its tools do not render, synthesize speech, hear audio or review visuals. |
| Text-only agent | Read pasted instructions and produce a script, shot list, asset specifications, narration text and checklist. Clearly mark finished audiovisual files as blocked unless media tools become available. |

If the package is not locally accessible, fetch the public GitHub repository, or individual raw files, using the host's supported tool. The primary entry point is `https://raw.githubusercontent.com/selther-core/animated-video-skill-mcp/main/.agents/skills/cinematic-narrative-video/SKILL.md`. Related paths beneath `.agents/skills/cinematic-narrative-video/` include `references/niche-adaptation.md`, `references/visual-reference.md`, `references/character-rig.md` and `references/voice-direction.md`. If the host cannot fetch files, ask for the package or the necessary text; do not pretend it has been read.

## 2. Capability audit before production

Silently check what the host actually exposes; don't ask the user to perform work the agent can do. Where permissions are required, request them according to the host's rules. Keep a brief internal record:

- **Access and writing:** Can the agent read the package, write files and make downloadable deliverables? Can it use a local command runner or an existing editing/animation application?
- **Research:** Does it have trustworthy/current web access where claims need it? If not, do not claim real-time verification.
- **Art:** Is native image generation available? If so, use it when useful. Otherwise can the agent programmatically draw SVG, Canvas, or other editable assets? Use original procedural artwork if it meets the requirements. If neither route is available, provide a detailed asset list and label media creation as blocked.
- **Voice:** Is native TTS available, and does it require selecting/registering a voice? Follow the host tool's actual requirements, synthesize and align audio when possible. If it is not available, provide TTS-ready text and flag voice generation as an unresolved blocker; do not describe a silent video as finished.
- **Animation/encoding:** Can the agent run a renderer and mux audio/video, or does the host provide a native video generation/editing tool? Check actual availability. Where permitted, use or install necessary local dependencies, or adapt to available media software; don't assume a particular binary exists. A browser preview or project file alone is not an MP4.
- **Review:** Can it visually inspect actual frames or the rendered video? Can it actually listen to the output? Technical probes cannot establish that it sounds good or looks right. Mark the relevant checks as incomplete if it cannot.
- **Delivery/publishing:** Can it deliver files via the current host? Upload or publish externally only with authorization and the required connected account. Do not imply publication was completed when only instructions were prepared.

## 3. Use the best available implementation

1. **Native media-capable agent:** use built-in TTS and image generation plus available video editing/rendering tools. Follow the model's own voice registration, selection and usage requirements; do not ask the user to find an outside service if you already have a capable tool.
2. **Coding agent with local tools:** build layered vector/raster art and an animation renderer or timeline in software actually available; synthesize speech through native TTS if available; use local encoding tools such as FFmpeg if present or install them when allowed. The example HTML is a visual demo, not an automated finished-video renderer. Run actual output through visual/audio checks.
3. **MCP-enabled agent:** use the optional server for its advertised tooling, but use other host tools to do the substantive creative work. A successful `validate_timeline` call means only that the checked timing constraints pass, not that the video exists or is high-quality.
4. **No render or voice capability:** deliver the strongest real partial package—script, timed storyboard, exact TTS text, asset briefs and build instructions—and state the missing capabilities. A suggested next step is not a claim that the user must obtain external help when the agent already has the necessary tools.

The execution path is chosen from capabilities, not from the agent's brand name. Do not overwrite global host configuration, install packages, use network services or create external repositories without the host's required consent. Keep existing user projects safe. The original reference video, audio, frames and temporary tools should be cleaned up only according to the current user's instructions; retain requested deliverables.

## 4. Delivery and quality checks

- The task asks for a real video, thumbnail, transcript/TTS text, captions, title/description, publishing instructions, and playlist recommendation. Produce these if possible; inspect the actual artifacts before claiming completion.
- Include a quality report describing factual checks, timing and duration, rights, audio/visual inspection actually performed, outstanding issues, and platform rules verified at the time. A metadata-only inspection is not a full playback review.
- Preserve the evidence boundary: source visuals were sampled from the first 3:57.9, four selected seconds were examined frame by frame, and its audio and remaining ~3 minutes were not reviewed. Voice profiles and proposed animation techniques are recommendations, not measured replicas.
- Never reuse the third-party reference frames as output assets or imply permission to redistribute them. Check rights separately if they are to be included in a publicly shared package.
