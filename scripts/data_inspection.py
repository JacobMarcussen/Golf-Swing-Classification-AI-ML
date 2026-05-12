import pandas as pd

df = pd.read_pickle('data/golfDB.pkl')

print("=" * 60)
print("FULL DATASET")
print("=" * 60)
print(f"Total clips: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print(f"\nSample row:")
print(df.iloc[0])

print("\n" + "=" * 60)
print("CATEGORICAL BREAKDOWNS")
print("=" * 60)
for col in ['club', 'view', 'sex', 'slow']:
    if col in df.columns:
        print(f"\n{col}:")
        print(df[col].value_counts())

print("\n" + "=" * 60)
print("DRIVER SUBSET")
print("=" * 60)
driver_df = df[df['club'] == 'driver'].copy()
print(f"Driver clips: {len(driver_df)}")
print(f"\nView breakdown within driver:")
print(driver_df['view'].value_counts())
print(f"\nSlow-motion breakdown within driver:")
print(driver_df['slow'].value_counts())
print(f"\nUnique players in driver subset: {driver_df['player'].nunique()}")
print(f"\nTop 10 players by clip count:")
print(driver_df['player'].value_counts().head(10))
print(f"\nClip count distribution per player:")
print(driver_df['player'].value_counts().describe())


print(f"Events array length: {len(df.iloc[0]['events'])}")
print(f"Events array: {df.iloc[0]['events']}")

# The first 8 events are at indices 1-8; index 0 is start, indices 9+ are clip end / extras
# Per the GolfDB code: events[1:9] = the 8 swing events
events = df.iloc[0]['events']
event_names = ['Address', 'Toe-up', 'Mid-backswing', 'Top',
               'Mid-downswing', 'Impact', 'Mid-followthrough', 'Finish']
print(f"\nClip start frame: {events[0]}")
print(f"Clip end frame: {events[-1] if len(events) > 9 else 'N/A'}")
print(f"\nThe 8 events:")
for name, frame in zip(event_names, events[1:9]):
    print(f"  {name}: frame {frame}")

df_driver = df[df['club'] == 'driver']
swing_lengths = df_driver['events'].apply(lambda e: e[8] - e[1])
print(f"\nSwing length (Address to Finish), in frames:")
print(swing_lengths.describe())

print(f"\nExact view labels: {df['view'].unique()}")

sample_events = df.iloc[0]['events']
print(f"Type: {type(sample_events)}")
print(f"Dtype: {sample_events.dtype if hasattr(sample_events, 'dtype') else 'N/A'}")
print(f"Element type: {type(sample_events[0])}")
print(f"Subtraction result: {sample_events[8] - sample_events[1]}, type: {type(sample_events[8] - sample_events[1])}")

# Force to int and try again
swing_lengths = df_driver['events'].apply(lambda e: int(e[8]) - int(e[1]))
print(f"\nSwing length (Address to Finish), forced to int:")
print(swing_lengths.describe())

print(df_driver.groupby('slow')['events'].apply(
    lambda col: col.apply(lambda e: int(e[8]) - int(e[1])).describe()
))