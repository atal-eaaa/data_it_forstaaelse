foreign_amount = input('Hvor meget vil du veksle?')
foreign_amount = float(foreign_amount)
currency    = input("Dollars eller Euro (D/E)")

if currency.upper() == "D":
    exchange_rate = 6.5
else:
    exchange_rate = 7.35

dkk_amount  = foreign_amount * exchange_rate

if dkk_amount * 0.01 > 30:
    fee = dkk_amount * 0.01
else:
    fee = 30

dkk_amount -= fee

print('Udbetalt i DKK :', dkk_amount)
print('Veksel-gebyr   :', fee)