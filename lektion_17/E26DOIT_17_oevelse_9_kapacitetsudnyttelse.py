# %%

# Data loades og de to konlonner med timestamps konverteres til 
# pd.datetime format.

import pandas as pd

f = r"E26DOIT_17_parkings.csv"

df_total = pd.read_csv(f, sep=',', encoding='utf-8-sig')

df_total['time_start'] = pd.to_datetime(
    df_total['time_start'], 
    format='%Y-%m-%d %H:%M:%S.%f', 
    errors='coerce'
)

df_total['time_end'] = pd.to_datetime(
    df_total['time_end'], 
    format='%Y-%m-%d %H:%M:%S.%f', 
    errors='coerce'
)

print('Loaded og datetimes konverteret')

# %%


# Alle parkeringer i 20 filtreres ud i en ny datframe

dfw = df_total[df_total['time_start'].dt.isocalendar().week == 20 ]

# Her findes første dato i uge 20, idet første dato må være mindste dato.
# Klokkeslættet på timestampet "smides væk" med normalize(). Jeg har nu et 
# timestamp, der giver mig første dag i ugen kl. 00:00. Dette er tidspunktet
# for starten af min analyse.
hour_start = dfw['time_start'].dt.normalize().min()

# Jeg laver nu et andet timestamp, som ligger en præcis en time efter hour_start.
# pd.Timedelta er en funktion, hvor jeg kan lægge et tidsrum til et timestamp.
# Nu har jeg to timestamps: Et der markerer starten af den første time og et, der
# markerer slutningen af den første time i ugen.

hour_end = hour_start + pd.Timedelta(hours=1)
    
# Der er 7 x 24 = 168 timer i en uge. Jeg skal med andre ord finde antallet af 
# biler for hver af disse timer - 168 gange. Jeg danner to tomme lister. Den 
# første skal indeholde antallet af optalte biler time-for-time. Den anden skal 
# indeholde times nummer i rækken, dvs. 0 til 167.
count_cars   = []
hour_of_week = []

# Jeg looper 168 gange og danner i hvert loop et subset af alle de biler, der
# var parkeret i den pågældende time. Hver bil fylder en række i subsettet, så
# antallet af biler må svare til antallet af rækker. Derfor bruger jeg len()
# Jeg appender antallet af biler til listen count_cars og timenummeret (0-167)
# appendes til listen hour_of_week. Så tæller jeg hour_start og hour_end een 
# time frem, så de nu markerer start og slut på den næste time. Jeg looper igen 
# og fortsætter til jeg har loopet 168 gange.

for i in range(168):
    df_cars = dfw[(dfw['time_start'] <= hour_start) & (dfw['time_end'] >= hour_end)]
    count_cars.append(len(df_cars))
    hour_of_week.append(i)
    hour_start += pd.Timedelta(hours=1)
    hour_end += pd.Timedelta(hours=1)
    
print("Done")
# %%

# Nu har jeg to lister, som jeg kan anvendes som x- og y-aksen i et søjlediagram
# Jeg laver det meget primitivt og udskriver det. I visualiseringen ser jeg, at
# at parkeringskælderen peaker ved 1500 biler i "travl time". Der er altså fortsat
# tomme parkeringspladser. Fredag, lørdag og søndag er ikke nær så velbesøgte som
# ugens første fire dage

import matplotlib.pyplot as plt

plt.bar(x = hour_of_week, height = count_cars)
plt.show()


# %%
