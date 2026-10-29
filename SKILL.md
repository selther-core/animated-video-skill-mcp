---
name: cinematic-narrative-video
summary: Create original narrative-driven animated videos and thumbnails across niches using expressive minimalist characters, staged visual metaphors, and cinematic lighting.
description: Use for animated storytelling, explainers, tutorials, commentary, and fictional narratives in any niche, inspired by the reference visual language. Includes cross-niche adaptation, original assets, production, TTS, sound, review, and publishing.
---

# Cinematic narrative video — cross-niche agent skill

## Package map: read the examples as needed

All paths are relative to this file. `assets/` and `examples/` contain original demonstrations. `reference-frames/` contains labeled stills extracted from the user-supplied reference excerpt; they are not original assets and may require permission or another lawful basis to redistribute. No reference audio is included.

- `mcp/README.md` and `mcp/server.py` — optional local MCP server, host setup and tool descriptions. MCP access is a supplement to this skill, not a replacement for the agent's actual rendering, image, speech and review capabilities.
- `tests/test_mcp.py` — stdio protocol and tool smoke tests.
- `references/agent-compatibility.md` — choose a workflow based on the host's real capabilities, whether or not it has skills or MCP.
- `references/visual-reference.md` and `reference-frames/README.md` — selected reference stills with timestamps, observational analysis, reconstruction notes and rights caveats. Only eight stills are included; the full video was not reviewed frame by frame.
- `references/niche-adaptation.md` — how to translate any niche, genre and topic into story beats, environments, figures, props, pacing, audio and evidence rules.
- `examples/cross-niche-scripts.md` — example briefs, original voice scripts and mini storyboards for several non-science niches.
- `references/character-rig.md` — coordinate system, hierarchy, joint placement, facial states and a usable pose data example.
- `references/voice-direction.md` — voice profiles, audition and TTS instructions, pacing, sound placement, and limitations. No voice files or reference-voice claims.
- `examples/example-script-and-board.md` — a complete short example narration, time-coded visual plan, TTS-ready lines and edit notes.
- `examples/example-timeline.json` — valid example scene/visual/audio event plan; a planning file, not an executable program.
- `examples/puppet-demo.html` — self-contained animated character/board demo. Open locally in a browser; it has no narration and is not a finished video.
- `assets/character-rig.svg` — annotated editable rig illustration and joint map.
- `assets/classroom-example.svg` — sample wide educational scene.
- `assets/thumbnail-example.svg` — sample original thumbnail composition.
- `assets/README.md` — what each image demonstrates and how to use or adapt it.

For production, first use this file to collect requirements. Read `references/niche-adaptation.md`, then select the most relevant script, rig, and voice references before generating assets; use examples as scaffolding, never as facts about the reference or as final assets without adaptation. The package's demonstrations are illustrative, not a finished rendering engine.

## 0. Evidence, limits and honesty

**Reference:** [Can 2 People Really Restart Humanity?](https://www.youtube.com/watch?v=6oZ9fdM0n50), Awaken, published 20 October 2026, listed duration 6:58. The user supplied a compressed excerpt, `New project.webm`, 3:57.92, 1920×1080, 30 fps, VP9 video and 48 kHz stereo Opus. It contains approximately the opening 3:58, not the ending. Its visuals were inspected using one image per second across the excerpt and four 30-frame, one-second sequences at 1.0, 40.5, 123.0 and 206.4 seconds. This is **sampling plus selected frame-by-frame inspection**, not every frame of the whole video or real-time viewing. The thumbnail, public description, chapters, and transcript were also inspected. The audio track exists, but this analysis had no capability to audition it; specific music, effects, voice characteristics, levels and exact audio/visual synchronization remain unverified. The last ~3 minutes were not visually inspected, so animals and later scenes cannot be described as observed. The actual production tools, rigs, typefaces, keyframe easing and render process are unknown. Distinguish observed evidence from implementation recommendations; do not claim an exact recreation.

**Observed thumbnail:** a wide 16:9 composition of a stylized empty city street, viewed obliquely from above; two worried, small figures stand below center in a warm amber pool of light, with elongated shadows. Each has a round near-black head and limbs, white oval eyes, small white brows and mouth, and simple clothed body; one wears light clothing, the other a yellow outer garment. Background buildings and pavement are cool purple-blue, with a warm shop interior, café furniture, planters, a streetlamp and foreground depth. Large off-white rounded uppercase words occupy much of the upper-left area; an amber numeral supplies emphasis. Soft bloom, edge lighting, atmospheric depth, and high contrast make the figures legible. Exact typeface and production technique are unknown; the excerpt has a predominantly flat, layered 2D appearance with soft shaded depth. **Do not duplicate the wording, characters, composition or visual assets exactly**; generate an original thumbnail appropriate to the topic.

**Observed narrative from chapters/transcript:** the opening asks the viewer to imagine a changed everyday situation; a brief character exchange punctuates narration. The story gives a large target, builds simple illustrative arithmetic, then pivots into a complication. It uses personal consequences, a historical example, biological mechanisms, an animal recovery story and counterexamples, then a qualified conclusion and audience question. The transcript contains music markers, but **does not reveal** musical style, exact sound effects, their timing, or mix. Page chapter times are coarse waypoints, not observed edit boundaries: 0:00 premise; 0:29 question; 0:38 math; 1:36 family growth; 1:59 genetics; 2:52 historical case; 3:17 generations; 4:05 aging; 4:20 black robin; 5:00 recoveries; 5:48 conclusion; 6:30 close.

**Content safety:** Create an original work, not a frame-for-frame or asset-for-asset copy. Use licensed or self-made media and fonts. Do not reuse the reference thumbnail, dialogue, music, or narrative wording. Cite factual sources in the final description. Imitating broad aesthetic traits is different from copying protected assets.

### 0A. Visual audit of the supplied 0:00–3:57.9 excerpt

Times below are approximately the sampled frame's time, not guaranteed cut boundaries. Observations concern the supplied compressed copy; the original may differ. The 1-fps sampling covers the whole supplied excerpt, and four 1-second sequences were examined at 30 fps. No visual evidence is available after 3:57.9. Audio and exact voice-to-picture sync were not auditioned.

| Approx. time | What the image shows | Reusable design mechanism |
|---|---|---|
| 0:01–0:04 | Side-on streetscape, small white-shirt figure walking past a door/café while holding a small object near face. Lit windows, planter, railing and café chairs. | Start with a contained side-view world and one easy-to-read subject; use contextual background details and a restrained walk. |
| 0:05–0:10 | Separate short close-ups of a traffic signal, ambulance, and a window with a small yellow object, against simplified backgrounds. | Insert literal visual illustrations of ideas before returning to the protagonist. These are discrete vignettes rather than a continuous roaming camera. |
| 0:11–0:29 | Back to street; small flying paper prop; then a much wider café façade with a second yellow-clad figure to the right. The scene holds a long time, with limited character action. | Establish geography by returning to a shared background, then widen to place characters apart. Do not assume every second requires a cut. |
| 0:30–0:38 | Question is staged across the storefront: narrow upper label, colorful letter-block word across the lower half, smaller lower question and handwritten accent; characters move among/behind blocks. | Make a title out of scene-integrated props; reveal components sequentially and preserve layers/occlusion. Do not reproduce the reference words or blocks verbatim. |
| 0:39–1:11 | Abrupt switch to warm wooden classroom with large green board, two tiny full-body figures to either side. Chalklike writing and simple pictograms accumulate. Big handwritten numbers, count of drawn children, small bottom pill and tiny source line; later an illustrated panel with a stamped qualifier. | Keep a consistent wide teaching stage for a long explanatory section; animate the board itself, replace its contents and add brief footnote/claim labels. |
| 1:12–1:36 | Writing, two-to-many family tree and counter accumulate; the camera reframes tighter on the board, then full-screen dark-board infographic/counter; returns to the wide classroom and highlights a generation. | Move from staged character explanation to close infographic and back. Build diagrams progressively in synchronization with the script, then highlight the conflict. |
| 1:37–1:45 | A warmly lit family room progresses through labeled years with crib, bunk bed and children; a brief exterior car vignette punctuates the domestic gag. | Reuse a locked-off environment across time jumps, swapping props, poses, ages and small year tags; insert visual comedic counterpoint. |
| 1:46–1:59 | Long dinner-table tableau with family members, then closer crop as the scene darkens. | Hold a single composition while reactions and framing change; use a deliberate tonal change before the next explanation. |
| 2:00–2:51 | Dark navy, subtle grid infographic stage: the white-shirt figure stands on the far left while centered headings, colored paired gene columns, stylized people icons, schematic comparison panels, check/cross and a highlighted outcome appear in order. | Keep a character anchor in negative space; change explanatory data in the larger area. Use a limited teal/lavender palette, fine borders, small high-contrast pill labels and restrained reveal timing. |
| 2:52–3:16 | Warm red-draped portrait gallery with gold-framed stylized historical figures, a walking foreground character, candle, date tab and small data labels; a portrait is emphasized in close view. | Translate historical examples into an identifiable theatrical setting with consistent character design, dates and brief labels. |
| 3:17–3:25 | Side-on village tableau with houses, fence, color-coded descendants, year label and a semi-transparent family-tree overlay. | Overlay an abstract relationship diagram above a concrete scene rather than cutting away immediately. |
| 3:26–3:35 | Isolated overhead baby-in-cradle icon in warm halo; numeric counter rises while small pale dots accumulate; a darker/red dot subsequently appears. | Animate a visual count then hold its destination, and use a contrasting accent to direct attention. |
| 3:36–3:43 | A centered red toolbox under pale light gradually fills with four tools; two tiny figures flank it and a short label appears. | Explain an abstract limit through a large, easily understood prop surrounded by generous negative space. |
| 3:44–3:57 | Village returns with colored figures and small warning/health icons; some characters/icons fade or alter before a short bottom text pill. | Return to an established visual metaphor to show a consequence; carry color coding and character placement across shots. |

### 0B. Motion evidence and reconstruction

- **Walk, 1.000–1.967 s at 30 fps:** sampled character progresses gradually to the right across a stationary side-view set, with alternating long narrow legs and a hand maintained close to the head for much of the action. The torso/head move far less than the legs; this reads as economical puppet-like animation. Exact contact, rigging and easing are not proven by this small sequence. Recreate with hip and leg pivots, opposite leg phase, short planted-foot intervals and slow root translation. Preserve the action's restrained scale, not an exaggerated bouncy cartoon walk.
- **Board writing, 40.500–41.467 s at 30 fps:** a yellow-clad figure traverses the board with one arm raised; the chalklike number develops sequentially as the hand moves, while the other figure remains mostly still at left. Recreate as a masked/stroked glyph path plus a parented hand or separate arm keyframes, coordinating the hand with the tip of the reveal; don't use a single instant text appearance. Evidence does not establish the original mask or software.
- **Gene stage, 123.000–123.967 s at 30 fps:** the graph and presenter hold largely steady for this full sampled second; a subtle change in facial pose is visible near the end. Recreate using a deliberate static hold with an occasional small blink or expression shift. Don't force continuous idle motion. The subsequent 1-fps samples show an additional colored column and later discrete labels/diagrams.
- **Counter, 206.400–207.367 s at 30 fps:** while the cradle composition remains locked, the corner counter rises from 3 to 54 and small bright marks accumulate. Recreate as an integer driven by an eased or monotonic curve and independently staggered particles; hold the final value once reached. Do not infer the original interpolation formula from these samples.
- **Shot rhythm:** the excerpt mixes a few short early cutaways with exceptionally sustained educational stages (the classroom at about 0:39–1:36 and dark infographic stage at about 2:00–2:51), changing board contents, crops and overlays rather than continuously changing locations. These times describe broad visual settings, not a shot-duration statistic.
- **Spatial grammar:** many shots are orthographic/front-facing or gently angled, not photorealistic perspectives. Figures are often tiny relative to a large set or diagram, grounded on an implied floor baseline and placed left/right to free the middle. One horizontal 16:9 frame alternates full-stage tableaux, full-screen diagrams and closer crops. The thumbnail is a more dramatic elevated street view; do not assume thumbnail camera is the film's normal camera.
- **Character/face:** the excerpt uses spherical near-black heads, bright simple white eyes and sparse expressive mouth/brow marks; bodies have colored/simple long tops and slender dark limbs. Keep scale and colors consistent per character; build editable face layers. The sampled frames do not prove 3D spheres, lip-sync method, hidden joints, or one specific software pipeline.
- **Typography and UI:** classroom handwriting is informal, slanted/chalklike; labels and counters use compact sans-serif lettering, frequently inside dark rounded outlined capsules; small citation lines can appear below; year/date tags resemble small pale cards. Integrate only necessary claims and use a readable mobile-size minimum, even if this differs from the very small reference citations. Exact fonts are not identified.
- **Lighting and surfaces:** visual world alternates cool navy streets/infographics and warm interiors: localized pools of light, softly shaded props, a subdued vignette, little flecks or grain, and color gradients. These are visual observations, not verified physical lights. Choose a consistent 2D composite with shadow and glow layers. Red theatre curtains/gold frames distinguish the history section; simple matte teal/purple graphics distinguish the science stage.
- **Transitions:** obvious changes between locations occur around 0:39, 1:37, 2:00, 2:52, 3:17, 3:26, 3:36 and 3:44 in 1-fps sampling. The samples support changed scenes, not the exact cut/dissolve shape or transition duration; inspect more closely before claiming those details.
- **Audio evidence boundary:** the file has a stereo 48 kHz Opus track. The published transcript indicates narration, occasional character lines and music markers. The track was not listened to, so its sound effects, music instrumentation, tempo, dialogue voice identities and detailed cue timings are **unknown**. The recommended mix and synthesis in §3D are design proposals, not reference analysis.
- **Animals and ending:** not included in the submitted excerpt. The public transcript mentions a black robin later, but there is no basis to describe its actual design or movement, nor the actual visuals of the ending. If the missing portion becomes available, extend this audit before representing it as a full-video style analysis.

### 0C. Scene implementation recipe inspired by the observed visual grammar

1. Divide the original script into meaning beats and select an appropriate location for each. Build a layered scene in normalized coordinates: background 0–1, floor at a shared y, characters each as independently movable rigs, prop/data layer, then captions/labels and lighting overlay. Give every asset a unique identifier and preserve z-order to enable characters to pass in front of or behind information.
2. For a teaching shot, make a reusable room with a large board occupying the central majority, two characters at the outer thirds, and a warm practical light. Render background once; draw a new board payload for each concept. Derive topic-specific diagram geometry, reveal strokes or icons in script order, then keep the completed state onscreen while the explanation resolves.
3. For an analytical or informational shot, consider switching to a dark flat field, subtly gridded; place a small character at the far left and use the remaining space for clear contrasting geometric diagrams. Each timed beat reveals or replaces one visual element and one concise label. Validate that color is not the only cue, and distinguish data examples from real measurements.
4. For a personal consequence, keep a consistent side-view room/street while swapping props, time-card text and character poses. Insert a short separate vignette for a joke or consequence, then return to the established set. Save layout states rather than repeatedly generating unrelated compositions.
5. For a data metaphor, construct one large simple prop or symbol center-frame. Animate its components, count or color change using deterministic keyframes. Compare the final value against the research notes and hold long enough for comprehension. Give the director/agent editable parameters for timing, position, count and colors.
6. Recreate the visual hierarchy as a family of original elements, not the original layouts, exact title phrase, data illustrations, characters or asset designs. Render an initial 15–30 second test before scaling to the full video; inspect scene geometry, face legibility, character continuity, diagram readability, audio alignment and export performance.

## 1. How to activate and use

- **Skill-aware agent:** place this file at `cinematic-narrative-video/SKILL.md` in the platform's documented skill directory, reload/discover skills if required, and invoke it by name or ask the agent to use it. Discovery paths and frontmatter requirements vary; consult the host's actual documentation rather than assuming installation succeeded.
- **Agent without skills:** attach or paste this entire file into the session as an instruction document, then supply the brief below. Agents with project-instruction files can instead add an explicit instruction to read the location of this file; do not overwrite unrelated project instructions.
- **Optional MCP server:** Configure the local stdio server in `mcp/README.md` if your agent supports MCP. It exposes guides, a project scaffold, basic timeline validation, SRT generation and optional ffprobe metadata. It does not generate or render media, synthesize voice, watch/listen, or guarantee policy compliance. An agent can use the skill without MCP.
- **Agent execution:** Audit the host's actual capabilities and choose the appropriate path in `references/agent-compatibility.md`. Use your own file, code, image, speech, rendering and media-inspection capabilities. Use an existing connected TTS/image tool directly when appropriate. Do not tell a user to obtain external assistance when the agent can perform the task itself. If an essential capability is genuinely unavailable, disclose it and deliver the strongest truthful partial result; never label a silent or unrendered project a finished video.

### Input brief

```
Use cinematic-narrative-video.
Topic: ...
Niche and target audience: ...
Core promise, question, lesson or story conflict: ...
Genre and intent: explanation / tutorial / story / case study / commentary / other
Length or range: ...       Format: long-form 16:9 / vertical Short / other
Language and voice: ...   Tone and boundaries: ...
Specific facts/sources: ...  Brand/style or accessibility needs: ...
Publishing destination: ...  Playlist context if known: ...
Other requirements: ...
```

If topic or target audience is missing and materially affects the result, ask a focused question. Otherwise assume an original, accessible 16:9 video of about 4–7 minutes, 30 fps, 1920×1080, MP4, selecting narration or dialogue as appropriate to the niche, and state assumptions. Do not assume 6:58 is a requirement. Avoid forcing a standard length onto a short or a user-specified duration.

### Required deliverables

1. `final_video.mp4`: finished picture and audio, unless a true capability blocker is stated.
2. `thumbnail.png` or `.jpg`, original and legible at small size.
3. `caption_and_publish.md`: title, description/caption, sources, appropriate hashtags, audience setting considerations, playlist recommendation with rationale, and tailored publishing steps. Do not assert upload or publication happened unless it did.
4. `narration_script.md`: exact spoken text and speaker labels; include TTS text if TTS is unavailable.
5. `quality_report.md`: checks performed, measurements, defects fixed, unresolved constraints, evidence of source licenses, and actual duration.
6. When possible keep editable source: `timeline.json`, scene files, generated art/audio and renderer. If the user requires cleanup, delete only temporary resources they specified, not unrelated files; do not delete deliverables.

## 2. Upgrade to an evidence-based reference analysis if the media is available

Obtain the source only through permitted means. Do not bypass authentication or bot checks. Prefer a user-provided file with permission; optionally attempt a normal `yt-dlp` download if the environment permits. If blocked, say so. Never invent observations.

1. Probe with `ffprobe -v error -show_streams -show_format -of json reference.mp4 > probe.json`. Record duration, actual fps/time base, resolution, audio channels and sample rate. Extract audio losslessly for listening, for example `ffmpeg -i reference.mp4 -vn -c:a pcm_s16le reference_audio.wav`. Review the actual track on headphones or with a listening tool; waveforms and speech recognition alone cannot establish what it sounds like.
2. View the **entire** video in order at normal speed with audio; make a first-pass narrative and audio log. Extract a coarse contact sheet at 1 fps and scene-change candidate frames, then inspect every transition and representative motion in context. For genuine frame-by-frame review, decode every frame, determine frame number `n` and `t=n/fps` (use presentation timestamps for variable frame rate), inspect successive frames at slowed playback/frame-step, and log every shot and significant pose. If resource limits mean only sampling, explicitly report sampling density; do not say frame-by-frame. Analysis should note hold length, in-betweens, reversals, pivot paths, occlusion, continuity, and when visual and audio cues meet. A fully automated agent may combine cuts/optical flow/audio detection with human-equivalent visual and aural inspection if available; algorithms alone are not an observation of subjective intent.
3. For every shot record: `start`, `end`, visual subject, composition/camera, background layers, light direction/color, movement, character positions, facial poses, transitions, text and timing, narration/dialogue, music/SFX, and confidence. Analyze 3–5 representative actions frame by frame: neutral → anticipation → action → overshoot → settle; document actual timings, interpolation, joint arcs and contact. Count holds and changes over a representative period; measure typical shot durations instead of guessing. Record examples of audio ducking and sync offsets.
4. Compare the actual thumbnail, first 30 seconds, middle, ending and full scene map. Identify repeated engagement mechanisms; separate observed facts from inferred causes and proposed changes. Record what you could not verify. Integrate timestamped evidence into the style rules below, without claiming identical reproduction unless demonstrably true.
5. If cleanup is requested, remove the source video, frames, extracted audio and temporary installations after the analysis is recorded. Inventory the work directory first. Do not remove tools or files that predated the job. A user-uploaded original outside the temporary work directory must not be deleted without clear permission.

## 3. Production architecture

Work in four passes: **story → boards and sound plan → asset and motion build → render and review**. Complete each with evidence, not generic checkboxes. This method is for **any niche**, not just science: preserve the reference-inspired visual grammar while replacing narrative structure, setting, people, animals, props, diagrams, voice direction, facts and pacing to fit the brief. The science example is illustrative only. See `references/niche-adaptation.md` and `examples/cross-niche-scripts.md` before planning.

### A. Research and script

- For factual work in any niche, research topic-specific claims using reliable primary or expert sources and capture the source, date, support, uncertainties and media rights. History and biography need provenance and context; business and finance need current figures and jurisdiction; tutorials need verified steps; health needs credible guidance and careful safety boundaries. For fiction, invent original material, mark it as fiction and verify only real-world claims used for grounding. Never transfer the reference's science claims or citations to a new topic without verification. Distinguish consensus from speculation and correlation from causation.
- Pick a narrative structure appropriate to the niche: an explanation may use question → intuitive answer → complication → evidence → conclusion; a tutorial may use goal → obstacle → steps → demonstration → recap; a fictional story may use character desire → obstacle → choices → consequences → resolution; a case study may use context → decisions → outcomes → lessons. Start with a concrete visual hook, make the stakes clear, and offer a satisfying payoff. Do not force a scientific problem, numbers, diagrams or a viewer question into unrelated content.
- Write natural spoken prose suited to the genre; for explanatory narration, 125–160 words/minute is a starting estimate, not a mandatory rate. Use actual TTS duration. Some stories work better as dialogue, guided action, character voiceover, comedy or little narration; choose the mix based on the brief, and do not undermine sensitive subjects with forced humor.
- Sustain attention with a relevant unresolved question, decision, emotional tension, progression or visual reveal; give the promised payoff before the ending. No unsupported clickbait. Never imply a thumbnail promise that the video does not address.
- Make a beat sheet. Set estimated time, purpose, narrative text, visual metaphor, on-screen text, planned change, SFX/music cue, and supporting source. Key changes should coincide with the word or idea they explain; avoid simultaneously introducing several new facts. Plan regular purposeful visual updates rather than a forced cut rate. Leave reading time proportional to text complexity.

### B. Boards, assets and original style

Create a palette and model sheet before rendering. These are practical design choices informed by the inspected thumbnail and excerpt; numerical values are proposed defaults, not measurements:

- World: desaturated midnight-indigo/violet environment with amber practical lights. Suggested palette: near-black `#101017`, cool shadow `#323652`, violet pavement `#655C79`, warm light `#FFBD61`, cream text `#F8F1DD`; adjust for contrast. Shapes simple and softly modeled; environmental details selective, not photo-busy. Establish one coherent world, then vary location and framing according to the story.
- Characters: simple round dark head, two light eyes and small editable brows/mouth; thin dark limbs, mitt-like hands, clean clothed torso and distinct silhouette. Make **new** people, clothes, hair, skin/head treatments and proportions; do not reuse the reference character designs as exact copies. Build a front/three-quarter/side model sheet, with neutral, puzzled, worried, surprised, relieved and speaking variants. Design accessible contrast and facial expression at thumbnail and mobile scale.
- Character construction: separate head, neck, torso/pelvis, upper/lower limbs, hands and feet as local-coordinate shapes with pivot points at neck, shoulders, elbows, hips, knees and ankles. Overlap joints to hide gaps; layer far arm/leg behind torso, near arm/leg in front. Keep torso attached to pelvis, head attached to neck; place all pivots from one rest-pose skeleton. Ensure no intersections or limb length changes except deliberate squash. Make mouth, eyes and brows independent layers parented to head. Use masks/occlusion for sleeves, pockets and hair.
- Background: foreground vignette, midground subject and readable background landmarks. Create streets, rooms, homes, labs, maps or landscapes using simple shape layers, muted cool fills and a few warm windows/practical lamps; draw depth from scale, overlap, perspective, soft shadow and atmospheric contrast. Keep key action against a quiet region. An individual scene need not repeat the reference street.
- Lighting: choose a consistent motivated light source. Use warm pooled radial gradients, restrained bloom, rim highlights on the light-facing side, and soft cool shadows with consistent direction. Fake 3D with gradients, layered silhouettes and blurred shadow ellipses, or use a 3D renderer if available. Avoid claiming physically accurate illumination if the scene uses 2D approximations.
- Animals and props: original simplified silhouettes and identifiable features; anatomical articulation appropriate to each species (bird body, head, wing and leg pivots, for instance). Create reusable prop layers—cards, diagrams, icons, counters or charts—designed to carry the actual explanation. Do not depict people as biologically representative without appropriate context.
- Text: for initial thumbnail treatment choose a licensed heavy rounded sans-serif (e.g. a locally available rounded bold typeface) or draw original lettering. Exact reference font is unknown. Use large bold high-contrast text, usually 2–5 words for thumbnail, and emphasize one important word or number in amber. Keep video labels short; avoid covering faces or information. Verify font license and glyph support. Readability outranks stylistic fidelity.

**Image generation if available:** Generate individual scene backgrounds or character components, not baked-in tiny lettering. Use transparent layers or remove backgrounds locally. Write prompts describing original figures, camera, shapes, palette and lighting; include consistent model-sheet identifiers. Anchor consistency with the same generated references if supported. Check that the resulting parts are separately controllable; for essential body animation, use editable vector rigs rather than expecting a still image to animate itself. If image generation is unavailable, draw vector shapes procedurally with SVG/Canvas or use local graphics software.

### C. Precise motion system (proposed defaults)

Animate in world coordinates with a deterministic timeline. At 30 fps, frame `n` is `t=n/30`; compute poses directly from `t`, not accumulated per-frame increments. Store a start pose, pose keyframes, easing and holds for each animated property. Suggested motion grammar, **not reference observations**:

1. Favor readable poses with short anticipation and settle over constant motion. Pose change: anticipate 3–5 frames, main movement 6–12 frames, overshoot 2–3, settle 4–8; vary according to intent and dialogue. Let emotional reactions breathe for several seconds if the line needs it.
2. Ease interpolation `s=3u²−2u³`, `u=clamp((t−t0)/(t1−t0),0,1)`. Linear translation only for deliberately mechanical motion. A useful pop-in starts at scale 0.85, rises to 1.04, then settles to 1.0; do not apply it to every element.
3. Compose 2D transforms as `parent_world × translate(pivot) × rotate(angle) × translate(-pivot)`; draw child parts in their parent coordinate space. Limb segments rotate about their joints, with elbow/knee positions calculated by parent transforms. Keep feet planted during holds; shift body mass before stepping; move foot along a short arc and land before weight settles. Ensure the ground contact does not slip. In a walk loop, opposing arms and legs swing with a phase offset; keep stride and root speed consistent. In a reaction, use small head tilt, blink, eyebrows and one hand gesture rather than animating all parts simultaneously.
4. Use mouth poses: closed / open / wide. If phoneme alignment is available, use it; otherwise derive coarse mouth-open events from narration amplitude, manually correct important beats, and close during silence. This is approximate, not genuine lip-sync. Use distinct voices for true dialogue when supported, but do not clone the reference narrator. Animate tiny eye/brow changes at meaningful beats; no rapid blinking loops.
5. Use camera reframing to signal a new thought: hold a readable wide, gently push 2–6% across several seconds, then cut to a detail or analogy; restore the geography after a diagram. Use background/foreground parallax sparingly. Transition by clean cut, motivated pan, dissolve or shape wipe only when it helps continuity. Never use random motion to manufacture engagement.
6. Put diagrams/labels into screen-safe areas (at least ~5% inset as an initial target), reveal in semantic order, and retain long enough to read. Numbers should count only when useful; reconcile their final values with the script. No flashing or rapid high-contrast patterns.

### D. Sound and timing (proposed, not observed)

- Generate the final narration first if possible; use agent-native TTS. Save exact transcript and time cues. After receiving audio, measure duration and align scene lengths to actual speech, not estimated word counts. Keep dialogue distinct and intelligible. If no TTS capability exists, produce exact TTS-ready text and a clearly marked temporary silent/picture-only preview only if useful; request audio input only as the remaining blocker, not generic outside assistance.
- Design a small original palette: soft tonal ambient bed, room/street atmosphere where relevant, quiet UI pops or swishes for information reveals, gentle footsteps, and a restrained accent on genuine surprises. Generate procedural SFX with synthesis/noise envelopes or use properly licensed assets; do not assume any of these are present in the reference. No unnecessary stingers on every cut. Keep the opening clear and avoid a loud logo sting.
- Lay narration, music and SFX on separate tracks. Sync pops to on-screen arrival; place breaths/pauses naturally; duck music and effects under speech. A practical initial target for online video is integrated loudness near −16 LUFS stereo, true peak at or below −1 dBTP, with narration clearly dominant; this is a production target, not a platform requirement. Measure with `ffmpeg -i final_video.mp4 -af loudnorm=I=-16:TP=-1:LRA=11:print_format=json -f null -`; inspect levels and listen after adjustment. Avoid clipping and overcompression. Loudness target is not a substitute for intelligibility or final listening.
- If only procedural audio is available, synthesize short envelope-shaped sound waves and layer at low level; use original sound or silence rather than unlicensed music. Captions should include important non-speech information where relevant.

## 4. Implement and render

### Timeline contract

Save machine-readable `timeline.json`. All times in seconds, continuous from 0. `shots` must have start/end, description, camera and visual layers; `audio_cues` and `captions` must have timed entries. Include `assets` with relative paths and rights. Example schema fragment (replace with real brief-specific content):

```json
{
  "fps": 30, "width": 1920, "height": 1080,
  "audio_sample_rate": 48000, "duration": 12.0,
  "shots": [
    {"id":"s01","start":0.0,"end":5.0,"purpose":"Establish the question",
     "camera":{"from":[0,0,1],"to":[0,-8,1.03],"ease":"smoothstep"},
     "layers":[{"asset":"bg.svg","z":0},{"asset":"character.svg","z":1,"x":960,"y":700}]},
    {"id":"s02","start":5.0,"end":12.0,"purpose":"Reveal the first constraint",
     "camera":{"from":[0,0,1],"to":[0,0,1],"ease":"smoothstep"},"layers":[]}
  ],
  "audio_cues":[{"start":0.0,"end":12.0,"asset":"narration.wav","role":"voice"}],
  "captions":[{"start":0.5,"end":3.0,"text":"Replace with the actual spoken line."}],
  "assets":[{"path":"bg.svg","rights":"original"}]
}
```

This is a planning contract, **not a supplied renderer or CLI**. The agent must implement or adapt the renderer to match it. Validate no gaps or unintended overlaps in shot coverage, asset references resolve, frames after `duration` are not rendered, and audio never ends early. Offset sounds using cue times in an audio editor or FFmpeg filter graph. For 30 fps and duration `D`, target `ceil(D*30)` frames indexed 000000 onward. Derive captions from the final audio and correct names, punctuation and timing.

### Rendering choices

Use available native capabilities. A viable self-contained route: create SVG shapes and rigs; render frames through a local browser Canvas/SVG renderer (or Python rasterization library); generate speech through connected TTS; synthesize simple SFX; mix and encode with FFmpeg. Alternatively use an existing animation/NLE/3D environment. Check tool availability and licenses first; install dependencies only if permitted and needed. Keep installs within a project-local temporary directory if cleanup was requested. Do not require a user to manually animate.

Example encode for **already rendered frames and already mixed** 48 kHz audio (`N` frames define exact duration; mix audio to match):

```sh
ffmpeg -framerate 30 -start_number 0 -i frames/%06d.png -i mix.wav \
  -map 0:v:0 -map 1:a:0 -c:v libx264 -pix_fmt yuv420p -crf 18 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart final_video.mp4
ffprobe -v error -show_entries format=duration,size:stream=codec_name,codec_type,width,height,avg_frame_rate,sample_rate -of json final_video.mp4
```

Choose a supported codec if x264 is unavailable. Avoid using `-shortest` to hide mismatched tracks; explicitly trim or pad audio and verify the intended end. Check frame sequence completeness and no duplicate-frame artifacts unintended by design. Add an independently timed SRT or WebVTT sidecar; upload it or use reliable platform captioning. If burned captions are requested, encode them with sufficient contrast and safe margins.

## 5. Thumbnail procedure

Start from the actual story, promise, conflict or question, not a generic template. Design a new 16:9 still with one unmistakable conflict, one or two original figures or symbols, a simple environment and an area reserved for very large, short wording. Reference-informed starting ingredients: cool moody atmosphere, warm focal light, readable rounded bold type, facial expression and a contrasting key numeral/word. Change the scene, poses, wording, character identities and graphical layout to suit the topic; avoid simply recreating the reference. Export a high-quality 1280×720 or larger JPEG/PNG, and use a conservative `<2 MB` for portable long-form upload; check current YouTube requirements because they vary by interface and can change. Test at ~200 px wide, including in grayscale: hierarchy, face, contrast, and message must survive. Do not imply an outcome or fact the video does not support. Maintain source artwork with text as editable layers.

## 6. Quality gate: inspect, fix, then report

Review a full final playback with audio if tools allow; examine opening, each transition, captions, final card and a contact sheet. Do not claim a subjective listening/viewing check that was not performed. Record specific timestamps for defects, fix, rerender and recheck. Requirements are goals, not a guarantee of viewer retention.

**Story & engagement**
- [ ] Topic and audience are clear; immediate premise and stakes appear early, without unnecessary branding.
- [ ] The central promise is paid off: answer the question, complete the tutorial, resolve the narrative arc, or provide the intended takeaways. Any complication, twist or reversal is meaningful rather than forced.
- [ ] Scenes, visual metaphors and changes in scale serve the chosen niche and audience; factual examples are accurate and fictional examples are clearly framed.
- [ ] Scene pacing changes when the information or emotional beat changes. Remove filler or overlong static holds; allow time for complex ideas and jokes.
- [ ] Ending supplies the appropriate resolution, recap or qualified conclusion. Include a relevant, non-manipulative question only when it fits. Thumbnail and title match the content.

**Visual craft & accessibility**
- [ ] Characters are consistent across shots; pivots are connected; hands and feet avoid accidental sliding, discontinuity, collisions and frame-edge clipping. Expressions are readable at small size.
- [ ] Lighting, shadows, perspective and color support scene geography; text and diagrams stay clear of faces and within a safe region. Show each label long enough to read.
- [ ] Cuts and transitions preserve continuity. No broken assets, accidental black frames, awkward unmotivated motion or illegible frames. Avoid distracting flashes.
- [ ] Verify thumbnail at full and small scale and validate font/image rights.

**Sound & factual quality**
- [ ] Voice is understandable throughout, words and cues line up, music/SFX do not mask speech, and peaks do not clip. Listen at a moderate level and, if possible, on small speakers/headphones.
- [ ] All factual claims have appropriate credible sources; uncertain claims are qualified. Numbers and diagrams agree with narration. Disclose significant limitations.
- [ ] Caption file matches final speech and sound cues; legibility and sync checked.

**Technical & policy**
- [ ] `ffprobe` confirms video/audio streams, dimensions, codec and actual duration; compare to the brief and report any mismatch. Check the full output decodes; a useful check is `ffmpeg -v error -i final_video.mp4 -f null -`.
- [ ] Verify all rights for voice, music, graphics and fonts. Avoid misleading metadata, prohibited content, and inappropriate audience settings. If realistic altered/synthetic content requires disclosure, apply the appropriate YouTube setting; check current policy. No automated checklist can guarantee upload approval or monetization.
- [ ] Check the current YouTube help pages for upload limits, Shorts classification, thumbnail format and disclosure rules. Confirm features applicable to the destination/account. Never assert an account is verified or the video is compliant based only on its length.

If actual listening or visual playback is impossible, label the missing checks explicitly; deliver as a draft, not a passed final. If a checklist item fails, revise and rerender; if it cannot be fixed, identify the blocker, deliver what is genuinely complete, and never manufacture a passing report.

## 7. Publishing package and current-policy checks

Draft a concise title (YouTube's title limit is currently 100 characters; confirm if needed), one-sentence summary, informative description, source URLs, 1–3 relevant hashtags if useful, and chapters if suitable. Add a playlist **only if** an existing or proposed playlist genuinely matches the topic and audience; otherwise recommend no playlist. If the channel's playlists are unknown, phrase as conditional rather than claiming one exists.

YouTube Studio workflow: upload → title/description → custom thumbnail where eligible → audience selection based on actual intended audience, not desired monetization → relevant playlist if appropriate → subtitles → check copyright and content/policy notices → set visibility/schedule → review and publish. Do not publish without authorization. For long-form, unverified accounts generally have a 15-minute default upload limit; verification enables longer uploads. Long-form custom thumbnails have feature eligibility requirements. Square/vertical uploads up to three minutes can qualify as Shorts; Shorts thumbnail options differ by interface and policy may change. Maximum upload size and other limits must be verified at upload time. Avoid promising monetization, absence of Content ID claims, or automatic approval. Refer to:

- Upload length: https://support.google.com/youtube/answer/71673
- Thumbnails: https://support.google.com/youtube/answer/72431
- Shorts upload: https://support.google.com/youtube/answer/12779649
- Community Guidelines: https://www.youtube.com/howyoutubeworks/policies/community-guidelines/
- Altered/synthetic content: https://support.google.com/youtube/answer/14328491
- Copyright basics: https://support.google.com/youtube/answer/2797466

## 8. Completion response

List actual downloadable files, their duration and format, brief sources/rights note, and exactly which reviews were or were not possible. If a requested reference was unavailable, say the result is based on accessible evidence, not frame-by-frame analysis, and request the source file if the user wants a verified style audit. Never claim an output exists without verifying it on disk.
