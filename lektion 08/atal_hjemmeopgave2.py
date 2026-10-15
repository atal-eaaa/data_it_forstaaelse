# #############################################################

# # Byg et program, der slår 1000 gange med én terning og beregner gennemsnittet, medianen og
# # standardafvigelsen af alle slagene. Udskriv gennemsnittet med én decimal, median med nul og
# # standardafvigelsen med to decimaler. Hvis du kører programmet nogle gange, vil du sikkert se,
# # at medianen skifter mellem at være 3 og 4. Hvordan kan det være?

# import random 
# import statistics as sts

# terningslag = []

# for i in range(0,1000):
#     terningslag.append(random.randint(1,6))

# print("Mean:", round(sts.mean(terningslag),1), "\nMedian:", sts.median(terningslag), "\nStd.deviation:", round(sts.stdev(terningslag),2))


import random 
import statistics as sts

mine_terninge_slag = []

for i in range(1000):
    x = random.randint(1,6)
    mine_terninge_slag.append(x)

# print(mine_terninge_slag)

print("gennemsnitsværdien er:", round(sts.mean(mine_terninge_slag),1))
