tekst = "DkeAmvTbcAsd_ltEbrRgb_cnDncEhcTsn_btNdhYvvEtb_ttGmbUhbLseDjn"
kode = ''

for i, tegn in enumerate(tekst):
    if i % 3 == 0:
        if tegn == '_':
            kode = kode + ' '
        else:
            kode = kode + tegn

print("koden er:", kode)

kode2 = ''

for tegn in tekst:
    if tegn == tegn.upper():
        if tegn == '_':
            kode2 = kode2 + ' '
        else:
            kode2 = kode2 + tegn

print(kode2)