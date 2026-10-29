# Backgrounds, lighting and cinematic cutaways

This guide is an actionable code-authored staging recipe, not a claim about the source video's software. Open `../examples/staging-rig-demo.html`: it is a **silent, original, self-contained** ten-second example with two shots, the long capsule character rig, a layered mountain environment, practical color contrast, a journal cutaway, deterministic animation and a short dissolve. Use it as a starting point, not a finished film; replace all story and visual details for the project. Add narration, sound, longer action and conduct review before delivering a film.

## 1. Design the environment around the story

For every shot identify location/time, subject, action, camera distance, light source, emotional purpose and safe areas. Sketch in grayscale before details. Build five independent groups:

1. **Sky and far background:** a gradient, distant mountain/ridge/city silhouettes, small clouds. Far elements have reduced contrast and slower drift.
2. **Midground:** readable location-specific shapes and props. Use silhouettes for far-away vehicles and people, with a recognizable scale and orientation. Avoid accidental claims that an invented scene depicts a documented place or vehicle.
3. **Action plane:** a clear ground line, coherent feet/shadow positions and an uncluttered region behind faces and hands. Set props to attach to the relevant hand or surface.
4. **Foreground:** darker or softer framing shapes and surfaces; leave face, action and subtitles unobscured. Do not apply dense detail uniformly.
5. **Atmosphere:** transparent haze, rain in separate depth layers, dust, drifting smoke or light shafts as the setting warrants. They should not conceal the action or create a seizure-inducing flash.

For a fictional mountain battlefield, for example, layer ridge silhouettes, snowcap accents, flags with no invented historical identification, a small tank silhouette with hull/turret/tracks, distant aircraft traveling nose-first, muddy puddles and wind-driven rain. Change geography and props to suit the actual story; do not turn generic landmarks or vehicles into false historical claims. For a kitchen, substitute distant shelves, worktop action, foreground utensils, steam and practical lamps. Keep composition, hierarchy and lighting principles; do not recycle battle imagery across niches.

## 2. Set light with purpose

Choose a source and color direction per scene: warm porch or interior practical, diffuse overcast outdoors, reflected cool sea light, or restrained flashes on an impact. In SVG define a radial gradient fading to transparent, then place a low-opacity ellipse behind the subject; use a subtle polygon for a directional shaft. Add a small rim highlight or shadow on character and props from the same side. Place ground shadows on the same surface. A screen-wide dark overlay is not lighting. Keep foreground/background values separated, reveal eyes/hands, and avoid a white flash or shaking camera long enough to impair readability. For rain/mud, use scattered angled strokes, animated offsets and small fading ripples; don't animate the whole scene as one rigid card.

Example SVG layer order:

```html
<g class="camera">
  <rect width="1280" height="720" fill="url(#sky)"/>
  <g id="far-ridges">…</g>
  <g id="moving-clouds">…</g>
  <g id="midground">…</g>
  <ellipse fill="url(#warmPool)" cx="900" cy="250" rx="300" ry="190" opacity=".18"/>
  <g id="actors">…</g>
  <g id="foreground">…</g>
  <g id="weather">…</g>
</g>
```

The ellipses represent your own content, not a complete runnable scene; the included HTML is executable. Each layer's movement should be deterministic from time, for instance `cloudX = -8*t`, foreground motion faster than background, or ripples with `phase=(t*speed+offset)%1`. Animate only the groups that should move. Crop moving layers beyond frame bounds to avoid revealing blank edges. Work in scene coordinates before camera transform.

## 3. Direct an actual sequence, not just a backdrop

Build a shot list timed to the narration: a purposeful hook, an establishing wide, medium character action, motivated object/letter insert, vehicle or environment cutaway, consequence/reaction, and quieter close. Not every beat needs a character. For each cut, note what changes, why it happens at that word, and how it maintains geography (screen direction, eyeline, prop shape and relative position). Scale an object up for an insert, not all scene elements; mark symbolic closeups as illustrative. Change lighting as locations change.

Use a planned hard cut when action or an important word lands. Use a short eased dissolve only if the shots benefit from a softer passage; avoid ghosted text/labels and unmotivated long crossfades. The example uses two independently rendered SVG groups and a 0.22-second dissolve; during overlap, hold the prior shot and compute the current opacity using smoothstep. Use masks/wipes sparingly. Move the camera subtly and separately from the characters; an SVG scale/translate is a 2D camera simulation, not a true 3D angle. Reserve brief shake for a motivated event; never shake every shot at high amplitude.

## 4. Render and review

The example auto-plays when opened and exposes `window.seek(seconds)`; open with `?t=3.5` to inspect an exact point. Its geometry, motion and shot timing are editable inline, so agents without a specific animation framework can adapt it. To render, follow `code-animation.md` and use the available local browser and encoder. Ensure every `seek(t)` resets all relevant state: render out of order as well as in sequence to find accumulated transforms/opacity.

Review first/middle/last frames of every shot, overlap frames, prop contacts, moving objects at start and end, mobile-safe labels, lighting consistency and facial readability. Check that characters retain **back arm → torso → front arm**, slim legs and long rounded torso if the brief requests this design. Inspect encoded output, decode the full file, and actually play the motion and audio when those capabilities exist. Still frames and technical checks cannot prove expressive motion or sound quality. Iterate from user feedback; document evidence and remaining limitations in the living production notes.

## Motivated opening: follow a moving object

When an action hook suits the brief, plan a visible causal chain rather than an unrelated dramatic flash: **establish vehicle → show the object attached → release → follow object in world coordinates → show a restrained consequence → reveal the story promise → return to a human-scale scene**. For other genres replace the military example with an appropriate item: a parcel falling from a shelf, a rocket launching, a ball entering a goal, or a seed traveling in the wind. Do not imply fictional visuals are real footage or sensationalize human suffering.

For a 2D SVG stage taller than the viewport, place the vehicle, object, clouds and ground in the same world coordinate system. Before release, compute the object's position from the vehicle; after release, use a continuous trajectory beginning at the exact release position. For instance, `y = y0 + v*dt + 0.5*g*dt*dt`, and a restrained horizontal drift. Compute camera offset from the object position with bounds; keep the object inside a readable region while the world moves behind it. At impact replace the object with a short, soft light/dust event, then hold and resolve. Use a path and timing suitable to the content, not a claim of real physics. Never hide a jump at release or leave blank edges as the camera tracks.

Use an authored sky gradient and a motivated warm backlight, subtle directionally consistent highlights on vehicle/prop, deeper distant silhouettes, and a localized consequence glow. The rest of the film should have different lighting appropriate to each location—not one global overlay. Schedule sound and narration relative to the new cut, shift captions and downstream cues together, and inspect release, tracking, impact, title safe bounds, transition and speech onset in the **encoded** video. Watch and listen when available; otherwise label those perceptual checks unverified.
