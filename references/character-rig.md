# Character construction and rig reference

This is an **original proposed rig**, not recovered source artwork or a claim about the reference's actual joints. See `../assets/character-rig.svg` for a visual model and `../examples/puppet-demo.html` for an animated implementation.

## Coordinate system and proportions

Use 1920×1080 scene pixels or an equivalent scalable coordinate system. Position the rig's root at the midpoint between the ankles on the ground; local +x points right and +y points down. This starter character's total height is roughly 412 local units. Scale uniformly into a scene; e.g. `scale=0.55` makes a ~227 px figure. Sizes below are starting points, not measured proportions of the source.

| Component | Local geometry or pivot | Parent / attachment |
|---|---|---|
| Root / feet baseline | `(0, 0)` | Scene transform |
| Pelvis | `(0, -190)` | Root |
| Torso | rounded rectangle `(-32,-324,64,134)` | Pelvis, optional slight rotation |
| Neck | `(0,-327)` | Torso |
| Head | center `(0,-369)`, radius `42` | Neck |
| Left shoulder / elbow / wrist | `(-29,-300) / (-57,-236) / (-58,-185)` | Torso → upper arm → forearm |
| Right shoulder / elbow / wrist | `(29,-300) / (57,-236) / (58,-185)` | Torso → upper arm → forearm |
| Left hip / knee / ankle | `(-15,-190) / (-22,-101) / (-29,-11)` | Pelvis → thigh → calf |
| Right hip / knee / ankle | `(15,-190) / (22,-101) / (29,-11)` | Pelvis → thigh → calf |
| Eyes, brows and mouth | in head-local coordinates | Head; remain attached to head rotation |

Draw the figure with a softly rim-lit near-black circle for the head, a distinct colored, gently shaded garment, slim limbs, simple shoes and small hands. The silhouette should still read when the figure's entire height is under ~200 pixels. Make two original characters distinguishable by clothing color, shape, hair or accessories; do not copy the reference's distinctive designs.

## Rigging and layer order

A 2D skeletal rig is the suggested implementation; it is not known how the original was made. An animator or agent can implement rigid pieces, vector paths, an HTML Canvas hierarchy, Blender 2D/3D or another local renderer. Build a model sheet with front, side, 3/4 and close-up; test each limb bend before animating. Name assets descriptively:

```
scene/root
  farLeg: hip > thigh > knee > calf > ankle > foot
  farArm: shoulder > upperArm > elbow > forearm > wrist > hand
  pelvis > torso > neck > head > [eyes, brows, mouth, hair/accessory]
  nearLeg: hip > thigh > knee > calf > ankle > foot
  nearArm: shoulder > upperArm > elbow > forearm > wrist > hand
```

Depth order changes on turns: put the far side behind the body and near side in front. Place circles or sleeve cuffs over joints to conceal seams. Keep limb segment lengths constant. Every child transform is relative to the parent; local rotation around a pivot `p` is `T(p) R(angle) T(-p)`. For line-segment drawing, compute the elbow from shoulder plus the first vector rotated by shoulder angle, then compute the hand from elbow plus the second vector rotated by shoulder + elbow angle. Avoid moving the hand independently while leaving the arm behind.

### Minimum pose library

- **Neutral:** relaxed shoulders, legs shoulder-width, mouth small, eyes level.
- **Curious:** head tilted 5–10°, brows raised, one forearm rotated upward, feet grounded.
- **Concerned:** inner brows raised, mouth downturned, shoulders slightly forward.
- **Explain/point:** one upper arm lifted, forearm directed toward an object, body facing the audience. Anchor finger/hand to the visual target during a hold.
- **Walk:** alternating legs; one planted foot under body while the other swings; hip advances at a pace consistent with stride. Arms counter-swing unless one hand holds a prop.
- **Blink:** eyes scale vertically down then up over a few frames. Do not blink constantly. **Speech:** swap mouth shapes or use actual phoneme alignment where available; crude amplitude-driven mouth motion is approximate.

Illustrative pose key data (angles in degrees, relative to parent, not a ready-to-run renderer):

```json
{
  "id": "curious",
  "root": {"x": 384, "y": 922, "scale": 0.55},
  "channels": {"head.rotation": -7, "torso.rotation": 2,
    "nearArm.shoulder": -28, "nearArm.elbow": -48,
    "farArm.shoulder": 5, "leftLeg.hip": 2, "rightLeg.hip": -3},
  "face": {"eyes": "open", "brows": "raised", "mouth": "small-o"}
}
```

Agent implementation must define sign conventions for angles, rests, transform order and the actual local coordinates; do not assume this JSON alone animates anything. Tween only the affected channels with easing, keep feet grounded during still holds, and inspect frame sequences for elbow snapping, floating props, facial drift or accidental foot sliding.

## Rig QA

1. In a neutral front pose check both feet touch the same ground plane.
2. Rotate head, each shoulder, elbow, hip and knee independently. No disconnection or inverted hierarchy.
3. Test reaching and walking with prop contact; inspect frames at 30 fps. Contact points do not slide or pop.
4. Render neutral and curious poses at intended mobile size; eyes and gestures are readable without huge outlines.
5. Check that all three principal facial expressions convey intended emotion without relying on color.
6. Keep the editable source rig and its original asset/license notes in the production project.
