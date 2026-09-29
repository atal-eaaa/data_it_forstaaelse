# OPGAVE 5:
# ---------------------------------------------------------------------
# Hvor mange gange skal man gennemsnitlig slå for at slå Yatzy i ét 
# slag? Udvid koden i opgave 4, så du gentager spillet 1000 gange. 
# Registrer antal brugte slag i en liste og beregn gennemsnittet, 
# minimum, maksimum median og standardafvigelse af listen.



import random
import statistics as sts
yatzy=[]

for counter in range(0, 1000):
    antal_slag = 0
    while True:
        antal_slag +=1
        terning_1 = random.randint(1,6)
        terning_2 = random.randint(1,6)
        terning_3 = random.randint(1,6)
        terning_4 = random.randint(1,6)
        terning_5 = random.randint(1,6)
        if terning_1 == terning_2 and terning_1 == terning_3 and terning_1 == terning_4 and terning_1 == terning_5:
            break
    yatzy.append(antal_slag)        


print("YATZY-statistik")
print("-------------------------------------------------------")
print('Gennemsnitligt antal slag for at slå Yatzy :', round(sts.mean(yatzy),1))
print('Median-slag for at slå Yatzy               :', sts.median(yatzy))
print('Standardafvigelse på Yatzy-slag            :', round(sts.stdev(yatzy),1))
print('Færrest antal slag for at slå Yatzy        :', min(yatzy))
print('Flest antal slag for at slå Yatzy          :', max(yatzy))
print("-------------------------------------------------------")


