# OPGAVE 5: Lagerstatus (løsningsforslag)

varer       = ["Mus", "Tastatur", "Skærm", "USB-kabel", "Headset", "Webcam"]
paa_lager   = [42, 3, 7, 150, 0, 12]

minimum = 10
bestil  = []

for i in range(len(varer)):
    print(varer[i] + ":", paa_lager[i], "stk.")
    if paa_lager[i] == 0:
        print("  -> UDSOLGT")
        bestil.append(varer[i])
    elif paa_lager[i] < minimum:
        print("  -> Skal genbestilles")
        bestil.append(varer[i])

print("Varer der skal bestilles:", bestil)
