total_belob = 0
flere_varer = 'J'
while flere_varer == 'J' or flere_varer == 'j':
    pris = input("Indtast prisen på varen: ")
    pris = float(pris)
    total_belob += pris
    flere_varer = input("Vil du indtaste en anden vare? (J/N): ")
    
print("Det totale beløb er: ", total_belob)

