# Voice and audio direction

## Evidence limit

No reference audio was auditioned. The public transcript supports the presence of narration, occasional dialogue and music markers, but not a specific gender, accent, voice timbre, speaking rate, emotional delivery, music genre, sound effects, or exact sync. The profiles below are **original recommendations**, not a transcription of the reference voice. Never use or request a clone of an identifiable narrator.

## Voice profile A — main narrator

- Role: an approachable narrator who can explain, tell a story or guide the viewer, without sounding like a sales pitch. Adapt the performance to the niche, characters and intended emotion.
- Age impression: adult. Gender: unrestricted unless the user specifies; choose an available voice appropriate to the requested language and audience.
- Tone: warm, close, dryly curious, conversational; gentle sense of wonder; matter-of-fact during technical explanations, warmer or more dramatic when the story calls for it. A light, friendly smile is fine. Avoid exaggerated cartoon squeaks, hype, whispered ASMR, theatrical gravitas, or an imitation of a particular creator.
- Pace: begin testing at roughly 135–155 spoken words per minute, with a short pause after the setup and before a major reversal; adjust to the selected voice and intended runtime. Numerical facts can use slightly slower articulation; do not insert artificial pauses at every sentence.
- Delivery contour: match the chosen story structure—curiosity or urgency at the hook, clarity during explanation or action, space around a turn or character reaction, and an appropriate resolution. Include caveats for factual uncertainty. Never use rising pitch on every line.
- Recording: clean, close and dry mono or stereo speech, no embedded soundtrack/reverb; provide PCM WAV when possible. Avoid noise, breath pops and clipped consonants. Use pronunciation hints in the TTS tool if supported and needed.

## Voice profile B — character reactions

- Use an optional second voice, clearly distinct from the narrator and any other characters. Character speech should be brief and natural, with a slight surprised or concerned reaction. Gender, accent and age depend on the brief; don't imply the reference has a particular voice.
- Keep character dialogue distinct in timing and spatial position, but not so distant or processed that it becomes hard to understand. Small pauses around reactions give them room. Avoid treating the written transcript as proof of a specific reference delivery.

## Tool workflow and TTS scripts

1. Write and fact-check the exact script, with natural punctuation and speaker labels. Specify language and pronunciation per role. If the agent has native TTS, use it directly. Preview the same 30–45 word passage in candidate voices when the tool supports auditioning; register any voice as required by the agent's tools. Do not ask the user to find a TTS service if you have one.
2. Synthesize separate chunks at sentence or beat boundaries. Save a mapping from cue ID to audio filename and actual measured duration. Example plain-text narrator audition, inspired by the sample topic but not by the reference wording:

   > Imagine a night with no Moon overhead. The sky would look different, but the more interesting changes would happen closer to home. What keeps the tides moving, and what would remain if our familiar companion disappeared?

   Example character audition:

   > Wait, you mean the ocean would still have tides? I thought the Moon did all of that. So what else is pulling on the water?

   These audition lines are original. Check factual claims for the topic before publishing; use as voice tests, not a substitute for research.
3. Use a forced aligner, TTS timing metadata or careful manual cueing to mark start/end of phrases. Without a reliable aligner, timing can be approximate and must be reviewed. Animate labels and visual reveals on the key noun or concept; avoid simultaneous dialogue and important competing text.
4. Add original or appropriately licensed SFX/music on separate tracks. Examples of possible *proposed* design, not observed reference sounds: soft paper movement, restrained chalk ticks, low ambient texture, gentle neutral notification cue. Keep effects short and quiet; no clone or extraction of source audio.
5. Mix for speech intelligibility; begin around −16 LUFS integrated stereo and ≤−1 dBTP true peak as optional production targets, not platform rules. Duck the bed under voice. Confirm actual levels with available tooling and listen end to end. If audio listening is unavailable, clearly mark listening-based quality control as incomplete.

## Example human-readable cue sheet

| Cue | Speaker / mood | Text | Trigger | Sound design starting point |
|---|---|---|---|---|
| V01 | narrator; curious | First two lines of `../examples/example-script-and-board.md` | 0:00; opening image | subtle original ambient bed |
| V02 | narrator; explanatory | The board/diagram explanation | measured end of V01 | optional soft chart reveal |
| V03 | character; puzzled | One short question | allow a short gap after V02 | do not mask the voice |
| V04 | narrator; clear, qualified | Answer and limits | after V03 | reduce bed slightly under voice |

The rendered audio determines actual timestamps; never assume the nominal storyboard time exactly matches the TTS duration. Use the generated waveform and listening to adjust visuals and cue timing. If TTS is unavailable, deliver labeled text and disclose that the finished voiced video is blocked; do not pretend that a silent preview passes.
