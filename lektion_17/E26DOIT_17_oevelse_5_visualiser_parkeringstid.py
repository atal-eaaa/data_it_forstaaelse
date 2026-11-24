# %% LOAD DATA

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

# %% KONVERTER TIMESTAMPS TIL DATETIME-FORMAT


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


# %% UDFYLD MISSING VALUES I TIME_END KOLONNEN

end_date = '2026-11-23 23:59:59'
end_date = pd.to_datetime(end_date, format='%Y-%m-%d %H:%M:%S')
df = df.fillna(end_date)


df.info()
# %% BEREGN PARKERINGSTIDEN

df['duration'] = (df['time_end'] - df['time_start'])
df['duration_min'] = df['duration'].dt.total_seconds()/60
df.info()

# %% DAN ET HISTOGRAM OVER PARKERINGSTIDEN

df.plot(
    kind = 'hist',
    y = 'duration_min',
    bins = 100
)

plt.show()

print(f"Gennemsnitlig parkeringstid :  {df['duration'].mean()}")
print(f"Median parkeringstid        :  {df['duration'].median()}")
print(f"Standardafvigelse           :  {df['duration'].std()}")

# %% DAN ET BOXPLOT OVER PARKERINGSTIDER FORDELT PÅ UGEDAGE
print(df.head())


# %%
df['weekday_name'] = df['time_start'].dt.day_name()
print(df.head())

# %%
df.boxplot(
    by = 'weekday_name',
    column = 'duration_min'
)

plt.show()
# %%
