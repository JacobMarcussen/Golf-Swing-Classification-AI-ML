# Step 5 — Retrieval trace

## Query embedded

```
Coaching advice for Top swing position.
```

## Retrieved chunks

### Chunk 1 (distance 0.9096)

**Source**: `p4_top_faults.md` | section: *Overswinging (club past parallel)*

```
## Overswinging (club past parallel)

**What it looks like:** The club swings past the parallel-to-ground position at the top, sometimes reaching a nearly vertical shaft angle pointing toward the ground. The lead arm is typically well above horizontal, and the lead elbow often collapses significantly to allow the extra range.

**Detection signal:** `shaft proxy angle` indicating the club past parallel (shaft angle greater than 100° past vertical); `left_elbow` angle substantially below 150°; `left_shoulder` elevated significantly above horizontal.

**Why it happens:** Usually results from a collapsed lead arm, excessive wrist hinge, or very loose grip pressure allowing the club to slide in the fingers. Can also stem from trying to generate more power by swinging longer.

**Fix:** Firm up grip pressure (particularly the last three fingers of the lead hand) to prevent the club sliding at the top. Focus on shoulder rotation depth rather than arm swing length. Drill: make backswings stopping when the lead arm is parallel to the ground — at this point the club is typically near parallel and the position feels controlled.
```

### Chunk 2 (distance 0.9725)

**Source**: `p4_top_faults.md` | section: *Reverse spine angle (C-posture at top)*

```
## Reverse spine angle (C-posture at top)

**What it looks like:** At the top of the backswing, the upper spine has tilted toward the target rather than away from it. The trail shoulder is higher than the lead shoulder rather than lower. The spine forms a reverse C from a face-on view.

**Detection signal:** `spine_angle_from_vertical` direction reversing from address (tilting toward target side); `right_shoulder` elevated above `left_shoulder` by more than expected; `hip_line_from_horizontal` tilted inconsistently with a proper coil.

**Why it happens:** Often caused by a restricted hip turn — when the hips don't rotate, the upper body compensates by lateral tilting to create the appearance of a shoulder turn. Also common in players with tight hip flexors or a setup fault (insufficient hip flexion at address).

**Fix:** Ensure hip rotation in the backswing rather than just shoulder tilt. Drill: make slow backswings with a hand on the trail hip, feeling it rotate backward (not slide). The spine should tilt away from the target (trail shoulder lower) at the top — this is the correct lateral spine tilt for a driver.
```

### Chunk 3 (distance 1.0400)

**Source**: `p4_top_faults.md` | section: *Flying trail elbow*

```
## Flying trail elbow

**What it looks like:** At the top, the trail elbow points outward (away from the body) rather than downward. The trail arm has not folded correctly, causing the elbow to lift and the club to travel on a steep, outside plane.

**Detection signal:** `right_elbow` angle approaching or exceeding 90° in the horizontal plane rather than pointing down; `right_shoulder` position elevated and rotated inconsistently with a connected arm position.

**Why it happens:** Taking the club outside during the takeaway (P2) is the most common cause. The trail elbow rises to compensate for a club that is already too far outside the body. Some players also consciously try to keep the trail elbow high to prevent a flat swing.

**Fix:** Feel the trail elbow "pocket" — it should point roughly at the trail hip at the top. Drill: practice backswings with a headcover or glove tucked under the trail armpit; if it falls out, the trail elbow has separated from the body. This helps keep the arm connected and the elbow folding correctly.
```

