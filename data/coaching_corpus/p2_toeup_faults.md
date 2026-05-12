# P2 — Toe-up — Common Faults and Fixes

## Inside takeaway (club too far inside)

**What it looks like:** The club is pulled behind the body early in the takeaway rather than tracking along or outside the target line. From a down-the-line view, the club shaft disappears behind the trail hip well before it reaches hip height. The lead arm often collapses inward across the chest.

**Detection signal:** `shaft proxy angle` deviating significantly to the inside of target line at P2; `right_shoulder` and `left_shoulder` values showing limited rotation relative to the amount of arm swing; `left_elbow` showing increased flex (below 155°).

**Why it happens:** The golfer initiates the takeaway with the hands and arms rather than the body, rolling the club inward immediately. A weak grip or fear of an outside swing path are common causes.

**Fix:** Use a one-piece takeaway — the shoulders, arms, and club should move together as a unit for the first foot of the swing. Drill: place an alignment rod along the target line and practice sweeping the club head along this rod for the first 18 inches of the backswing.

## Outside takeaway (club laid off or steep)

**What it looks like:** The club is pushed away from the body, with the shaft tracking well outside the target line. The club head moves toward the target line or beyond it before the arm reaches hip height, producing a steep swing plane.

**Detection signal:** `shaft proxy angle` deviating to the outside of target line; `shoulder_line_from_horizontal` showing less rotation than expected relative to arm position, indicating the arms are outrunning body turn.

**Why it happens:** Common in players who try to keep the club "on plane" by consciously pushing it outside. Can also stem from an overly strong grip that causes the club to fan outward.

**Fix:** Feel that the club head stays slightly inside the hands during the takeaway. Drill: set a headcover just outside the ball on the target line; a correct takeaway should not knock it away.

## Closed clubface at toe-up (toe down)

**What it looks like:** When the shaft reaches horizontal, the toe of the club points toward the ground rather than straight up. The leading edge has rotated past vertical in a clockwise direction (for a right-handed golfer).

**Detection signal:** `shaft proxy angle` from the face-on view showing the club face rotated significantly; can be inferred from `left_shoulder` and `right_shoulder` rotation relative to the forearm position.

**Why it happens:** Excessive forearm roll or hand action during the takeaway. Common in players with very strong grips or those who have been told to "close the face" to fix a slice.

**Fix:** Check grip neutrality. During the takeaway, the back of the lead hand should face roughly downward (not skyward) when the club is at hip height. Drill: make slow-motion takeaways with eyes closed, stopping at P2 to check the toe angle in a mirror.

## Open clubface at toe-up (face skyward)

**What it looks like:** When the shaft reaches horizontal, the clubface is open — the leading edge angles away from vertical with the toe well past 12 o'clock, essentially looking upward. This is the mirror fault of the closed face.

**Detection signal:** Shaft proxy angle indicating the clubface is significantly open; often accompanies `shoulder_line_from_horizontal` showing the left shoulder higher than expected, or a steep lift rather than rotation.

**Why it happens:** Insufficient forearm rotation during takeaway, very weak grip, or a tendency to "fan" the club open in an attempt to prevent hooking.

**Fix:** Allow the forearms to rotate naturally with the body turn rather than fighting rotation. A neutral grip combined with a one-piece takeaway typically self-corrects this fault. Drill: practice toe-up position and check that the leading edge of the club is within 15° of vertical.

## Early loss of spine angle

**What it looks like:** The golfer stands up or loses their forward bend from the hips before the club reaches hip height. The upper body rises and the hips push back, producing a more upright posture than at address.

**Detection signal:** `spine_angle_from_vertical` decreasing from the P1 value by more than 8-10°; `right_hip` and `left_hip` showing the hip line tilting or rising inconsistently with a rotation pattern.

**Why it happens:** Often a reflex response to the backswing — the body straightens to create room for the arms to swing. Can stem from tight hip flexors or insufficient core stability.

**Fix:** Maintain hip flexion through the backswing. Cue: "stay in your posture" or "keep your belt buckle pointed at the ball." Drill: make half-swings with a foam pool noodle or alignment stick pressed between the back and a wall; losing spine angle breaks the contact.
