# ØVELSE 1
# -------------------------------------

talraekke = [2, 3, 4, 5]
total = 0
for i, tal in enumerate(talraekke):
    if i % 2 == 0:
        total += tal

print(f"Øvelse 1 : {total}")



# ØVELSE 2
# -------------------------------------

talraekke = [2, 4, 10]
x = sum(talraekke) 
x = x // 5
x = x % 2

print(f"Øvelse 2 : {x}")



# ØVELSE 3
# -------------------------------------

tal = 2
Tal = 3
for i in range(tal):
    if i == 3:
        tal = 7
        break

print(f"Øvelse 3 : {tal}")



# ØVELSE 4
# -------------------------------------

tal = 15 % 10
tal = min([tal, 6]) * ( 7 // 3 )

print(f"Øvelse 4 : {tal}")



# ØVELSE 5
# -------------------------------------
import statistics as sts
tal = max(min([4, 7, 3]), sts.mean([2, 3, 4]), sts.median([2, 5, 4]))

print(f"Øvelse 5 : {tal}")



# ØVELSE 6
# -------------------------------------

navn = 'HELSINGBORG' 
i = 0
while navn[i] > 'C':
    i += 1

print(f"Øvelse 6 : {i}")

