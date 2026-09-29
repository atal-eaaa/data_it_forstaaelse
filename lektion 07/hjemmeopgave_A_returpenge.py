# Skriv et program, der hjælper kassemedarbejderen med at udregne byttepenge.
# Start med at definere 2 variable, pris og betalt.
# Tjek dernæst om der er betalt nok til at dække prisen:
# - Hvis ja så skal programmet beregne og printe byttepengene. Fx "Du skal have 72 kr. tilbage"
# - Hvis nej, skal programmet beregne og printe hvor mange penge kunden mangler. Fx ”Betal venligst mere. Du mangler 28 kr.”

amount_payable = float(input("At betale : "))
amount_paid    = float(input("Betalt    : "))

if amount_payable > amount_paid:
    outstanding = amount_payable - amount_paid
    print("Du skylder ", outstanding, "kr. Betal venligst")    
elif amount_payable < amount_paid:
    refund = amount_paid - amount_payable
    print("Du skal have ", refund , "kr. retur")
else:
    print("Tak for handlen")
        
