# Character structure and working rig

For the long, slim character requested in the current brief, use the original, editable implementation in `../examples/staging-rig-demo.html`. It is a code-authored interpretation of the user's structural direction, not a claim of an exact match or a copy of third-party artwork. Clothing and facial expressions can change while the silhouette and layering remain consistent. The older `../examples/puppet-demo.html` and `../assets/character-rig.svg` illustrate a different, stockier generic rig; **do not use their proportions for this particular character**.

## Geometry and hierarchy

In the working example the root is at ground level, local +x is right, and local +y is down. The head is a near-black circle centered at `(0,-332)`, radius `32`; the capsule torso extends approximately from `y=-298` to `-154` and is 60 units wide; long slender legs extend from around `y=-176` to the feet at ground level. Total height with head is about 364 local units, or about 388 with a helmet. Scale proportionally into your own composition. These are design starting coordinates, not measured claims about the source. Preserve the requested long rounded torso, circular dark head, long slim legs and restrained hands/feet before adding new details.

Draw order in the demo is **far leg → back arm → torso → near leg → front arm → head**. The back arm must be occluded by the torso where it passes behind it; the front arm and hand sit visibly above the torso. When a figure turns, deliberately update depth order rather than letting both arms become printed stripes or both appear in front. Eyes, brows and mouth are children of the head. Attach a letter, bag or other prop inside the correct hand's local group so that it follows the hand.

```text
root at feet
  shadow
  farLeg: hip → knee → foot
  upper (subtle body bob/rotation)
    backArm: shoulder → elbow → wrist/hand
    capsule torso + subtle shade
    nearLeg: hip → knee → foot
    frontArm: shoulder → elbow → wrist/hand → prop
    head: dark circle → eyes / brows / mouth / optional headwear
```

This is an SVG path-based procedural approximation, not a physical skeleton solver. `actor()` creates the groups; `put()` updates the pose; `limb()` computes a planted/swinging foot path. In the example coordinates, limb positions are recomputed from the current time. This makes direct seeking possible, but segment lengths are not mathematically constrained and foot contact is only approximated: inspect the actual motion and improve the solver for demanding shots. Keep the original user brief's structural design separate from other projects that need their own proportions.

## Acting and movement

- **Idle:** tiny head/breath movement, grounded feet and intermittent blink; no constant swaying.
- **Walk:** choose stance versus swing; calculate planted foot position in world space and match body travel to stride. Lift the swing foot and add only a small foot rotation; counter-swing the arms minimally. The demo provides a simple starting pattern, not a guarantee against sliding.
- **Reach or hold:** set a shoulder, elbow and hand path together, ease into a hold, then settle. Move the prop with the hand and check grips at start, contact and release.
- **Expressions:** change brows and mouth for concern, smile or a brief startled reaction. Keep facial features attached to the head and large enough for the intended frame size. Do not rely on exaggerated arm flailing for emotion.
- **Clothing:** change colors, cuffs, collar or headwear without changing the body proportions. For the current user direction, arms and legs move only a little and naturally.

## Visual tests

Inspect neutral silhouette and near/far layering at full frame and mobile size. Verify both feet touch the same ground plane, hands stay connected, held props don't drift, and facial features don't slide during head rotation. Test one complete slow walk frame-by-frame and in real time for foot sliding, knee pops and unnatural leg spacing. Test the back arm, front arm and depth overlap independently. Create additional turning poses if the shot requires them; never pretend a single front-facing rig provides a complete 3D turn. Keep an editable source file and record known limitations.
