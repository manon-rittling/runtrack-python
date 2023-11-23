
# Liste donnée
L = [7,22,12,4,45,32,25]

# Fonction pour calculer la longueur de la liste sans utiliser la fonction système len()
def longueur(liste):
    compteur = 0
    for nombre in liste:
        compteur += 1
    return compteur

# Fonction pour trier la liste dans l'ordre croissant sans utiliser une fonction système
def trier(liste):
    echange = True #echange effectué
    while echange:
        echange = False #on passe l'echange en faux 
        index = 1 #commence a l'index 1 pour qu'il puisse comparé avec l'index0
        while index < longueur(liste):
            if liste[index-1] > liste[index]:
                liste[index-1], liste[index] = liste[index], liste[index-1]
                echange = True
            index += 1
    return liste

print(trier(L))
