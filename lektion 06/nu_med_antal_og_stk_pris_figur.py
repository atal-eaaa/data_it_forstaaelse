def Input():
    pass
def Sum():
    pass

kurv     = []
stk_pris = []
kassebon = []
pris = float(Input('Varens pris : '))
while pris !=0:
    antal = Input('Antal købt :')
    
    # Her skal du selv lave noget kode

    stk_pris.append(pris)
    pris = float(input('Varens pris : '))

# Her skal du selv lave noget kode
print("Total for varer : ", Sum(kassebon))

