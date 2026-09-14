belob     = input("Indtast beløb : ")
try:
    belob     = float(belob)
except:
    belob     = -1

med_moms  = input("Er beløbet incl. moms? (J/N) : ")

if belob >= 0:
    if med_moms == "J" or med_moms == "j":
        moms_belob = belob * 0.2
        ex_moms_belob = belob - moms_belob
        incl_moms_belob = belob
        ok = True
    elif med_moms == "N" or med_moms == "n":
        moms_belob = belob * 0.25
        ex_moms_belob = belob
        incl_moms_belob = belob + moms_belob
        ok = True
    else:
        ok = False
else:
    ok = False

if ok:
    print("Momsen udgør      : ", moms_belob, " kr.")
    print("Beløbet uden moms : ", ex_moms_belob, " kr.")    
    print("Beløbet med moms  : ", incl_moms_belob, " kr.")
else:
    print("Ugyldigt svar. Indtast J eller N og et beløb større end 0.")
    






