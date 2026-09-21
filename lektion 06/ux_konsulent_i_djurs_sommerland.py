antal_gaester = 0
score_sum = 0
while True:
    score = input("Indtast gæstens score eller 'S/s' for stop :")
    if score.lower() == "s" :
        break   
    
    try:
        score = int(score)
        ok  = (score >= 0 and score <= 10)
    except:
        ok = False    
       
    if ok == True:   
        antal_gaester += 1    
        score_sum += score
    else:
        print("Ugyldigt input, prøv igen")
 
nps = score_sum / antal_gaester
nps = round(nps, 2)
print("NPS er: ", nps)
print("Antal gæster: ", antal_gaester)