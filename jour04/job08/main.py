L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

liste = len(L)
somme=0

for nombre in range (liste):
    if L[nombre] %2 ==0:
        somme= somme + L[i]

print (somme)


#Une boucle for parcourt tous les indices de la liste (de 0 à -1).
#La condition if L[nombre] % 2 == 0 vérifie si l'élément à l'indice actuel est pair.
#Si c'est le cas, l'élément est ajouté à la variable somme.

# exemple sup avec fonction
#L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

#def somme():
#    count = sum([nombre_pair for nombre_pair  in L if (nombre_pair  % 2 ==0)])
#    return count
#print(somme())