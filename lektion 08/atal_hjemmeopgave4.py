import random



n = 0
while True:
    terningslag = []
    for i in range(5):
        n += 1
        terningslag.append(random.randint(1,6))


    if terningslag[0]==terningslag[1]==terningslag[2]==terningslag[3]==terningslag[4]:
        print("vindende slag:", terningslag)
        print("det tog kun", n, "gange")
        break
    else: 
        pass