import random

over_8 = 0
for sample in range(1000):
    plat = 0
    for toss in range(10):
        # Vi definerer 0 som plat og 1 som krone
        result = random.randint(0, 1)
        if result == 0:
            plat += 1    
    if plat >= 8:
        over_8 += 1
    print(plat)
print("Antal gange, vi  8 eller flere plat ud af 10 kast i 1000 forsøg: ", over_8)
print("Sandsynligheden for at få flere end 8 plat i 10 kast: ", over_8 / 1000 * 100, "%")