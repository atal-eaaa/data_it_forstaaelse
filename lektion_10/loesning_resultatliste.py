loebere = ["Sara", "Jonas", "Mette", "Ali", "Freja", "Oskar", "Lise", "Emil"]
tider   = [21.4, 22.1, 22.9, 24.0, 25.3, 27.8, 29.5, 31.2]


for idx, lober in enumerate(loebere):
    if idx == 0:
        print(idx+1, ':', loebere[idx], '-', tider[idx], 'min. GULD')

    elif idx == 1:
        print(idx+1, ':', loebere[idx], '-', tider[idx], 'min. SØLV')
    
    elif idx == 2:
        print(idx+1, ':', loebere[idx], '-', tider[idx], 'min. BRONZE')

    else:
        print(idx+1, ':', loebere[idx], '-', tider[idx], 'min.')


# antal kvalificerede
kval = 0

for tid in tider:
    if tid < 25:
        kval += 1

print("\nAntal kvalificerede er:", kval)

# hvem kommer ind efter Ali
ali_index = loebere.index('Ali')
efter_ali = loebere[ali_index+1]

print("Efter Ali kom:", efter_ali)