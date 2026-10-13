roulette_colors = ["Grøn", "Rød", "Sort", "Rød", "Sort", "Rød", "Sort", 
                   "Rød", "Sort", "Rød", "Sort", "Sort", "Rød", "Sort", 
                   "Rød", "Sort", "Rød", "Sort", "Rød", "Rød", "Sort", 
                   "Rød", "Sort", "Rød", "Sort", "Rød", "Sort", "Rød", 
                   "Sort", "Sort", "Rød", "Sort", "Rød", "Sort", "Rød", 
                   "Sort", "Rød"]

import random



winner_number = random.randint(0,36)

print()
print('Vindere :')
print('-----------------------------------------')
print('Vindertallet er : ', winner_number)

if winner_number != 0:
    if (winner_number / 2 == int(winner_number) / 2):
        print('Lige vinder')
    else:
        print('Ulige vinder')

if winner_number > 0 and winner_number <= 18:
    print('Lav vinder')        
elif winner_number > 18:
    print('Høj vinder')

if roulette_colors[winner_number] != 'Green':
    print(roulette_colors[winner_number], "vinder")

print('-----------------------------------------')
