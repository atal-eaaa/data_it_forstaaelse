import random

roulette_colors = ["Grøn", "Rød", "Sort", "Rød", "Sort", "Rød", "Sort", 
                   "Rød", "Sort", "Rød", "Sort", "Sort", "Rød", "Sort", 
                   "Rød", "Sort", "Rød", "Sort", "Rød", "Rød", "Sort", 
                   "Rød", "Sort", "Rød", "Sort", "Rød", "Sort", "Rød", 
                   "Sort", "Sort", "Rød", "Sort", "Rød", "Sort", "Rød", 
                   "Sort", "Rød"]


# generer vinder-tallet 
idx = random.randint(0,36)



print("Vindertallet er:", idx)
print("Farven er:", roulette_colors[idx])

if idx != 0:
    if idx % 2 == 0:
        print("Lige")
    else:
        print("Ulige")
 
    if idx <= 18:
        print("Lav")
    else: 
        print("Høj")



answer = ['1','2','3','4','S']

while True:
    bet_type = input("What type of bet do you want to make. Press '1: red/black', '2: even/odd', '3: high/low', '4: specific number', 'S' for stop: ")


    if bet_type in answer:
        if bet_type == 'S':
            break
        elif bet_type == '1':
            guess = input("red/black?: ")
            odds = 1.98
        elif bet_type == '2':
            guess = input("even/odd?: ")
            odds = 1.98
        elif bet_type == '3':
            guess = input("high/low?: ")
            odds = 1.98
        elif bet_type == '4':
            guess = input("what number?: ")
            odds = 49

    else:
        pass # go again