# Detailed production manual

This is the deep, optional reference for research, timeline, rendering, audio, thumbnails, QA and publishing. `../SKILL.md` is the compact authoritative entry point: follow its prompt-first flow, user constraints and niche-specific choices. Examples, numeric targets, platform workflows, palettes, character proportions and requested deliverables below are **options**, not universal defaults. Use only sections relevant to this project. Paths such as `references/...` and `examples/...` below are relative to the skill root, not this file. A silent or character-free project needs neither voice nor a character rig. The WWII cut is the default animation-type benchmark; never carry its specific story, uniform or battlefield into another niche unless requested. Follow `animation-blueprint.md` and reject static slide-style output.

## 2. Upgrade to an evidence-based reference analysis if the media is available

Obtain the source only through permitted means. Do not bypass authentication or bot checks. Prefer a user-provided file with permission; optionally attempt a normal `yt-dlp` download if the environment permits. If blocked, say so. Never invent observations.

1. Probe with `ffprobe -v error -show_streams -show_format -of json reference.mp4 > probe.json`. Record duration, actual fps/time base, resolution, audio channels and sample rate. Extract audio losslessly for listening, for example `ffmpeg -i reference.mp4 -vn -c:a pcm_s16le reference_audio.wav`. Review the actual track on headphones or with a listening tool; waveforms and speech recognition alone cannot establish what it sounds like.
2. View the **entire** video in order at normal speed with audio; make a first-pass narrative and audio log. Extract a coarse contact sheet at 1 fps and scene-change candidate frames, then inspect every transition and representative motion in context. For genuine frame-by-frame review, decode every frame, determine frame number `n` and `t=n/fps` (use presentation timestamps for variable frame rate), inspect successive frames at slowed playback/frame-step, and log every shot and significant pose. If resource limits mean only sampling, explicitly report sampling density; do not say frame-by-frame. Analysis should note hold length, in-betweens, reversals, pivot paths, occlusion, continuity, and when visual and audio cues meet. A fully automated agent may combine cuts/optical flow/audio detection with human-equivalent visual and aural inspection if available; algorithms alone are not an observation of subjective intent.
3. For every shot record: `start`, `end`, visual subject, composition/camera, background layers, light direction/color, movement, character positions, facial poses, transitions, text and timing, narration/dialogue, music/SFX, and confidence. Analyze 3–5 representative actions frame by frame: neutral → anticipation → action → overshoot → settle; document actual timings, interpolation, joint arcs and contact. Count holds and changes over a representative period; measure typical shot durations instead of guessing. Record examples of audio ducking and sync offsets.
4. Compare the actual thumbnail, first 30 seconds, middle, ending and full scene map. Identify repeated engagement mechanisms; separate observed facts from inferred causes and proposed changes. Record what you could not verify. Integrate timestamped evidence into the style rules below, without claiming identical reproduction unless demonstrably true.
5. If cleanup is requested, remove the source video, frames, extracted audio and temporary installations after the analysis is recorded. Inventory the work directory first. Do not remove tools or files that predated the job. A user-uploaded original outside the temporary work directory must not be deleted without clear permission.

## 3. Production architecture

### Reference-informed structural gate

Before making scenes, use `references/story-structure.md` and `examples/story-beat-template.json` to connect the user's promise to a genre-appropriate sequence. For each major beat write the viewer change, before/action/after/hold, meaningful timed visual events, character/prop intent, speech cue and supporting source or fiction label. Where an idea or action develops, show the change within a coherent held location; maintain prior states long enough to understand the next. Include a purposeful wide/insert/return when useful, not obligatory rapid cuts or fake motion. Quiet holds and story-led narratives are valid; do not force classrooms, charts or a formula on unrelated topics. The included silent progressive example demonstrates editable timing and states; it is not a finished video.

The WWII example illustrates cast, varied sets, map and atmosphere; some scenes can benefit from more developed action and interaction. See the current example breakdown. The user's new work should not be labeled reference-matched based on similar silhouettes or a completed encode. Record pass/partial/fail/unknown with timestamps and evidence; visual samples cannot prove full-speed motion, sound or sync. Resolve material failures before delivery and report unknowns.


Work in four passes: **story → boards and sound plan → asset and motion build → render and review**. Complete each with evidence, not generic checkboxes. This method is for **any niche**, not just science: preserve the example-informed visual grammar while replacing narrative structure, setting, people, animals, props, diagrams, voice direction, facts and pacing to fit the brief. The science example is illustrative only. See `references/niche-adaptation.md` and `examples/cross-niche-scripts.md` before planning.

### A. Research and script

- For factual work in any niche, research topic-specific claims using reliable primary or expert sources and capture the source, date, support, uncertainties and media rights. History and biography need provenance and context; business and finance need current figures and jurisdiction; tutorials need verified steps; health needs credible guidance and careful safety boundaries. For fiction, invent original material, mark it as fiction and verify only real-world claims used for grounding. Never transfer a sample film’s factual claims or citations to a new topic without verification. Distinguish consensus from speculation and correlation from causation.
- Pick a narrative structure appropriate to the niche: an explanation may use question → intuitive answer → complication → evidence → conclusion; a tutorial may use goal → obstacle → steps → demonstration → recap; a fictional story may use character desire → obstacle → choices → consequences → resolution; a case study may use context → decisions → outcomes → lessons. Start with a concrete visual hook, make the stakes clear, and offer a satisfying payoff. Do not force a scientific problem, numbers, diagrams or a viewer question into unrelated content.
- Write natural spoken prose suited to the genre; for explanatory narration, 125–160 words/minute is a starting estimate, not a mandatory rate. Use actual TTS duration. Some stories work better as dialogue, guided action, character voiceover, comedy or little narration; choose the mix based on the brief, and do not undermine sensitive subjects with forced humor.
- Sustain attention with a relevant unresolved question, decision, emotional tension, progression or visual reveal; give the promised payoff before the ending. No unsupported clickbait. Never imply a thumbnail promise that the video does not address.
- Make a beat sheet. Set estimated time, purpose, narrative text, visual metaphor, on-screen text, planned change, SFX/music cue, and supporting source. Key changes should coincide with the word or idea they explain; avoid simultaneously introducing several new facts. Plan regular purposeful visual updates rather than a forced cut rate. Leave reading time proportional to text complexity.

### B. Boards, assets and original style

Create a palette and model sheet before rendering. These are flexible design choices for a project; numerical values are proposed defaults, not measurements:

- World: desaturated midnight-indigo/violet environment with amber practical lights. Suggested palette: near-black `#101017`, cool shadow `#323652`, violet pavement `#655C79`, warm light `#FFBD61`, cream text `#F8F1DD`; adjust for contrast. Shapes simple and softly modeled; environmental details selective, not photo-busy. Establish one coherent world, then vary location and framing according to the story.
- Characters: simple round dark head, two light eyes and small editable brows/mouth; thin dark limbs, mitt-like hands, clean clothed torso and distinct silhouette. Create original artwork and treatments; follow the user-specified character proportions and depth order when requested, without claiming an exact copy or using reference assets. Build a front/three-quarter/side model sheet, with neutral, puzzled, worried, surprised, relieved and speaking variants. Design accessible contrast and facial expression at thumbnail and mobile scale.
- Character construction: separate head, neck, torso/pelvis, upper/lower limbs, hands and feet as local-coordinate shapes with pivot points at neck, shoulders, elbows, hips, knees and ankles. Overlap joints to hide gaps; layer far arm/leg behind torso, near arm/leg in front. Keep torso attached to pelvis, head attached to neck; place all pivots from one rest-pose skeleton. Ensure no intersections or limb length changes except deliberate squash. Make mouth, eyes and brows independent layers parented to head. Use masks/occlusion for sleeves, pockets and hair.
- Background: foreground vignette, midground subject and readable background landmarks. Create streets, rooms, homes, labs, maps or landscapes using simple shape layers, muted cool fills and a few warm windows/practical lamps; draw depth from scale, overlap, perspective, soft shadow and atmospheric contrast. Keep key action against a quiet region. Select the location for the current story.
- Lighting: choose a consistent motivated light source. Use warm pooled radial gradients, restrained bloom, rim highlights on the light-facing side, and soft cool shadows with consistent direction. Fake 3D with gradients, layered silhouettes and blurred shadow ellipses, or use a 3D renderer if available. Avoid claiming physically accurate illumination if the scene uses 2D approximations.
- Animals and props: original simplified silhouettes and identifiable features; anatomical articulation appropriate to each species (bird body, head, wing and leg pivots, for instance). Create reusable prop layers—cards, diagrams, icons, counters or charts—designed to carry the actual explanation. Do not depict people as biologically representative without appropriate context.
- Text: for initial thumbnail treatment choose a licensed heavy rounded sans-serif (e.g. a locally available rounded bold typeface) or draw original lettering. Exact reference font is unknown. Use large bold high-contrast text, usually 2–5 words for thumbnail, and emphasize one important word or number in amber. Keep video labels short; avoid covering faces or information. Verify font license and glyph support. Readability outranks stylistic fidelity.

**Code-drawn production:** Author scene layers, characters, text, diagrams, props and thumbnails as editable SVG/CSS/Canvas or equivalent code. Use reusable parts with named local pivots, parameterized color/light and a deterministic timeline. Rasterize the authored scene only for preview/export. Do not use image-generation models, generated backgrounds, still-image sequences or text overlays as a substitute for character/prop animation. See `references/code-animation.md`, `examples/staging-rig-demo.html`, and `examples/progressive-scene-demo.html`; the older backyard prototype is not the quality benchmark.

### C. Precise motion system (proposed defaults)

Animate in world coordinates with a deterministic timeline. At 30 fps, frame `n` is `t=n/30`; compute poses directly from `t`, not accumulated per-frame increments. Store a start pose, pose keyframes, easing and holds for each animated property. Suggested motion grammar, **not reference observations**:

1. Favor readable poses with short anticipation and settle over constant motion. Pose change: anticipate 3–5 frames, main movement 6–12 frames, overshoot 2–3, settle 4–8; vary according to intent and dialogue. Let emotional reactions breathe for several seconds if the line needs it.
2. Ease interpolation `s=3u²−2u³`, `u=clamp((t−t0)/(t1−t0),0,1)`. Linear translation only for deliberately mechanical motion. A useful pop-in starts at scale 0.85, rises to 1.04, then settles to 1.0; do not apply it to every element.
3. Compose 2D transforms as `parent_world × translate(pivot) × rotate(angle) × translate(-pivot)`; draw child parts in their parent coordinate space. Limb segments rotate about their joints, with elbow/knee positions calculated by parent transforms. Keep feet planted during holds; shift body mass before stepping; move foot along a short arc and land before weight settles. Ensure the ground contact does not slip. In a walk loop, opposing arms and legs swing with a phase offset; keep stride and root speed consistent. In a reaction, use small head tilt, blink, eyebrows and one hand gesture rather than animating all parts simultaneously.
4. Use mouth poses: closed / open / wide. If phoneme alignment is available, use it; otherwise derive coarse mouth-open events from narration amplitude, manually correct important beats, and close during silence. This is approximate, not genuine lip-sync. Use distinct voices for true dialogue when supported, but do not clone the reference narrator. Animate tiny eye/brow changes at meaningful beats; no rapid blinking loops.
5. Use camera reframing to signal a new thought: hold a readable wide, gently push 2–6% across several seconds, then cut to a detail or analogy; restore the geography after a diagram. Use background/foreground parallax sparingly. Transition by clean cut, motivated pan, dissolve or shape wipe only when it helps continuity. Never use random motion to manufacture engagement.
6. Put diagrams/labels into screen-safe areas (at least ~5% inset as an initial target), reveal in semantic order, and retain long enough to read. Numbers should count only when useful; reconcile their final values with the script. No flashing or rapid high-contrast patterns.

### D. Sound and timing (proposed, not observed)

- **American accent for every spoken voice:** Select an explicitly American-accented voice for narration and for each character, using U.S. English (`en-US`) for English scripts. Do not substitute other accents. If a suitable accent is unavailable or cannot be verified, disclose that limitation rather than claiming compliance. For non-English speech, use an American-accented voice only if supported; otherwise provide the written script. See `references/voice-direction.md` for niche-specific voice profiles and TTS-ready examples. The reference voice and accent were not auditioned.
- **Energetic, loud and clear:** For every speaker, select an engaging, expressive and confidently projected voice rather than a flat, sleepy or monotone performance. Keep speech prominent over background audio, articulate clearly, vary emphasis and pacing, and re-synthesize weak passages when possible. Match the emotion to the topic without shouting, clipping, forced hype or unintelligible whispering. Audition and listen to the actual output where possible; disclose unverified quality checks.
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

Apply the evidence-tagged structure rubric in `references/story-structure.md`. Check that the actual encoded sequence delivers the promise and planned before/action/after/hold, not just that the storyboard contains those words. Mark unreviewed sound or motion **unknown**, never pass. A plan-field checker does not review media or guarantee creative quality.

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
