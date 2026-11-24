# %%

import pandas as pd

f_parking = r"E26DOIT_17_parkings_sample_25.csv"

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
df['duration_min'] = df['duration'].dt.total_seconds()/60

print(df['duration'].mean())
print(df['duration'].sum())
print(df['duration_min'].mean())
print(df['duration_min'].sum())




# %%

# INDSÆT MISSING VALUE I TIME_END KOLONNEN
# ----------------------------------------

end_date = '2026-11-23 23:59:59'
end_date = pd.to_datetime(end_date, format='%Y-%m-%d %H:%M:%S')
df = df.fillna(end_date)




print(df)


print(end_date)

# %%
