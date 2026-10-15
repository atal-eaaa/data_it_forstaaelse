# Her er en liste: data = ["HEJ", -4, 12, "13", 4, "112", False, [1, 29], "N/A", -77, 0, 115]. Dan en ny
# liste med de værdier fra listen data, er tocifrede eller negative. Udskriv listen Beregn og
# udskriv summen af listen


mylist = ["HEJ", -4, 12, "13", 4, "112", False, [1, 29], "N/A", -77, 0, 115]
newlist = []

for x in mylist:

    try:
        x = int(x)
        if x < 0:
            newlist.append(x)
        elif x > 9 and x < 100:
            newlist.append(x)
    except:
        pass


print(newlist)