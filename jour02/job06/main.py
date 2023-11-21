for i in range (2,1001): #iterer sur les nombres de 2 a 1000
    if i > 1: #verifie si i est superieur a 1 (les nbres premiers sont >1)
        for n in range (2, i): # verifier les diviseurs de 2 a i-1
            if (i % n) == 0: # si i est divisible par n  
                break # i n'est pas premier donc on sort de la boucle
        else:
            print(i)