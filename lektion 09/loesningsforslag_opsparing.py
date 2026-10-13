startbeloeb = float(input('Startbeløb : '))
rente       = float(input('Rente (%)  : '))

beloeb = startbeloeb
aar    = 0

while beloeb < 2 * startbeloeb:
    aar += 1
    beloeb = beloeb + beloeb * rente / 100
    print("År", str(aar) + ":", round(beloeb, 2), "kr.")

print("Det tog", aar, "år at fordoble opsparingen.")
