moms_belob = 0

belob     = input("Indtast beløb : ")
belob     = belob.replace(",", ".")


med_moms  = input("Er beløbet incl. moms? (J/N) : ")
med_moms  = med_moms.lower()


moms_belob = round(moms_belob, 2)
print("Momsen udgør : ", moms_belob, " kr.")