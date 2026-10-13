arv = 100000
inflation = 0.023

rente = input('Forventet årlig rente-procent :')
rente = float(rente) / 100
alder = input('Din nuværende alder : ')
alder = int(alder)
pensionsalder = input('Din alder ved pensionering : ')
pensionsalder = int(pensionsalder)
faste_priser  = input('Vil du have beløbet i faste eller løbende priser (F/L)')
faste_priser   = faste_priser.upper()


aar_til_pension = pensionsalder - alder

for i in range(aar_til_pension):
    arv = arv * (1 + rente)
    if faste_priser == 'F':
        arv = arv / (1 + inflation)

print('Du kan om,', aar_til_pension, "år hæve", round(arv,2), "kr.")    


