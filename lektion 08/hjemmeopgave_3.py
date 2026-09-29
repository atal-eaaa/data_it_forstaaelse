# OPGAVE 3:
# ---------------------------------------------------------------------
# Her er en liste: 
# data = ["HEJ", -4, 12, "13", 4, "112", False, [1, 29], "N/A", -77, 0, 115]. 
# Dan en ny liste med de værdier fra listen data,  er tocifrede eller 
# negative. Udskriv listen, beregn og udskriv summen af listen.



data = ["HEJ", -4, 12, "13", 4, "112", False, [1, 29], "N/A", -77, 0, 115]
ny_liste  = []
for vaerdi in data:
    try:
        vaerdi = int(vaerdi)
        if (vaerdi >= 10 and vaerdi <= 99) or vaerdi < 0:
            ny_liste.append(vaerdi)
    except:
        pass

print(ny_liste)
print(sum(ny_liste))       