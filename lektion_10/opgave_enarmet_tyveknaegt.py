import random

symbols =  ["🍒", "🍒", "🍒", "🍒", "🍋", "🍋", "🍋","⭐", "⭐", "7"]


stake_start = 20
stake = stake_start

stake -=1
combination = []
for i in range(3):
    symbol = symbols[random.randint(0,9)]
    combination.append(symbol)

if combination[0] == combination[1] and combination[0] == combination[2]:
    if combination[0] == "🍒":
        win = 8
    elif combination[0] == "🍋":
        win = 16
    elif combination[0] == "⭐":   
        win = 30
    else:
        win = 100    
else:
    win = 0
stake += win
print(f"{combination} -> du vinder {win}. Du har nu {stake} kr. at spille for")        
print(f"Tak for i dag")     
if stake >= stake_start:
    print(f"Du vandt {stake - stake_start} kr.")
else:
    print(f"Du tabte {stake_start - stake} kr.")
    