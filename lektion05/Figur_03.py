belob     = input("Indtast beløb : ")
belob     = float(belob) 
med_moms  = input("Er beløbet incl. moms? (J/N) : ")

if med_moms == "J" or med_moms == "j":
    moms_belob = belob * 0.2
    ex_moms_belob = belob - moms_belob
    incl_moms_belob = belob
else:
    moms_belob = belob * 0.25
    ex_moms_belob = belob
    incl_moms_belob = belob + moms_belob

print("Momsen udgør      : ", moms_belob, " kr.")
print("Beløbet uden moms : ", ex_moms_belob, " kr.")    
print("Beløbet med moms  : ", incl_moms_belob, " kr.")






