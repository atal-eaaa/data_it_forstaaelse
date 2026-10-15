# Her er liste med salg inklusiv moms. Dan en liste med salget eksklusiv moms samt en liste med
# momsen: salg = [ 123.90, 212.10, 87.95, 99.90, 117.15, 92.95, 21.00, 345.00]. Udskriv listerne.
# Du bør kunne kopiere den viste listen til over i VSC med cut ‘n paste

pris_m_moms = [ 123.90, 212.10, 87.95, 99.90, 117.15, 92.95, 21.00, 345.00]

pris_u_moms = []

moms = []

for pris in pris_m_moms:
    pris_u_moms.append(0.8*pris)
    moms.append(0.2*pris)

print(pris_u_moms)
print(moms)

