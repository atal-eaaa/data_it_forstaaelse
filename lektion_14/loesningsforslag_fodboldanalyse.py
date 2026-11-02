# %%

import pandas as pd
import matplotlib.pyplot as plt


f_fixtures = r"fixtures.csv"
f_market_values = r"all_leagues.csv"

df_mval = pd.read_csv(f_market_values, sep=',', encoding='utf-8-sig')


# %%

# STEP 1: Få styr på fixtures.csv
# ---------------------------------------


df_fixt = pd.read_csv(f_fixtures, sep=',', encoding='utf-8-sig')


df_fixt.info()
print(df_fixt.describe())

df_fixt.loc[df_fixt['tier'] == 'b1', 'tier'] = 'B1'
df_fixt.loc[df_fixt['tier'] == 'b2', 'tier'] = 'B2'

print(df_fixt['tier'].value_counts())

# %%

# STEP 2: Dan kolonne med points pr. kamp
# ---------------------------------------

df_fixt['points'] = 1
df_fixt.loc[(df_fixt['own_goals_full_time'] > df_fixt['opponent_goals_full_time']), 'points'] = 3
df_fixt.loc[(df_fixt['own_goals_full_time'] < df_fixt['opponent_goals_full_time']), 'points'] = 0

print(df_fixt.head())


# %%

# STEP 3: Aggreger data
# ---------------------------------------

df_agg = df_fixt.groupby(['season', 'own_team'])[['own_goals_full_time', 'opponent_goals_full_time', 'points' ]].sum().reset_index()
print(df_agg.head(10))

# %%

# STEP 4: kombiner data
# ---------------------------------------


df_merge = pd.merge(df_mval, df_agg, left_on=['season', 'club_std_name'], right_on=['season', 'own_team'], how='left')
df_merge = df_merge.drop(columns=['club', 'own_team'])
df_merge = df_merge.rename( columns = { 'club_std_name' : 'club'}) 

print(df_merge.head())

# %%


print(df_merge['season'].dtype)
print(df_merge['season'].unique())
print(len(df_merge))
# df_merge=df_merge[df_merge['season'] > '2024/25']

print(len(df_merge))
      



# %% 
# STEP 5: Overvej
# ---------------------------------------

# Ikke en kodeopgave



# STEP 6: Visualisering
# ---------------------------------------

tiers = ['PL', 'LL', 'B1', 'LC', 'SA']
df_plt = df_merge[df_merge['tier'].isin(tiers) ]
df_plt= df_plt[df_plt['season'] == '2025/26'] 
df_plt.plot(
    kind='scatter',
    x = 'total_market_value',
    y = 'points'
)
plt.show()

# %%
