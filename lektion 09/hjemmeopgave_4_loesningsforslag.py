medlem_navn = ['Alice Olsen', 'Bob Hansen', 'Charlie Dean', 'Diana Ross', 'Eva Larsen']
medlemsnummer = [1001, 1002, 1003, 1004, 1005]
telefonnummer = ['+45 12345678', '+45 23456789', '+45 34567890', '+45 45678901', '+45 56789012']

for idx, navn in enumerate(medlem_navn):
    print( medlemsnummer[idx], navn, telefonnummer[idx] )