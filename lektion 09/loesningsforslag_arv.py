arv = 100000

rente = input('Forventet årlig rente-procent :')
rente = float(rente) / 100

alder = input('Din nuværende alder : ')
alder = int(alder)

pensionsalder = input('Din alder ved pensionering : ')
pensionsalder = int(pensionsalder)

aar_til_pension = pensionsalder - alder

for i in range(aar_til_pension):
    arv = arv * (1 + rente)

print('Du kan om,', aar_til_pension, "år hæve", round(arv,2), "kr.")    


