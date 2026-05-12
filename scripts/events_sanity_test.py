import cv2
import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_pickle('data/golfDB.pkl')

clip = df.iloc[357]  # SANDRA GAL clip
video_path = f'data/videos_160/{clip["id"]}.mp4'
cap = cv2.VideoCapture(video_path)

event_names = ['P1 - Address', 'P2 - Toe-up', 'P3 - Mid-backswing', 'P4 - Top',
               'P5 - Mid-downswing', 'P7 - Impact', 'P8/P9 - Mid-followthrough', 'P10 - Finish']

# Note: the event frame numbers are absolute YouTube-video frames.
# In the trimmed videos_160 clips, they're relative to clip start.
# So we need to subtract events[0] to get the index within the trimmed video.
clip_start = clip['events'][0]
event_frames = [f - clip_start for f in clip['events'][1:9]]

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
for ax, name, frame_idx in zip(axes.flatten(), event_names, event_frames):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        ax.set_title(f'{name} (frame {frame_idx})')
        ax.axis('off')
plt.tight_layout()
plt.show()