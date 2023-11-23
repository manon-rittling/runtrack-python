def multiple3(liste):
    return sum(1 for nombre in liste if nombre %3 ==0)
L=[8, 24, 48, 2, 16]
resultat=multiple3(L) #variable qui appel la fonction avec la liste spécifiée
print(resultat)


#return sum(1 for nombre in liste if nombre %3 ==0)
#À l'intérieur de la fonction, il y a une expression génératrice utilisant la fonction sum.
#Pour chaque élément nombre dans la liste, on émet un 1 si nombre est un multiple de 3 (vérifié avec nombre % 3 == 0).
#La fonction sum additionne tous les 1 émis, donnant ainsi le nombre total d'éléments qui sont des multiples de 3 dans la liste.
#La valeur résultante est renvoyée.
