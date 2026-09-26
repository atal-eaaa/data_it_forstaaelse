# Opgave B
# Du skal spare 2000 kr. op til en gave og kan lægge 200 kr. fra hver uge. Din startsaldo (i #uge=0) er 500 kr.
# Skriv et while-loop, der lægger 200 kr. til saldo for hver uge, og printer saldoen efter hver uge, fx: "Uge 1: 700 kr."
# Når loopet er færdigt, skal programmet printe: "Du har nu sparet nok op!

opsparing = 500
uge_nr    = 0
while opsparing < 2000:
    uge_nr +=1
    opsparing += 200
    print("Uge", uge_nr, ": Du har nu opsparet", opsparing, "kr.")

print("Du har nu sparet nok op til at kunne købe gaven")    


