---
name: cinematic-narrative-video
description: Plan, create, animate, render and review original code-drawn narrative videos, explainers, tutorials, ads, commentary and stories for any niche. Use the detailed references selectively for the actual brief.
---

# Cinematic narrative video

Create an **animated film in the production style of the project-authored WWII cut** by default: original code-drawn layered environments, the cut's distinctive long-body figures when people appear, expressive acting, moving props and subjects, cinematic lighting, motivated camera and cutaways. It must not be a slideshow. Read `references/animation-blueprint.md` and use the actual silent visual source `examples/ww2-seekable-scene.html` as the working technical benchmark. Recreate its *type of animation*, not its war story, narration, scenery, costumes or props. Match the user's **topic, niche, audience and requested format**; character-free and voice-free projects are possible: animate relevant nonhuman subjects when characters are not needed, and omit speech only when requested. If the user explicitly requests a different style, follow that instead. The example does not guarantee equivalent quality; inspect and revise the actual output.

## 1. Install separately; then understand and ask

If the task is only to install, set up the skill and optional MCP where permitted, verify discovery as possible and **stop**. Do not request a topic or create a video during setup. Once the user supplies a creative prompt, understand it and ask one concise grouped round about:

1. **Backgrounds:** preferred settings, visual mood and inclusions/exclusions.
2. **Length:** target duration or range, and intended platform/aspect ratio if relevant.
3. **Video type:** story, tutorial, explainer, documentary-style, commentary, ad or other; tone and format.
4. **Niche and audience:** topic category, viewer, knowledge level and goal.
5. **Voice:** narrator/characters or none; preferred gender presentation, energy and delivery. Every spoken voice uses an American accent; English defaults to `en-US`.

Acknowledge details already supplied instead of asking the user to repeat them. Offer “choose for me”; suggest choices suited to the actual prompt. If all choices are explicit, briefly confirm with an easy correction/proceed option rather than re-asking. If the user says not to ask, proceed using known details and state key assumptions. After the answers, resolve the brief and **begin**, without another general approval; follow up only for a material blocker or required permissions. Preserve a previously selected voice unless changed. For wording and edge cases, read `references/intake.md`.

## 2. Match the method to the niche

Read `references/animation-blueprint.md`, `references/niche-adaptation.md` and `references/scene-wardrobe.md` for practical selection. Derive the video's promise, desired viewer change, central subject/goal, format and emotional tone from the brief. Choose a story structure because it suits that purpose: an explanation can reveal an answer, a tutorial demonstrates steps, an ad communicates a truthful benefit, fiction follows choices and consequences, and commentary supports a view. These are options, not a fixed formula. For a new or hybrid niche, extract its subject-specific actions, environment, people/objects, evidence needs and audience expectations; adapt instead of falling back to an unrelated example.

- Break the script into meaningful beats. For each, identify what must be understood, the change/action, visual candidates, location and props, narration cue and any required evidence. Pick scenes for relevance, clarity, continuity, user preferences, feasible motion and accuracy; cut filler. Build only as many sets and shots as the story needs.
- Choose clothing only for characters who appear. Match role, culture, place, weather, era and action, while retaining identity, accessible contrast, prop attachments and continuity. Research factual designs or label uncertain stylization; avoid invented insignia and stereotypes. Animals need appropriate species/body mechanics, not a repurposed human puppet. If no characters appear, plan visual subjects and props instead—no character or costume is required. Use `examples/scene-wardrobe-template.md` when helpful.
- Factual video: use credible, current, topic-appropriate sources; track claims, dates, quotes, uncertainty and media rights. Check jurisdiction/current versions for finance, health, legal or software; don't invent evidence or give unsupported guarantees. Fiction: label illustrative composites where confusion is likely. Respect sensitive topics and audience age; no invented real-person statements.

## 3. Build the production

1. **Script and board.** Draft a niche-appropriate script, timed beat/shot list and audio plan. Map each important beat to a visible before/action/after or an intentional hold, with a readable payoff. Include structure and continuity notes; `references/story-structure.md` and `examples/story-beat-template.json` can help. Scale planning and scene count to duration and complexity.
2. **Original code-drawn art.** Build editable multi-layered animated scenes using the actual WWII visual source as a technical guide. Do not use image-generation models. Author backgrounds, props, diagrams, characters, lighting and thumbnails using SVG, CSS, Canvas, 3D or comparable editable code/tools. Set a topic-specific art direction, not a compulsory palette. Use layered foreground/midground/background, readable contrast and a motivated light source. Compose shots that serve the narrative and avoid covering faces or text. Refer to `references/code-animation.md` and `references/cinematic-staging.md`.
3. **Animation and camera.** Use deterministic time-based animation so a frame at `t` can be reproduced. Animate purposeful changes: action, prop interaction, expression or environmental movement where appropriate. Natural idles can support an active scene; a quiet hold can be intentional. Ease camera pushes/pans and transitions; motivate spotlights and shakes. Check borders, continuity and readability. For characters, build reusable jointed parts with stable pivots, weight/contact and appropriate anatomy; apply the long-body back-arm/torso/front-arm structure in `references/character-rig.md` for human figures by default, retaining the reference proportions and layering unless the user requests a different design. Do not turn animals or vehicles into humans.
4. **Voice and sound.** If narration/dialogue is wanted, use available native TTS with American-accent speakers, clear expressive delivery and energy appropriate to the subject—not shouting, clipping or a flat monotone. Preserve a chosen voice; follow the tool's actual registration/audition requirements. Measure generated speech and align shots to it. Use original or properly licensed sound and music; mix speech clearly and avoid clipping. Check actual listening when possible. For non-English speech, verify an American-accent option is supported; if unavailable, disclose it and supply a script rather than silently changing accents. A silent video needs no TTS. See `references/voice-direction.md`.
5. **Test and render.** A sequence of static illustrations or title cards is not an animated film, even with zooms, crossfades, captions, blinking, rain or particles. Plan meaningful subject and prop action within scenes, including changing poses and visible causes and results. Before scaling, make and inspect a proportionate representative style test of actual motion, framing and sound where possible; a very short or silent project may need a brief or silent test rather than a 15–30-second voiced one. Reject a style test that only pans/zooms static art, then fix it before full rendering. The optional `examples/render_seekable.py` renders authored `window.seek(t)` HTML; it creates no animation or voice itself. Generate a seekable timeline with actual timings; handle shot boundaries, final frame, audio duration and captions. Encode using available tools and user-selected aspect, duration and platform. Avoid unjustified installs or cloud services; if a capability is unavailable, give a useful, clearly labeled partial rather than claiming a finished video.
6. **Inspect and fix.** Sample the encoded output across the opening, middle, ending, transitions and key actions; note timestamps and the actual subject/prop movement inside each action scene. Fail and revise slideshow-style results; check full decode/metadata. Review real playback and listen to the final mix when capabilities allow. Check visual causality, anatomy/contact, motion, lighting, captions, titles, legibility, cuts, factual support, rights and accessibility. Sampled frames and metadata do not prove full-speed motion, audio quality or sync. Mark unperformed checks unknown, fix failures when feasible, and never fabricate approval or quality.

For detailed motion math, timeline schema, commands, audio targets, reference-analysis procedure, thumbnail design, publishing and full QA, load `references/production-manual.md` as needed. Defaults there are suggestions, not one-size-fits-all rules.

## 4. Deliver honestly

Provide the requested finished video when capabilities allow. Include subtitles, sources/credits, editable project assets, thumbnail, script, publishing copy or related items when requested or appropriate to the intended platform; do not publish without authorization. Report format/duration, major choices and checks actually performed; name remaining limitations and any blockers. Use current destination/platform rules instead of claiming automatic compliance. Retain only assets requested or needed, and follow cleanup/rights instructions. No voice/audio recordings are bundled with this skill.

## 5. Progressive reference map

Load only what's relevant; the core above is the starting point, not a demand to read every file on every job. Preserve useful detailed guidance rather than duplicating it in every prompt.

| Need | Read |
|---|---|
| Prompt-first questions | `references/intake.md` |
| Any niche, including unfamiliar/hybrid topics | `references/niche-adaptation.md`, `examples/cross-niche-scripts.md` |
| Story, scene, clothing | `references/story-structure.md`, `references/scene-wardrobe.md`, `examples/scene-wardrobe-template.md` |
| Actual WWII-style animation and anti-slideshow gate | `references/animation-blueprint.md`, `examples/ww2-seekable-scene.html`, `examples/render_seekable.py` |
| Visual style and animation | `references/code-animation.md`, `references/cinematic-staging.md`; `references/character-rig.md` for characters |
| Voice, scripts and sound | `references/voice-direction.md` |
| Full technical production, QA and publishing | `references/production-manual.md` |
| Host capabilities and fallbacks | `references/agent-compatibility.md` |
| Project-authored WWII example only | `references/visual-reference.md`, `references/ww2-example-breakdown.md`, `reference-frames/`, `examples/ww2-seekable-scene.html` (silent and editable) |
| Other editable visual examples | `examples/staging-rig-demo.html`, `examples/progressive-scene-demo.html`, `assets/README.md` |
| Retained feedback and lessons | `references/production-learning-notes.md` — update after significant user feedback or verified lessons |

The optional repository-root `mcp/` exposes selected guides, an intake-aware project scaffold, basic plan/timing checks, SRT generation and optional ffprobe metadata. It is **not** interactive, a renderer, TTS, media reviewer or quality guarantee; the host agent asks questions and does the production work. Skill-aware agents load the skill directory; other agents can read these files as ordinary instructions. See `references/agent-compatibility.md` and `mcp/README.md`.
