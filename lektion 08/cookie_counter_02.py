cookie_types = ['Chokolade', 'Vanilje', 'Nødder']
price_list   = [3.50, 2.00, 1.50]

cookie_types.append('Kardemomme')
price_list.append(2.50)

while True:
    cookie = input("Hvilken slags cookie vil du købe? (S for stop): ")
    if cookie == "S":
        break
    if cookie in cookie_types:
        idx    = cookie_types.index(cookie)
        price  = price_list[idx]
        print("Prisen for en", cookie, "cookie er:", price, "kr.") 
    else:
        print("Beklager - vi har ikke den slags cookie. Prøv igen.")

print("Tak for dit køb!")    
