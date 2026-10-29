# Living production notes

**Purpose:** Working notes for improving the cinematic narrative video skill. Update this file when new user feedback or a verified production lesson changes the recommendations. Date updates; distinguish direct user feedback and observed evidence from hypotheses. Promote tested general principles into `SKILL.md`, the rig, animation, voice or niche guides when appropriate. Do not present these notes as proof of reference-equivalent quality.

## 2026-10-30 — specific character-structure correction

The user supplied three close-up character screenshots and clarified the intended silhouette. For this user's requested character style, treat the images as the structural reference:

- A large, almost circular dark head with simple white eyes, small brows and mouth; a narrow, long rounded or capsule-like torso, not the stocky short jacket body used in the previous cut.
- Very long, slim dark legs with small understated feet; in a resting side-oriented pose, the legs can nearly overlap. A foreground leg may begin visually in front of the lower torso.
- **Updated correction:** The user clarified that one arm and hand should be in front of the torso and the other arm behind it, with the rear hand partially visible at the edge. This supersedes the earlier instruction that both should be in front. Set actual drawing order to back arm → torso → front arm, with the hands attached to their respective arms. Show rounded clothing-colored sleeve caps, thin dark arms and small dark hands. Keep any carried prop attached to its hand, and avoid rigid parallel marks that read as printed decorations.
- Maintain the same underlying body proportions and structure between characters; change clothes and facial expressions as needed. Preserve distinct poses and subtle details without inventing a new stocky anatomy.
- Motion should be restrained and natural: legs move a little, arms move a little, and contact with the ground should remain plausible. Avoid exaggerated knee bends, wide swings, rubbery limbs or large involuntary head/body movements. Use bigger action only if the user later asks for it. The goal is controlled motion, not a static image.
- These are visual observations and the user's requested structure; the new code-authored rig is an interpretation, not proof of an exact match. Inspect close-ups and motion sequences and ask the user to judge the result.

This is a **current, user-specific direction** and takes precedence over older broad rig examples below where they conflict. Keep these notes updated with later corrections and verified tests.

## 2026-10-30 — reference and feedback

### Evidence and limits

- The supplied reference excerpt was approximately 3:57.9 of a longer video. Its visuals were sampled across the excerpt, and selected brief actions were examined frame-by-frame; the full reference and its final portion were not inspected in real time. Audio was not directly auditioned. Do not claim precise soundtrack details or that the original's production software is known. HTML, CSS and SVG are practical reconstruction tools, not a verified identification of the original pipeline.
- Reference observations include a layered street with a small articulated walker; character gestures coupled to sequential chalkboard marks; camera compositions, warm practical light and foreground occlusion; and cuts to standalone objects, vehicles, diagrams and other visual metaphors. The cast does not need to appear in every shot.
- The user wants a more cinematic, lively result, especially better motion, walking, body structure, hands, legs, feet, expressions, camera movement, sound effects and flowing scenes. They specifically requested additional shake where appropriate and non-character subjects such as ships and aircraft. They viewed the third WWII cut as an improvement while asking for more components, stronger hooks and further animation improvement. This is user feedback, not a general quality certification.
- Earlier still-heavy output was rejected; a simple silent backyard demo was rejected as dull; the first voiced WWII version was considered too flat and static; the second was considered insufficiently natural. Do not reuse these as evidence of a successful match. Several new examples below are tests and proposals, not guarantees that they meet the user's target.

### Hook, pacing and storyboarding

1. Start with a visual promise that is meaningful to the story: a striking action, object, question or consequence, quickly followed by context. A hook should make viewers curious without misleading them or sensationalizing sensitive material.
2. Storyboard more than one type of shot: character performance; location establishing shot; prop close-up; vehicle or environmental action; progressive diagram or visual metaphor; and a quieter emotional detail. Only use the combinations relevant to the story. Avoid placing the same standing character against every backdrop.
3. Time visual events to the specific words or ideas they support. Leave room for comprehension, and use movement, revealing details, changes in shot size and cuts rather than letting every shot become a static illustration with text.
4. Preserve spatial continuity through shot changes; use intentional cut points, matched movement, short dissolves or other transitions appropriate to the scene. A dissolve is not a substitute for action. Vary framing and the motion of camera versus subjects; flat 2D push-ins are not genuine 3D camera angles.
5. Plan ambient motion separately from main action: smoke drifting, water moving, cloud parallax, lights, depth and foreground elements. Controlled camera drift or shake can add immediacy; reserve stronger shakes for motivated impacts and keep them brief enough to preserve legibility and viewer comfort.

### Character structure and motion

- Use a consistent character design with independent head, eyes, brows, mouth, torso, upper and lower arms, hands, upper and lower legs, feet and shadows. Specify pivots, hierarchy and attachment points. Characters, props, and rigs should be original, not copies of reference assets.
- Construct action through anticipation, purposeful movement, overlap/follow-through and a settle. Vary timing and pauses. Breathing, blinks, gaze changes and small weight shifts should support the action, not replace it.
- For a walk, separately animate hips, knees, ankles and feet. Alternate stance and swing; keep the planted foot approximately stationary in world space and lift the swinging foot, with visible heel/toe or foot rotation when suitable. Couple stride length, walk cycle and translation speed so the character does not slide. Use reference footage and frame-by-frame checks, including reversals and contact positions. A periodic rotation of a rigid straight leg is not enough.
- Animate arm swing opposite the legs when appropriate. Use elbows, wrists and clearly readable hands; stage grips so a held letter, suitcase or tool remains attached to the hand. A pointing or writing hand should travel to the mark or object and align with its reveal.
- Plan a character's direction of travel, facing, posture and intent for each action. Use physically plausible weight shifts; avoid both legs permanently bent in the same direction, jumping poses, indistinct hands, or interchangeable characters with no acting. Procedural inverse kinematics is one possible technique; it still requires visual review and may not look hand-animated.
- Check action at full speed, slow speed and frame-by-frame. Test contact numerically when useful, but do not let numeric tests replace perceptual review. Adjust foot placements and arm paths for the particular character's scale and speed.

### Objects and atmosphere

- Make non-character elements active when narratively useful: for example a locomotive with smoke and moving wheels, a troopship with wake and smoke, or aircraft with propeller, cloud parallax and a flyby. Build only historically appropriate elements and label generalized or fictional visuals; avoid falsely identifying invented vehicles or locations.
- Develop environments as layered compositions rather than flat backdrops: distant setting, midground action, foreground framing, meaningful props, local lighting, material detail, shadows and atmospheric depth. Add details that support the shot, not decorative clutter.
- For graphics, reveal diagrams, maps, marks or object labels progressively. A line or route can animate with a matching moving symbol; include qualifying language if a map or event is illustrative rather than a specific historical claim.

### Voice, written numbers and sound

- The user's standing direction is American accents only, with niche-appropriate voices that are lively, clear and engaging. User-selected voice identity should stay consistent across regenerated lines; never include generated voice recordings inside the skill repository.
- Write years in TTS scripts as they should be spoken. For example, script **“nineteen forty-four”** for the year 1944 rather than assuming the engine will read `1944` as a year; use “nineteen ninety-nine” for 1999. This user explicitly disliked hearing years read as long cardinal numbers. Keep human-readable captions as `1944` if desired, provided they match the actual narration. Audition or otherwise verify the resulting speech; spelling improves the odds but is not a guarantee.
- The opening year in the previous WWII cut was recognized as “one thousand nine hundred and forty four”; the user highlighted the unnatural number-reading pattern. A replacement was scripted as “nineteen forty-four”; automatic speech recognition of the replacement returned “nineteen forty four.” This is a useful pronunciation check, but the clip was not directly auditioned, so a human listening check remains recommended.
- Narration, music, room/setting ambience and distinct synchronized foley need separate roles and sensible levels. Use licensed or self-made music/effects, cue them to motion, and preserve clear dialogue. Do not copy the reference soundtrack or assert its content without actually hearing it. Automated RMS, peak and decode checks are not a substitute for listening.
- Cite third-party media and licenses accurately, even for CC0 assets where credit is not required. Distinguish a modern illustrative sound from a historical recording. Never put reference audio into the skill repository.

### Repeatable workflow and QA

1. Gather topic, intended audience, requested length and reference; research factual claims and rights. Obtain the reference through permitted means and keep a clear cleanup inventory. Retain only specifically authorized reference stills; delete temporary source video, unselected frames, extracted reference audio and job-specific installs when requested.
2. Break down representative motion and shot types, note evidence limits, and produce a timed storyboard that includes hooks, subjects, visual changes, sound cues, scripts and claims. Mark fictional composites and illustrative maps/vehicles.
3. Build original code-authored characters, environments and object assets. Image generation is not required for this workflow. Plan deterministic timeline seeking and reusable rigs; take advantage of native tools and TTS when available. The skill must work with or without native skills support; the optional MCP is not a renderer or a speech service.
4. Produce an actual voiced, sound-designed style test when the user agrees to that gate; review it before expanding. A style test is not a finished deliverable and an unvoiced silent demo does not satisfy a request for a voiced film. If the user requests a complete video, do not silently substitute a brief test.
5. Validate clips, narration pronunciation, captions, edit timing, foot contacts, prop attachments, shot continuity, safe display, audio peaks and decoding. Examine actual encoded frames and listen to the final mix if a listening tool is available. Be explicit if actual listening or perceptual motion review was unavailable. Report unresolved defects honestly; do not describe a vector test as an exact cinematic match.
6. Keep the notes current: append dated feedback, tests and lessons whenever new information arrives. Revise or mark obsolete recommendations instead of presenting unverified guesses as established facts. Keep repo guidance portable, lean and readable; preserve MIT attribution and separate reference-frame rights.
