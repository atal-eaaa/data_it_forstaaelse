residents    = ['Bo', 'Ea', 'Ali', 'Ib', 'Lei', 'Per', 'Noa', 'Pia']
cookie_types = ['Chokolade', 'Vanilje', 'Nødder']
cookie_price = [3.00, 1.50, 2.50]

who_took     = ['Bo', 'Ali', 'Bo', 'Ib', 'Lei', 'Lei', 'Pia', 'Bo', 'Noa', 'Joe', 'Noa', 'Bo', 'Ali']
amount       = [2, 3, 1, 5, 3, 2, 1, 3, 6, 1, 1, 2, 3]
cookie_type  = ['Chokolade', 'Chokolade','Nødder','Vanilje', 'Nødder','Vanilje', 'Chokolade','Nødder', 'Vanilje','Nødder','Chokolade','Vanilje','Vanilje']




unit_price = []
to_pay = []

for idx, cookie in enumerate(cookie_type):
    price = cookie_price[cookie_types.index(cookie)]
    unit_price.append(price)
    to_pay.append(price*amount[idx])

############################

skyldnere = []
total = []
ncookies_total = []

for idx,name in enumerate(who_took):
    if name not in skyldnere:
        skyldnere.append(name)
        total.append(to_pay[idx])
        ncookies_total.append(amount[idx])
    else:
        recurrent_guest_idx = skyldnere.index(name)
        total[recurrent_guest_idx] += to_pay[idx]
        ncookies_total[recurrent_guest_idx] += amount[idx]

print(skyldnere, total, ncookies_total)