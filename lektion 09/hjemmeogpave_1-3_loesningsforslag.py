legal_answers = ['Meget tilfreds', 'Tilfreds', 'Hverken tilfreds eller utilfreds', 'Utilfreds', 'Meget utilfreds']
point_answers = [3, 1, 0, -1, -3]

responses = [
    'Tilfreds', 'Meget tilfreds', 'Tilfreds','Hverken tilfreds eller utilfreds', 'Utilfreds', 'Meget tilfreds', 
    'Tilfreds', 'Tilfreds', 'Meget utilfreds', 'Tilfreds','Meget tilfreds', 'Utilfreds', 'Tilfreds', 
    'Meget tilfreds', 'Ved ikke', 'Tilfreds','Hverken tilfreds eller utilfreds', 'Utilfreds', 'Meget tilfreds',
    'Tilfreds', 'Tilfreds', 'Meget tilfreds', 'Utilfreds', 'Tilfreds', 'Meget tilfred', 'Meget tilfreds',
    'Tilfreds', 'Hverken tilfreds eller utilfreds', 'Utilfreds', 'Meget utilfreds', 'Tilfreds','Meget tilfreds',
    '', 'Tilfreds', 'Utilfreds', 'Meget tilfreds', 'Tilfreds', 'Tilfres', 'Neutral', 'Meget tilfreds', 'Utilfreds',
    'Tilfreds', 'Hverken tilfreds eller utilfreds', 'Meget utilfreds', 'Tilfreds', 'Meget tilfreds', 'tilfreds',
    'Tilfreds','Utilfreds', 'Meget tilfreds', 'Tilfreds', 'Ja', 'Hverken tilfreds eller utilfreds', 'Utilfreds',
    'Tilfreds', 'Meget tilfreds', 'Tilfreds', 'Meget utilfreds', 'Tilfreds', 'Utilfreds', 'No response', 
    'Meget tilfreds', 'Tilfreds', 'Hverken tilfreds eller utilfreds', 'Utilfreds', 'Meget tilfreds', 'Tilfreds',
    'Tilfreds', 'N/A', 'Meget utilfreds', 'Tilfreds','Meget tilfreds','Utilfreds', 'Tilfreds', 'Vil ikke svare', 
    'Hverken tilfreds eller utilfreds', 'Tilfreds', 'Meget tilfreds', 'Utilfreds', 'Vet ikke', 'Meget tilfreds',
    'Tilfreds', 'Tilfreds', 'Utilfred', 'Meget utilfreds', 'Hverken tilfreds eller utilfreds', 'Tilfreds', 
    'Meget tilfreds', 'Utilfreds', 'OK', 'Tilfreds', 'Meget tilfreds', 'Utilfreds', 'Utilfreds', 'Sur', 
    'Meget tilfreds', 'Tilfreds', 'Hverken tilfreds eller utilfreds', 'Utilfreds', 'Meget utilfreds',
    'Hverken tilfreds eller utilfreds', 'Tilfreds', '5', 'Meget utilfreds', 'Tilfreds', 'Meget tilfreds', None,
    'Utilfreds'
]


accepted_responses = []
for respond in responses:
    if respond in legal_answers:
        accepted_responses.append(respond)

illegal_responses = len(responses) - len(accepted_responses)

print('Antal ulovlige svar (stk): ', illegal_responses)
print('Antal ulovlige svar (pct): ', round(illegal_responses / len(responses) * 100, 2), '%')

# OPGAVE 2
# .............................................

tilfredse = 0
utilfredse = 0
for respond in accepted_responses:
    if respond == 'Meget tilfreds' or respond == 'Tilfreds':
        tilfredse += 1
    elif respond == 'Utilfreds' or respond == 'Meget utilfreds':
        utilfredse += 1

print()    
print('Antal tilfredse (stk): ', tilfredse)
print('Antal utilfredse (stk): ', utilfredse)      


# OPGAVE 3
# .............................................

import statistics as sts
scores = []
for respond in accepted_responses:
    idx = legal_answers.index(respond)
    score = point_answers[idx]
    scores.append(score)

print()
print('Gennemsnitlig score: ', round(sts.mean(scores), 2))
print('Median score: ', sts.median(scores))    
print('Standardafvigelse: ', round(sts.stdev(scores), 2))
