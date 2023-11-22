def calcule(num1,operator,num2):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        if num2 !=0:
            return num1/num2
        else:
            return "Erreur:division par 0"
        
    elif operator == '%':
        if num2 !=0:
            return num1%num2
        else:
            return "operateur non valide"
        
resultat = calcule(5,'+',3)
print("voici le resultat",resultat)

resultat = calcule(45, '-', 5)
print ("le resultat est :", resultat)

resultat = calcule(5,'*',4)
print("voici le resultat:",resultat)

resultat = calcule(50,'/',10)
print("le resultat est:", resultat)



    
     