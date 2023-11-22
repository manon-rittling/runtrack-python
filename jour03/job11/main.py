def timeToText(minutes):
    if minutes == int(minutes):
        return (f"{minutes//60:.0f} heures {minutes%60} minutes ")
    
print(timeToText(45)) 
print(timeToText(123))
       

# minutes//60: Cela représente la division entière de minutes par 60, ce qui donne le nombre d'heures. L'opérateur // effectue une division entière, en arrondissant le résultat vers le bas pour obtenir un nombre entier.
# :.0f: Cela fait partie de la syntaxe de la f-string et spécifie le formatage du nombre précédent. En l'occurrence, :.0f indique que le résultat doit être affiché sans décimales. Cela arrondit effectivement le nombre à la valeur la plus proche sans décimales.
# heures: C'est simplement une chaîne de caractères statique qui est incluse pour indiquer que la valeur précédente est en heures.
# minutes%60: Cela donne le reste de la division de minutes par 60, ce qui représente le nombre de minutes restantes après avoir pris en compte les heures. L'opérateur % est l'opérateur modulo, qui renvoie le reste de la division.
# minutes: Enfin, cela représente le nombre total de minutes non affectées à des heures entières.
