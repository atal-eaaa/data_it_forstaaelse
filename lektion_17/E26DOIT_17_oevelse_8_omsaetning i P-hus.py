# %%

# IMPORTER DATA

import pandas as pd
import matplotlib.pyplot as plt

f_cust = r"E26DOIT_17_customers.csv"
f_park = r"E26DOIT_17_parkings.csv"

df_park = pd.read_csv(f_park, sep=',', encoding='utf-8-sig')
df_cust = pd.read_csv(f_cust, sep=',', encoding='utf-8-sig')

#%%
# ERSTAT MANLGENDE VÆRDIER I date_termination MED EN SELVVALGT SLUTDATO. 
# KONVERTER DATOER OG TIMESTAMPS TIL pd.datetime()

end_date_analysis = '2026-11-30'
df_cust['date_termination'] = df_cust['date_termination'].fillna(end_date_analysis)


df_park['time_start'] = pd.to_datetime(
    df_park['time_start'], 
    format='%Y-%m-%d %H:%M:%S.%f', 
    errors='coerce'
)


df_park['time_end'] = pd.to_datetime(
    df_park['time_end'], 
    format='%Y-%m-%d %H:%M:%S.%f', 
    errors='coerce'
)


df_cust['date_sign_up'] = pd.to_datetime(
    df_cust['date_sign_up'], 
    format='%Y-%m-%d', 
    errors='coerce'
)


df_cust['date_termination'] = pd.to_datetime(
    df_cust['date_termination'], 
    format='%Y-%m-%d', 
    errors='coerce'
)

df_park.info()
df_cust.info()
print('Timestamps konvteretet')




# %%

# MERGE DE TO DATASÆT OG BEREGN KOLONNE duration_parking.

df_base                     = pd.merge(df_park, df_cust, left_on="license_plate", right_on="License_plate", how='left' )
df_base                     = df_base.drop( columns = "License_plate" )
df_base['duration_parking'] = ((df_base['time_end'] - df_base['time_start']).dt.total_seconds() // 60).astype('Int64')
df_base.info()

# %%

#end_date = '2026-11-30'
# end_date = pd.to_datetime(end_date, format = '%Y-%m-%d')

# %%

# OMSÆTNING HELE PERIODEN - EN SIMPEL LØSNING

df_pay_per_use      = df_base[df_base['type'].isna()]
total_hours         = df_pay_per_use['duration_parking'].sum() / 60
revenue_pay_per_use = (total_hours * 20).round(2)

df_post_paid        = df_base[df_base['type'] == 'post_paid']
total_hours         = df_pay_per_use['duration_parking'].sum() / 60
revenue_post_paid   = (total_hours * 20 * 0.91).round(2)


# %%

# På abonnementskunder vælger jeg at tælle dage, abonnementskunden har været hos parkeringshuset.
# Jeg antager, at når en måned koster 900 kr., koster en dag 900 / 30 = 30 kr!. Jeg bruger nu 
# customer-tabellen!

df_subscription     = df_cust[df_cust['type'] == 'subscription']
df_subscription['duration'] = (df_subscription['date_termination'] - df_subscription['date_sign_up']).dt.days.astype('Int64')

days_total = df_subscription['duration'].sum()
revenue_subscriptions = round(days_total * 900 / 30, 0)

print(f'Revenue Subscriptions    : {revenue_subscriptions}')
print(f'Revenue Post Paid        : {revenue_post_paid}')
print(f'Revenue Pay per Use      : {revenue_pay_per_use}')
print(f'Revenue Total            : {revenue_subscriptions+revenue_post_paid+revenue_pay_per_use}')



# %%
