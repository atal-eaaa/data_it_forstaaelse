alder      = int(input("Hvor gammel er du? "))
studerende = input("Er du studerende (j/n)? ").lower() == "j"
ugedag     = input("Hvilken ugedag er det? ").lower()

alder      = int(alder)
studerende = studerende.lower() == 'j'
ugedag     = ugedag.lower()

if alder < 12 or alder >= 65:
    pris = 70
elif studerende == True and alder >= 18 and alder <= 30:
    pris = 90
else:
    pris = 120

if ugedag == "tirsdag":
    pris -= 20

print("Din billet koster", pris, "kr.")
