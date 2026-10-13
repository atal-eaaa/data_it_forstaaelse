aar_lst = [2023, 2024, 2025, 2026]
tormentil = [520, 610, 860, 950]
pericon   = [810, 840, 1230, 1905]

vaerdi = 10000
aktie  =  []
for i, aar in enumerate(aar_lst):
    if i > 0:
        if tormentil[i] / tormentil[i-1] > (pericon[i] / pericon[i-1]):
            vaerdi = vaerdi * tormentil[i] / tormentil[i-1]
            aktie.append('Tormentil')
        else:
            vaerdi = vaerdi * pericon[i] / pericon[i-1]
            aktie.append('Pericon')

print('Bedste investeringsforløb    : ', aktie)
print('Værdi pr. 30. september 2026 :', round(vaerdi,2), "kr.")


