sko_stoerrelser = []

while True:
    try:
        sko_str = input("Hvilken størrelse bruger du i sko (S for stop): ")
        if sko_str.lower() == "s":
            break
        sko_str = int(sko_str)
        sko_stoerrelser.append(sko_str)
    except:
        print("Ugyldig skostørrelse. Prøv igen!")    

gennemsnit = round(sum(sko_stoerrelser) / len(sko_stoerrelser),1)
print( "Sko-statistik")
print( "--------------------------------------")
print( "Gennemsnitlig skostørrelse : ", gennemsnit)
print( "Mindste skostørrelse       : ", min(sko_stoerrelser))
print( "Største skostørrelse       : ", max(sko_stoerrelser))
print( "--------------------------------------")
