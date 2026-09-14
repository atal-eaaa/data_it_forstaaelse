belob     = input("Indtast beløb : ")
belob     = float(belob) 
med_moms  = input("Er beløbet incl. moms? (J/N) : ")

if med_moms == "J":
    moms_belob = belob * 0.2
else:
    moms_belob = belob * 0.25

print("Momsen udgør : ", moms_belob, " kr.")





belob     = belob.replace(",", ".")
