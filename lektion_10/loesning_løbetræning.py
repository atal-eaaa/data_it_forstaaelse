ugedage   = ["mandag", "onsdag", "fredag", "søndag", "tirsdag",
             "torsdag", "lørdag", "mandag", "onsdag", "lørdag"]
distancer = [5.1, 5.8, 4.4, 5.6, 4.8, 4.8, 6.1, 5.1, 5.0, 5.4]            # km
tider     = [33.1, 34.0, 27.7, 32.9, 29.1, 26.3, 37.0, 32.3, 29.6, 33.4]  # minutter
hastigheder = []


for i, distance in enumerate(distancer):
    tid_timer = tider[i]/60
    hastighed = round(distance/tid_timer,2)
    hastigheder.append(hastighed)
    print(f'Tur {i+1}: {distance} km på {tider[i]} minutter. Svarende til {hastighed} km/t')


# hurtigste tur
hurtigste_tur = max(hastigheder)
hurtigste_dag = ugedage[hastigheder.index(hurtigste_tur)]

print(f"Hurtigste dag var en {hurtigste_dag}, hvor hastigheden var {hurtigste_tur} km/t")

# gennemsnit

distance_total = sum(distancer)
tid_total = sum(tider)/60
hastighed_gennemsnit = round(distance_total/tid_total,2)

print(f'Gennemsnitshastigheden var {hastighed_gennemsnit} km/t')