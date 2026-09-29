# OPGAVE 4:
# ---------------------------------------------------------------------
# Byg et program, der spiller Yatzy, dvs. slår med fem terninger. Lad 
# programmet fortsætte med at slå, indtil det slå Yatzy (fem ens) i ét 
# slag. Hvor mange gange skal du slå før det lykkes?


import random
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

print("Vi slog Yatzy med ", terning_1, "'ere")
print("Vi brugte", antal_slag, "slag")
