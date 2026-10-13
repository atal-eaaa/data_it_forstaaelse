maalinger = [450, 520, 610, 740, 880, 1020, 1150, 990, 760, 1210]
graense   = 1000

i = 0
while i < len(maalinger) and maalinger[i] <= graense:
    i += 1

if i < len(maalinger):
    print("Grænsen blev overskredet ved index", i, "(" + str(maalinger[i]) + " ppm)")

    minutter = i * 10
    time     = 8 + minutter // 60
    minut    = minutter % 60

    time_tekst  = str(time)
    minut_tekst = str(minut)
    if time < 10:
        time_tekst = "0" + time_tekst
    if minut < 10:
        minut_tekst = "0" + minut_tekst
    print("Klokken var", time_tekst + ":" + minut_tekst)
else:
    print("Luften var OK hele dagen")
