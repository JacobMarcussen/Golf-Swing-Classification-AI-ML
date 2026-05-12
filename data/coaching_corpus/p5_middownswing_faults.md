# P5 — Mid-downswing — Common Faults and Fixes

## Casting (early release of lag)

**What it looks like:** The wrist hinge that was stored at the top (P4) releases early during the downswing — by P5, the shaft is nearly in line with the lead arm rather than maintaining a 60-90° lag angle. The club head "throws" outward in a casting motion, similar to casting a fishing rod.

**Detection signal:** `shaft proxy angle` from the lead arm showing near-linear alignment (lag angle below 40°) at P5; `left_wrist` extending prematurely; `right_elbow` extending and pushing away from the body before impact.

**Why it happens:** The most common cause is an instinct to "hit" at the ball by firing the hands early. Also caused by insufficient core and lower body strength — the arms take over when the body can't generate force efficiently. Anxiety about distance sometimes exacerbates casting.

**Fix:** Feel the trail elbow leading the hands into the impact zone — "bump the hip first, then the elbow drops." Drill: make slow downswings stopping at P5 and checking that the angle between the club and lead arm is still acute. The "whoosh" drill — swinging a club upside-down — gives auditory feedback that the speed is delivered past the ball, not before it.

## Over-the-top (outside-in swing path)

**What it looks like:** The club arrives at P5 from outside the target line — the club head is above the hands when viewed from behind, and the shaft approaches steeply from the outside. This is one of the most common faults in amateur golf and produces pulls, pull-slices, and weak contact.

**Detection signal:** `shaft proxy angle` showing the club approaching steep and from outside the target line; `left_shoulder` elevated or "throwing" outward; `shoulder_line_from_horizontal` significantly open (rotating too fast ahead of the lower body).

**Why it happens:** The shoulders begin the downswing before the lower body has cleared, causing the arms and club to be thrown out and over. Often traced back to a steep P4 (laid-off or flying elbow) combined with insufficient hip drive.

**Fix:** Initiate the downswing with a "bump" of the lead hip toward the target before the arms move. The feeling is that the lower body starts first. Drill: make downswings dropping a pool ball behind the trail knee and feeling the knee move toward the ball before the arms begin down.

## Early extension (hips thrusting toward ball)

**What it looks like:** The hips drive forward (toward the ball) rather than rotating. The spine angle decreases — the golfer "stands up" — and the arms have no room to swing through. This causes the club to approach from the inside and below the swing plane, often resulting in blocks, hooks, or fat contact.

**Detection signal:** `spine_angle_from_vertical` decreasing from its address value by more than 8-10°; `right_hip` and `left_hip` showing lateral movement toward the ball rather than rotational clearing; `hip_line_from_horizontal` shifting forward.

**Why it happens:** Poor sequencing — the hips thrust instead of rotate, often because the golfer has learned to "use the hips" incorrectly. Can also be a compensatory move when the backswing is excessively flat, forcing the body to make room for the club.

**Fix:** Feel the trail hip rotating through rather than thrusting toward the ball. Cue: "rotate around a fixed axis." Drill: make downswings with the back against a wall or chair; early extension pushes the hips into the wall, making the fault immediately apparent.

## Trail elbow chicken wing (elbow separating from body)

**What it looks like:** The trail elbow moves outward away from the body during the downswing rather than staying tucked close to the trail side. This typically causes the club to approach from outside the target line and produces an over-the-top motion.

**Detection signal:** `right_elbow` position showing it moving laterally away from the torso rather than downward and inward; `right_shoulder` elevated or pushed outward; shaft approach angle steep.

**Why it happens:** Usually stems from a flying trail elbow at P4, which propagates into P5. Also caused by an over-the-top move where the arm is pushed out to compensate for the steep approach.

**Fix:** Feel the trail elbow "brushing" the trail hip as it comes down. Drill: swing with a headcover tucked under the trail armpit — keeping it in place through the downswing ensures the elbow stays connected.

## Insufficient hip clearance (blocked rotation)

**What it looks like:** At P5, the hips have not rotated sufficiently toward the target. The lead hip has not cleared to the left (for a right-handed player), leaving the body "stuck." The arms swing past the body and the club tends to come from too far inside, causing blocks and pushes.

**Detection signal:** `hip_line_from_horizontal` showing minimal rotation back toward the target; `left_hip` and `right_hip` values showing less forward rotation than the shoulders; weight distribution still heavily on the trail side at P5.

**Why it happens:** Often a sequencing issue where the upper and lower body work in synchrony rather than with the lower body leading. Can also be caused by a ball position too far back in the stance, restricted lead hip mobility, or an excessively closed stance at address.

**Fix:** Initiate the downswing by feeling the lead hip "turning out of the way" first. Cue: "clear the lead hip." Drill: place an alignment stick in the ground next to the lead hip; practice rotating the hip to touch the stick without sliding toward it.
