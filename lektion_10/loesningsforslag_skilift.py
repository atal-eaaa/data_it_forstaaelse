queue = ['M', 'F', 'C', 'C', 'M', 'M', 'C', 'F', 'M', 'M', 'F', 'C', 'C', 'F', 'M', 'M', 'M', 'C', 'M', 'M', 
         'F', 'F', 'M', 'F', 'C', 'C', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'C', 'F', 'F', 'M', 'M', 'F', 'F']

passengers   = 0
weight_total = 0
while passengers < 12 and weight_total < 850: 
    if queue[passengers] == 'M':
        weight_total += 97
    elif queue[passengers] == 'F':
        weight_total += 81
    else:
        weight_total += 50
    passengers += 1



print('Antal passagerer: ', passengers) 
print('Passagervægt    : ', weight_total)