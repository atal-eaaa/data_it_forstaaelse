import random

hemmeligt_tal = random.randint(1, 100)
forsog = 0
while True:
    tal = input("Gæt på et tal :")
    tal = int(tal)
    forsog += 1
    if tal > hemmeligt_tal:
        print("For højt")
    elif tal < hemmeligt_tal:    
        print("For lavt")
    else:
        break
        
print("Det hemmelige tal er ", hemmeligt_tal)    
print("Du gættede tallet på ", forsog, "forsøg")