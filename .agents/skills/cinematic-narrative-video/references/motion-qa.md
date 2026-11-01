# Motion, contact and glitch QA

The user rejected recent videos for insufficient animation and glitchy elements. A successful render and a list of planned events are not proof of usable motion. Design the performance and set, inspect the output, fix the defects, then test again.

## Implement a contact rather than simulating one

1. Define a shoulder or hip root, joint, endpoint and two fixed segment lengths in the rig's rest coordinate space. Define a readable target and action timings: approach, contact, hold, release and follow-through. Avoid moving a separate prop on a guessed timeline when it is supposed to be gripped.
2. Transform the target into the same coordinate space as the chain and solve the elbow/knee. `../examples/contact-physics.js` offers a minimal 2D two-bone solution and affine matrix helpers. Its `reachable` flag is false when the requested target lies outside the chain's distance range; `end` is then clamped and `error` reports the miss. Change the blocking, character position or action; do not silently accept an unreachable grip. These helpers don't model anatomy, collisions, rotations, cloth or realistic weight.
3. During a grip, make the prop a child of the hand, or compute it from the hand's world transform. When parenting changes, multiply by the inverse of the new parent's world matrix so that the world-space pose does not jump. Deliberately define grip points and release timing. In a handoff, preserve contact with the giver until transfer and with the receiver thereafter; a prop center and a hand center are not necessarily the intended contact points.
4. For walking or stairs, make a world-space stance foot stay fixed while the body travels; choose a swing arc that clears the surface and ends on the next real tread. Solve the leg to that target and respect actual segment lengths and scale. Keep physical foot contact, torso height, forward travel and an occluding entrance consistent. Change staging or create additional poses if the movement cannot be performed naturally by the rig. A disappearing person or a set of timed still positions is not a climb.
5. Keep far arm, torso, near arm, hand, prop and surrounding objects in deliberate draw order. Test entry/exit behind occluders. Parent facial details to the head, and check expressions/readability at final size. Add idle breathing, gaze, posture shifts and blinks appropriate to the scene, but do not use idle as a substitute for a meaningful performance.

## Measure the actual authored transforms

Sample after applying the real pose, parent and camera transforms, not from an independent expected timeline. Use a common world-space coordinate system; if one point is in camera/screen space, invert the camera transform first. Export each frame in the critical action range, with joint centers and contact anchors. The technique study exports `window.motionSamples(t)` by reading actual SVG geometry and current transformation matrices; it uses the same world-coordinate system for the hand and switch. Adapt the exporter to your own DOM, Canvas or 3D scene. Sample before, during and after the intended contact, the transfer and occlusion; a sparse test misses transient artifacts.

A minimal input to the optional MCP tool `check_motion_samples` is:

```json
{
  "motion": {
    "space": "world",
    "samples": [
      {"time": 0.0, "limbs": [{"id": "arm", "joints": [[0, 0], [3, 4], [6, 8]], "rest_lengths": [5, 5], "relative_tolerance": 0.05}], "contacts": [{"id": "grip-1", "point": [6, 8], "target": [6, 8], "tolerance": 0.5, "fixed_target": true}]},
      {"time": 0.033, "limbs": [{"id": "arm", "joints": [[0, 0], [3, 4], [6, 8]], "rest_lengths": [5, 5], "relative_tolerance": 0.05}], "contacts": [{"id": "grip-1", "point": [6, 8], "target": [6, 8], "tolerance": 0.5, "fixed_target": true}]}
    ]
  }
}
```

`joints` are root, middle joint and end; `rest_lengths` match the two segments. Use meaningful nonzero, per-project tolerances in the chosen world units, and record why they are suitable at delivery size. `fixed_target: true` also compares the target with its first position for the same contact ID; use a new ID for a new stance or grip phase. For a moving handheld prop, omit `fixed_target` but compare hand and prop grip anchors throughout. Empty limb/contact arrays, non-finite data, unordered times and invalid coordinate systems are rejected. Sampling gaps over 0.101 seconds are warned; this threshold is not a completeness guarantee. Up to 5,000 samples per call; split long takes with overlapping boundaries and new IDs as appropriate.

The checker reports only numerical discrepancies in the supplied values, with a cap on displayed issues. It does **not** know whether the anchors, tolerance or phase are correct, check the actual pixels/encoded file, infer meaning, ensure continuity between batches, verify that every frame was exported or judge physicality and taste. A pass is not a visual, animation or reference-quality pass.

## Evidence and human review

- Record actual timestamps for anticipation, contact, hold, release, result, pose reaction, transition, and any feet crossing ground, stairs or occluders. Inspect every critical contact in the encoded output frame by frame. Verify that props do not float or snap; no limbs pass through unsupported objects; foot plants do not slide; and scene edges do not show unexpectedly.
- Inspect lighting hierarchy, background depth, silhouettes and facial readability in the actual output at full frame and phone size. Inspect subject/action movement separately from weather, camera, captions and dissolve.
- Watch normal-speed and slowed action, listen to the final mix, and compare the result with the user's reference when those capabilities exist. Mark each unavailable check **unknown**. Record unresolved failures and avoid treating a basic math test as artistic approval.
- The included `../examples/contact-light-study.html` is original, silent and deliberately limited to a single switch/plant action. It demonstrates contact/export mechanics; it does not demonstrate a complete narrative, walking, handoffs, rich shot variation, sound or equivalence to the reference. The caller must build and evaluate a representative test in the actual project's style.
