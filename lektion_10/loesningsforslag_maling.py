import statistics as sts

anlaeg_A = [ 
    4.02, 3.99, 4.01, 4.00, 4.03,
    3.98, 4.01, 4.00, 3.99, 4.02,
    4.01, 3.97, 4.00, 4.02, 3.99,
    4.01, 4.00, 3.98, 4.03, 4.01
]

anlaeg_B = [
    4.12, 3.91, 4.08, 3.95, 4.04,
    4.15, 3.87, 4.06, 3.94, 4.09,
    3.89, 4.11, 4.02, 3.92, 4.13,
    3.96, 4.07, 3.88, 4.10, 3.93
]


# Spørgsmål 1: Hvor mange påfyldninger ligger inden for kvalitetskravene?

godkendt_A = 0
godkendt_B = 0

for volumen in anlaeg_A:
    if volumen >= 3.95 and volumen <= 4.05:
        godkendt_A += 1

for volumen in anlaeg_B:
    if volumen >= 3.95 and volumen <= 4.05:
        godkendt_B += 1

godkendt_A_pct = godkendt_A / len(anlaeg_A) * 100
godkendt_B_pct = godkendt_B / len(anlaeg_B) * 100

print('Godkendt A:', godkendt_A, round(godkendt_A_pct, 1), "%")
print('Godkendt B:', godkendt_B, round(godkendt_B_pct, 1), "%")

# Spørgsmål 2: Er påfyldnings-anlægene lige stabile?

if godkendt_A_pct > godkendt_B_pct:
    print("Anlæg A er mere stabilt end Anlæg B")
elif godkendt_A_pct < godkendt_B_pct:
    print("Anlæg B er mere stabilt end Anlæg A")
else:
    print("Anlægene er lige stabile")    


# Spørgsmål 3: Beregn gennemsnit, median og standardafvigelse for påfyldningen i hvert af de to anlæg.

print()
print("Anlæg A:")
print("------------------------------------------")
print('Gennemsnitlig påfyldning,', round(sts.mean(anlaeg_A), 3))
print('Median påfyldning,       ', round(sts.median(anlaeg_A), 3))
print('Standardafvigelse,       ', round(sts.stdev(anlaeg_A), 3))

print()
print("Anlæg B:")
print("------------------------------------------")
print('Gennemsnitlig påfyldning,', round(sts.mean(anlaeg_B), 3))
print('Median påfyldning,       ', round(sts.median(anlaeg_B), 3))
print('Standardafvigelse,       ', round(sts.stdev(anlaeg_B), 3))
print()