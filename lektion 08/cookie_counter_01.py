cookie_types = ['Chokolade', 'Vanilje', 'Nødder']
price_list   = [3.50, 2.00, 1.50]


while True:
    cookie = input("Hvilken slags cookie vil du købe? (Chokolade, Vanilje, Nødder): ")

    if cookie in cookie_types:
        idx    = cookie_types.index(cookie)
        price  = price_list[idx]
        print("Prisen for en", cookie, "cookie er:", price, "kr.")

        isdone = input("Er du færdig (yay/nay): ")
        if isdone == 'yay':
            break





 

print("Tak for dit køb!")    
