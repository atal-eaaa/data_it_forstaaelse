residents    = ['Bo', 'Ea', 'Ali', 'Ib', 
                'Lei', 'Per', 'Noa', 'Pia',
                'Iben', 'Jan', 'Nia', 'Zoe']

who_took = ['Ali', 'Pia', 'Jan', 'Bo', 'Joe', 'Noa', 
            'Ib', 'Iben', 'Zoe', 'Per', 'Nia', 'Lei']

cookies_taken = [2, 1, 3, 7, 1, 2, 4, 3, 2, 3, 2, 5]



for idx, name in enumerate(who_took):
    if name not in residents:
        ncookies = cookies_taken[idx]

        print(name, "has stolen", ncookies, "cookie(s)")