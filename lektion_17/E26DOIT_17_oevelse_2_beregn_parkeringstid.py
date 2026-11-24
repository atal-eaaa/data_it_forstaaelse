# %%

import pandas as pd
import matplotlib.pyplot as plt


f_parking = r"E26DOIT_17_parkings_sample_100k.csv"

df_base   = pd.read_csv(
    f_parking, 
    sep=',', 
    encoding="utf-8-sig"
)
print('Data indlæst')
df_base.info()

# %%
df = df_base.copy()

df['time_start'] = pd.to_datetime(
    df['time_start'], 
    format='%Y-%m-%d %H:%M:%S.%f', 
    errors='coerce'
)

df['time_end'] = pd.to_datetime(
    df['time_end'], 
    format='%Y-%m-%d %H:%M:%S.%f', 
    errors='coerce'
)

df.info()
# %%

df['duration'] = (df['time_end'] - df['time_start'])
df['duration_minutes'] = df['duration'].dt.total_seconds()/60

print(df['duration'].mean())
print(df['duration'].sum())
print(df['duration_minutes'].mean())
print(df['duration_minutes'].sum())


# %%

df.plot(
    kind = 'hist',
    y    = 'duration_minutes',
    bins = 100
)

plt.show()
# %%

df['weekday'] = df['time_start'].dt.day_name()
print(df.head())
df.plot(
    kind='box',
    by='weekday',
    column='duration_minutes',
    figsize=(8, 5)
)
plt.show()

# %%
