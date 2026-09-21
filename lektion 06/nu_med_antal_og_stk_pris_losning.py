kurv     = []
stk_pris = []
kassebon = []
pris = float(input('Varens pris : '))
while pris !=0:
    pris = float(pris)
    antal = input('Antal købt :')
    antal = int(antal)
    samlet_pris = round(antal * pris, 2)
    kurv.append(antal)
    stk_pris.append(pris)
    kassebon.append(samlet_pris)
    pris = float(input('Varens pris : '))
print(stk_pris)
print(kurv)
print(kassebon)
print("Total for varer : ", round(sum(kassebon),2))

