vare     = "Kaffebønner"
antal    = "3"
stk_pris = "49.95"
medlem   = True

print(type(vare))
print(type(antal))
print(type(stk_pris))
print(type(medlem))

antal    = int(antal)
stk_pris = float(stk_pris)

pris_i_alt = antal * stk_pris
if medlem == True:
    pris_i_alt = pris_i_alt * 0.9

pris_i_alt = round(pris_i_alt, 2)

print(antal, "x", vare)
print("Pris i alt:", pris_i_alt, "kr.")
