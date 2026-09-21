ok = True
while ok == True:
    tal = input("Indtast tal : ")
    try:
        tal = float(tal)
        print( "10 x ", tal, "=", 10*tal)
    except:
        ok = False
print("Tak for turen!")  

