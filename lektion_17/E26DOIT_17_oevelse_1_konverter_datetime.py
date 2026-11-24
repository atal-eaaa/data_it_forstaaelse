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

df.info()
# %%
