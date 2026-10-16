
passagerliste = ['Mand', 'mand', 'Kvinde', 'KVINDE', 'mand', 'kvinde', 'barn', 'mand','kvinde', 'mand', 'Kvinde', 'Kvinde']
max_vaegt     = 1300

vaegt_passagerer = 0
for passager in passagerliste:
    if passager.lower() == 'mand':
        vaegt_passagerer += 90
    elif passager.lower() == 'kvinde':
        vaegt_passagerer += 75
    else:
        vaegt_passagerer += 40

vaegt_fragt = max_vaegt - vaegt_passagerer
print(vaegt_fragt)

