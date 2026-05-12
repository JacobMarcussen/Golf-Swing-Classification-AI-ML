# P6 — Impact — Common Faults and Fixes

## Scooping (shaft lean backward at impact)

**What it looks like:** At impact, the clubhead is ahead of the hands rather than behind them — the shaft leans away from the target rather than toward it. The lead wrist is cupped (in extension), and the golfer appears to be flicking the ball upward. Shots tend to be thin, high, and lacking compression.

**Detection signal:** `shaft proxy angle` showing negative lean (away from target) at impact; `left_wrist` in extension (cupped); `left_elbow` showing increased flex, indicating the lead arm has broken down; weight often still on the trail side.

**Why it happens:** The golfer is trying to "help" the ball into the air, unaware that loft on the club does this work. A fundamental misunderstanding of ball-striking — or an attempt to compensate for a low-lofted club — drives this fault. Also caused by a late wrist release that has not been properly sequenced.

**Fix:** Understand that hitting down (or through) creates backspin, which lifts the ball. Drill: hit punch shots with the feel of the handle leading the head through impact. A training aid with a bent shaft (impact bag) provides immediate feedback when the head arrives before the hands.

## Reverse pivot weight distribution (weight on trail side at impact)

**What it looks like:** At impact, the majority of the golfer's weight remains on the trail foot rather than having transferred to the lead side. The body is leaning away from the target, often producing fat shots (hitting behind the ball) or extreme scooping.

**Detection signal:** Weight distribution showing 50%+ on trail side at impact; `spine_angle_from_vertical` tilting toward target; `left_hip` and `right_hip` positions showing insufficient lead-side shift; `hip_line_from_horizontal` tilted incorrectly.

**Why it happens:** Often the result of a reverse pivot in the backswing (weight shifted to the lead side on the way back and is now stuck there, so the golfer leans back through impact to compensate). Can also result from fear of the swing or a conscious attempt to "stay behind the ball."

**Fix:** Transfer weight onto the lead side during the downswing. Drill: make impact with the trail foot raised off the ground (step-through drill) — this forces weight onto the lead side. A step-through finish is a useful rehearsal of proper weight transfer.

## Open clubface at impact (slice delivery)

**What it looks like:** The clubface is open to the swing path at impact — the leading edge tilted away from the target. This imparts left-to-right sidespin (for a right-handed player) and produces a fade or slice depending on severity.

**Detection signal:** Clubface angle at impact deviating significantly from the swing path (greater than 3-5° open). Can be inferred from `left_wrist` showing extension at impact (cupped wrist correlates with open face); ball flight data showing significant left-to-right curvature.

**Why it happens:** A cupped lead wrist at impact is the most biomechanically common cause. Also caused by an open clubface through the backswing (P2/P3 fault) that was never corrected. Some golfers unconsciously hold the face open to prevent a hook.

**Fix:** Address lead wrist position. Bowing the lead wrist slightly at impact closes the face. Drill: make slow-motion impact positions with a mirror, checking that the lead wrist is flat or slightly bowed. A tour stick or alignment rod held against the lead wrist confirms the position.

## Closed clubface at impact (hook delivery)

**What it looks like:** The clubface is closed to the swing path at impact — the leading edge has rotated past the square position. This produces right-to-left sidespin and a draw or hook depending on severity.

**Detection signal:** Clubface angle significantly closed relative to swing path (greater than 3-5° closed); `left_wrist` in excessive flexion (bowed); trail forearm rotating over the lead forearm excessively through impact.

**Why it happens:** Excessive forearm rollover through the impact zone — the trail hand rolls over the lead hand too quickly. A closed face through the backswing (P2 fault) propagates to a closed face at impact. Also caused by a very strong grip.

**Fix:** Check grip neutrality. Feeling the "back of the lead hand facing the target" at impact is a useful cue for preventing rollover. Drill: practice impact positions holding the face square and stopping; the feel of the lead wrist not flipping over is the key sensation.

## Early extension at impact (standing up)

**What it looks like:** The golfer has lost their spine angle through the downswing and at impact is noticeably more upright than at address. The hips have thrust toward the ball rather than rotating, creating a reverse-C posture. The arms have been crowded and the club often comes from inside-low, producing blocks or hooks.

**Detection signal:** `spine_angle_from_vertical` substantially reduced from address value (standing up); `right_hip` and `left_hip` showing forward thrust toward the ball; `hip_line_from_horizontal` shifted forward; arms typically in an awkward position with the trail arm not extending properly.

**Why it happens:** A sequencing fault where the hips thrust rather than rotate, usually because the golfer has learned to "drive the hips" without rotating them. Also common when the swing plane is too flat, forcing the body to make room by standing up.

**Fix:** Rotate the hips through rather than thrusting them at the ball. Cue: "belt buckle turns to face the target, not the ball." Drill: practice downswings against a wall behind the trail hip — any thrust will contact the wall, making the fault immediately clear.
