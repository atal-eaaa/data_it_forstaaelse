# OPGAVE 2:
# ---------------------------------------------------------------------
# Byg et program, der slår 1000 gange med én terning og beregner 
# gennemsnittet, medianen og standardafvigelsen af alle slagene. 
# Udskriv gennemsnittet med én decimal, median med nul og 
# standardafvigelsen med to decimalere Hvis du kører programmet nogle 
# gange, vil du sikkert se, at medianen skifter mellem at være 3 og 4. 
# Hvordan kan det være?


import random
import statistics as sts

rolls = []
for i in range(0,1000):
    roll = random.randint(1,6)
    rolls.append(roll)

print("Gennemsnit   : ", sts.mean(rolls))
print("Median       : ", sts.median(rolls))
print("Std.afvigelse: ", sts.stdev(rolls))

