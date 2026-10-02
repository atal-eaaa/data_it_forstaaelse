residents    = ['Bo', 'Ea', 'Ali', 'Ib', 
                'Lei', 'Per', 'Noa', 'Pia',
                'Iben', 'Jan', 'Nia', 'Zoe']

who_took = ['Ali', 'Pia', 'Jan', 'Bo', 'Joe', 'Noa', 
            'Ib', 'Iben', 'Zoe', 'Per', 'Nia', 'Lei']

cookies_taken = [2, 1, 3, 7, 1, 2, 4, 3, 2, 3, 2, 5]


# Spørgsmål 1: Fang cookie-tyven (simpel version)
# ---------------------------------------------------------------------

for navn in who_took:
    if not navn in residents:
        print("Cookie-tyven er:", navn)



# Spørgsmål 2: Fang cookie-tyven og opgør tyveriets omfang
# ---------------------------------------------------------------------

for idx, navn in enumerate(who_took):
    if not navn in residents:
        print(navn, "stjal", cookies_taken[idx], "cookie(s)")