# OPGAVE 1:
# ---------------------------------------------------------------------
# Her er liste med salg inklusiv moms. Dan en liste med salget 
# eksklusiv moms samt en liste med momsen: 
# salg = [ 123.90, 212.10, 87.95, 99.90, 117.15, 92.95, 21.00, 345.00].
# Udskriv listerne. Du bør kunne kopiere den viste listen til over i
# VSC med cut ‘n paste.


salg     = [ 123.90, 212.10, 87.95, 99.90, 117.15, 92.95, 21.00, 345.00]
ex_moms  = []
moms     = []
for belob in salg:
    ex_moms.append(belob * 0.8)
    moms.append(belob * 0.2)

print("Salg ex. moms", ex_moms)    
print("moms", moms)    

