aar_lst = [2023, 2024, 2025, 2026]
tormentil = [520, 610, 860, 950]
pericon   = [810, 840, 1230, 1905]



# Spørgsmål 1: Hvilke af selskaberne vil du helst have investeret i?

tormentil_afkast = round(tormentil[3] / tormentil[0] * 100, 0)
pericon_afkast = round(pericon[3] / pericon[0] * 100, 0)

print('Afkast: ')
print('-------------------------')
print('Tormentil  :', tormentil_afkast)
print('Pericon    :', pericon_afkast)

if pericon_afkast > tormentil_afkast:
    print('Pericon er den bedste investering')
elif pericon_afkast < tormentil_afkast:
    print('Tormentil er den bedste investering')
else:
    print('Investeringerne er lige gode')
    

# Spørgmsmål 2: Hvis du havde investeret 10.000 kr i den bedste aktie, hvor meget havde du så nu?

pericon_vaerdi   = 10000 * pericon_afkast / 100
tormentil_vaerdi = 10000 * tormentil_afkast / 100
vaerdi = max( [ pericon_vaerdi, tormentil_vaerdi])

print("Værdi af min investering pr. 30. september 2026:", vaerdi)

# Spørgsmål 3: Man skal købe et helt antal aktier. Hvor mange havde du købt og hvor stor havde din investering været, og hvor meget havde du tjent?
 
tormentil_antal_aktier = int(10000/ tormentil[0])
pericon_antal_aktier = int(10000/ pericon[0])

tormentil_vaerdi_2026 = tormentil_antal_aktier * tormentil[3]
pericon_vaerdi_2026 = pericon_antal_aktier * pericon[3]

if tormentil_vaerdi_2026 > pericon_vaerdi_2026:
    print('Antal aktier købt: ', tormentil_antal_aktier)
    print('Min investering var i 2026', tormentil_vaerdi_2026, 'kr. værd')
if tormentil_vaerdi_2026 < pericon_vaerdi_2026:
    print('Antal aktier købt: ', pericon_antal_aktier)
    print('Min investering var i 2026', pericon_vaerdi_2026, 'kr. værd')
else:
    print('De var begge', pericon_vaerdi_2026, 'kr. værd')    


