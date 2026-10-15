# Hvor mange gange skal man gennemsnitlig slå for at slå Yatzy i ét slag? Udvid koden i opgave
# 4, så du gentager spillet 1000 gange. Registrer antal brugte slag i en liste og beregn
# gennemsnittet, minimum, maksimum median og standardafvigelse af listen.
import random
import statistics as sts

ntimes = []


for i in range(1000):
    n = 0

    while True:
        terningslag = []
        for i in range(5):
            n += 1
            terningslag.append(random.randint(1,6))


        if terningslag[0]==terningslag[1]==terningslag[2]==terningslag[3]==terningslag[4]:
            #print("vindende slag:", terningslag)
            #print("det tog kun", n, "gange")
            ntimes.append(n)
            if n < 20:
                print(n, terningslag)
            break
        else: 
            pass

print("Mean:", round(sts.mean(ntimes),1), "\nMedian:", sts.median(ntimes), "\nStd.deviation:", round(sts.stdev(ntimes),2), "\nMax:", max(ntimes), "\nMin:", min(ntimes))
