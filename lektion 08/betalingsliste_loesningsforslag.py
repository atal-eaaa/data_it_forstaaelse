
who_took     = ['Bo', 'Ali', 'Bo', 'Ib', 'Lei', 'Lei', 'Pia', 'Bo', 'Noa', 'Joe', 'Noa', 'Bo', 'Ali']
amount       = [2, 3, 1, 5, 3, 2, 1, 3, 6, 1, 1, 2, 3]
cookie_type  = ['Chokolade', 'Chokolade','Nødder','Vanilje', 'Nødder','Vanilje', 'Chokolade','Nødder', 'Vanilje','Nødder','Chokolade','Vanilje','Vanilje']

cookie_types = ['Chokolade', 'Vanilje', 'Nødder']
cookie_price = [3.00, 1.50, 2.50]


# DAN UNIT_PRICE_LIST
# -----------------------------------------------------

unit_price = []
for cookie in cookie_type:
    idx = cookie_types.index(cookie)
    price = cookie_price[idx]
    unit_price.append(price)
print(unit_price)    


# DAN TO_PAY_LIST
# -----------------------------------------------------

to_pay = []
for idx, price in enumerate(unit_price):
    total = amount[idx] * price
    to_pay.append(total)
print(to_pay)



# DAN BETALINGSLISTE
# -----------------------------------------------------

who = []
cookies = []
total_to_pay = []

for idx, name in enumerate(who_took):
    if not name in who:
        who.append(name)
        cookies.append(0)
        total_to_pay.append(0)
    
    position_in_list = who.index(name)
    cookies[position_in_list] += amount[idx]
    total_to_pay[position_in_list] += to_pay[idx]

# Print betalingsliste
for idx, name in enumerate(who):
    print(name, "har købt", cookies[idx], "cookies og skal betale", total_to_pay[idx], "kr.")
