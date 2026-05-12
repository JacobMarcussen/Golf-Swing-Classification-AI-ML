# P8 — Finish — Common Faults and Fixes

## Falling backward (weight on trail side at finish)

**What it looks like:** At the finish, the golfer's weight remains on or falls back toward the trail foot rather than being fully committed to the lead side. The golfer may physically step backward to maintain balance, or lean noticeably away from the target. The overall posture looks like a reverse C or a lean away from the target.

**Detection signal:** Weight distribution showing trail-side loading at P8; `spine_angle_from_vertical` tilting toward the target rather than upright; `right_hip` and `left_hip` positions indicating insufficient forward transfer; `left_knee` not bearing the body weight.

**Why it happens:** A reverse pivot in the backswing (weight staying on the lead side) causes the golfer to fall backward through impact to compensate. Also caused by early extension, where the hips thrust toward the ball and the upper body leans back. Hitting "up" on the ball with a driver can also produce this if taken too far.

**Fix:** Commit to a full weight transfer to the lead side during the downswing. Drill: make swings where the trail foot lifts completely off the ground at the finish (step-through drill). If balance cannot be maintained on one leg, the weight transfer timing needs work.

## Short or low finish (incomplete followthrough)

**What it looks like:** The club stops significantly below the standard finish position — often around shoulder height or even lower — rather than wrapping high behind the lead shoulder. The body rotation is incomplete and the golfer looks "stuck" or stalled in the throughswing.

**Detection signal:** `shaft proxy angle` at P8 indicating the club has not reached its typical resting position; `shoulder_line_from_horizontal` showing less rotation than expected; `hip_line_from_horizontal` similarly under-rotated; `left_elbow` may be lower than expected.

**Why it happens:** Deceleration through the impact zone is the primary cause — the golfer subconsciously brakes rather than swinging through. Common in players who are focused on "controlling" the shot or who are anxious about direction. Also common when the arms are doing all the work and the body has stopped contributing.

**Fix:** Think of the target, not the ball. The swing should feel like it is aimed at the finish position, not at the ball. Drill: make practice swings with no ball, focusing entirely on reaching a high, balanced finish. Then replicate this feeling with a ball.

## Loss of balance at finish (falling sideways or forward)

**What it looks like:** The golfer loses postural control at or after impact, stumbling forward, sideways, or twisting awkwardly to maintain balance. The finish position cannot be held for more than a split second.

**Detection signal:** Significant changes in `left_hip`, `right_hip`, or `spine_angle_from_vertical` outside the normal ranges, with erratic movement patterns; difficulty detecting a stable P8 position in video analysis because the body continues moving chaotically after the swing.

**Why it happens:** The swing has generated more rotational speed than the golfer's balance and core stability can control. This can stem from overswinging, a poor athletic base at address (too wide or too narrow a stance, heel-heavy weight distribution), or trying to swing too hard.

**Fix:** Widen the athletic base and ensure address weight is on the balls of the feet. Practice controlled swings at 70-80% speed until balance is consistently achieved at the finish. Drill: make slow-motion swings with the conscious goal of holding the finish position for three full seconds — any instability is immediately apparent.

## Incomplete hip rotation (hips not facing target)

**What it looks like:** At the finish, the hips are still significantly angled — not yet facing the target. The belt buckle points to the right of the target (for a right-handed player) rather than at or past it. This indicates the lower body stalled before completing its rotation.

**Detection signal:** `hip_line_from_horizontal` and the rotational values of `left_hip` and `right_hip` showing less than 70-80° of rotation from address; `shoulder_line_from_horizontal` may be more open than the hips at finish, indicating the shoulders spun while the hips stalled.

**Why it happens:** Body stalling after impact — the hips rotated to clear for impact but didn't continue through. Often caused by a golfer who uses the hips reactively rather than actively driving them through the entire swing.

**Fix:** Drive the hips all the way through to face the target. Cue: "turn your back pocket to the target." Drill: make swings where the first thing checked in the finish is that the belt buckle faces the target. If it doesn't, the golfer practiced another repetition of incomplete rotation.

## Arms-only finish (body not rotated, only arms swung)

**What it looks like:** The body is barely rotated at the finish — the golfer's chest still faces roughly toward the ball position — while the arms have swung up to a finish position. The club may be relatively high behind the head, but the torso and hips have contributed little. The overall appearance is of the arms dragging the club around a static body.

**Detection signal:** `shoulder_line_from_horizontal` and `hip_line_from_horizontal` showing far less rotation than expected at P8; `spine_angle_from_vertical` remaining close to the address value (body barely moved); weight distribution still relatively balanced rather than fully committed to the lead side.

**Why it happens:** The golfer has learned to swing with the arms rather than the body — a common beginner pattern. Sometimes caused by overthinking alignment or swing positions mid-swing, which freezes the body. Also stems from a setup that restricts rotation (excessively closed stance, feet too close together).

**Fix:** Turn the body first, arms second. Cue: "lead with your chest, not your hands." Drill: practice making full turns with just the torso (no club), then add the arms as secondary movers. The body rotation should feel like it carries the arms around, not that the arms are swinging independently.
