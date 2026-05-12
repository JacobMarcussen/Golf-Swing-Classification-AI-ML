# Step 5 — Retrieval trace

## Query embedded

```
Coaching advice for Mid-downswing swing position. Notable deviations:   right_shoulder is 85.2° (above typical range 28.0-60.5°)   hip_line_from_horizontal is 179.5° (above typical range -177.8-177.9°)   shoulder_line_from_horizontal is -177.7° (below typical range -174.4-172.4°)   shaft (lead-arm proxy) is 179.6° (above typical range -173.2-173.9°)
```

## Retrieved chunks

### Chunk 1 (distance 0.7000)

**Source**: `p5_middownswing_faults.md` | section: *Over-the-top (outside-in swing path)*

```
## Over-the-top (outside-in swing path)

**What it looks like:** The club arrives at P5 from outside the target line — the club head is above the hands when viewed from behind, and the shaft approaches steeply from the outside. This is one of the most common faults in amateur golf and produces pulls, pull-slices, and weak contact.

**Detection signal:** `shaft proxy angle` showing the club approaching steep and from outside the target line; `left_shoulder` elevated or "throwing" outward; `shoulder_line_from_horizontal` significantly open (rotating too fast ahead of the lower body).

**Why it happens:** The shoulders begin the downswing before the lower body has cleared, causing the arms and club to be thrown out and over. Often traced back to a steep P4 (laid-off or flying elbow) combined with insufficient hip drive.

**Fix:** Initiate the downswing with a "bump" of the lead hip toward the target before the arms move. The feeling is that the lower body starts first. Drill: make downswings dropping a pool ball behind the trail knee and feeling the knee move toward the ball before the arms begin down.
```

### Chunk 2 (distance 0.7988)

**Source**: `p5_middownswing_faults.md` | section: *Insufficient hip clearance (blocked rotation)*

```
## Insufficient hip clearance (blocked rotation)

**What it looks like:** At P5, the hips have not rotated sufficiently toward the target. The lead hip has not cleared to the left (for a right-handed player), leaving the body "stuck." The arms swing past the body and the club tends to come from too far inside, causing blocks and pushes.

**Detection signal:** `hip_line_from_horizontal` showing minimal rotation back toward the target; `left_hip` and `right_hip` values showing less forward rotation than the shoulders; weight distribution still heavily on the trail side at P5.

**Why it happens:** Often a sequencing issue where the upper and lower body work in synchrony rather than with the lower body leading. Can also be caused by a ball position too far back in the stance, restricted lead hip mobility, or an excessively closed stance at address.

**Fix:** Initiate the downswing by feeling the lead hip "turning out of the way" first. Cue: "clear the lead hip." Drill: place an alignment stick in the ground next to the lead hip; practice rotating the hip to touch the stick without sliding toward it.
```

### Chunk 3 (distance 0.8270)

**Source**: `p5_middownswing_faults.md` | section: *Early extension (hips thrusting toward ball)*

```
## Early extension (hips thrusting toward ball)

**What it looks like:** The hips drive forward (toward the ball) rather than rotating. The spine angle decreases — the golfer "stands up" — and the arms have no room to swing through. This causes the club to approach from the inside and below the swing plane, often resulting in blocks, hooks, or fat contact.

**Detection signal:** `spine_angle_from_vertical` decreasing from its address value by more than 8-10°; `right_hip` and `left_hip` showing lateral movement toward the ball rather than rotational clearing; `hip_line_from_horizontal` shifting forward.

**Why it happens:** Poor sequencing — the hips thrust instead of rotate, often because the golfer has learned to "use the hips" incorrectly. Can also be a compensatory move when the backswing is excessively flat, forcing the body to make room for the club.

**Fix:** Feel the trail hip rotating through rather than thrusting toward the ball. Cue: "rotate around a fixed axis." Drill: make downswings with the back against a wall or chair; early extension pushes the hips into the wall, making the fault immediately apparent.
```

