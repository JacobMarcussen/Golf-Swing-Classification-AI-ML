"""
Phase 1 sanity check: extract and visualize the 8 event frames from a few clips.
Confirms the events array indexing is correct and the videos are usable.
"""
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PICKLE_PATH = 'data/golfDB.pkl'        # adjust if needed
VIDEOS_DIR = Path('data/videos_160')   # adjust if needed
N_CLIPS_TO_CHECK = 3                   # how many clips to visualize

EVENT_NAMES = ['P1 - Address', 'P2 - Toe-up', 'P3 - Mid-backswing', 'P4 - Top',
               'P5 - Mid-downswing', 'P7 - Impact', 'P8/P9 - Mid-followthrough', 'P10 - Finish']

df = pd.read_pickle(PICKLE_PATH)
df_filtered = df[
    (df['club'] == 'driver') &
    (df['view'].isin(['down-the-line', 'face-on']))
].copy().reset_index(drop=True)
print(f"Filtered dataset: {len(df_filtered)} clips")

# Pick clips from different views to make sure both work
sample_indices = []
sample_indices.extend(df_filtered[df_filtered['view'] == 'down-the-line'].head(2).index.tolist())
sample_indices.extend(df_filtered[df_filtered['view'] == 'face-on'].head(1).index.tolist())

for idx in sample_indices[:N_CLIPS_TO_CHECK]:
    clip = df_filtered.iloc[idx]
    clip_id = clip['id']
    video_path = VIDEOS_DIR / f'{clip_id}.mp4'

    if not video_path.exists():
        print(f"  MISSING: {video_path}")
        continue

    cap = cv2.VideoCapture(str(video_path))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Events array: [clip_start, e1, e2, ..., e8, clip_end]
    # The trimmed videos_160 clips start at frame 0, so subtract clip_start.
    events = clip['events']
    clip_start = int(events[0])
    event_frames_relative = [int(events[i]) - clip_start for i in range(1, 9)]

    print(f"\nClip {clip_id} | player: {clip['player']} | view: {clip['view']}")
    print(f"  Video has {total_frames} frames")
    print(f"  Event frames (relative): {event_frames_relative}")
    print(f"  Range: 0 .. {max(event_frames_relative)} (must be < {total_frames})")

    if max(event_frames_relative) >= total_frames:
        print(f"  WARNING: event frame out of range — indexing may be wrong")

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    for ax, name, frame_idx in zip(axes.flatten(), EVENT_NAMES, event_frames_relative):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            ax.text(0.5, 0.5, f'COULD NOT READ\nframe {frame_idx}',
                    ha='center', va='center', transform=ax.transAxes)
            ax.axis('off')
            continue
        ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        ax.set_title(f'{name}\n(frame {frame_idx})')
        ax.axis('off')

    fig.suptitle(f'Clip {clip_id} — {clip["player"]} ({clip["view"]})', fontsize=14)
    plt.tight_layout()
    plt.show()
    cap.release()