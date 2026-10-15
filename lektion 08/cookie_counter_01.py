cookie_types = ['Chokolade', 'Vanilje', 'Nødder']
price_list   = [3.50, 2.00, 1.50]

cookie = input("Hvilken slags cookie vil du købe? (Chokolade, Vanilje, Nødder): ")
idx    = cookie_types.index(cookie)
price  = price_list[idx]
print("Prisen for en", cookie, "cookie er:", price, "kr.") 

print("Tak for dit køb!")    
