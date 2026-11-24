# %%

import pandas as pd

f = r'E26DOIT_17_parkings.csv'
f_25 = r'E26DOIT_17_parkings_sample_25.csv'
f_100k = r'E26DOIT_17_parkings_sample_100k.csv'
df = pd.read_csv(f, sep=',', encoding='utf-8-sig')
print("DONE")
# %%

df_25 = df.sample(n=25, replace=False)
df_25 = df_25.sort_values(by='time_start')
df_25.to_csv(f_25, sep=',', index=False, encoding='utf-8-sig')

# %%

df_100k = df.sample(n=100000, replace=False)
df_100k = df_100k.sort_values(by='time_start')
df_100k.to_csv(f_100k, sep=',', index=False, encoding='utf-8-sig')
print("DONE")


# %%
