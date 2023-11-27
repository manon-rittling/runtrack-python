# Liste donnée
L = [7, 22, 12, 4, 45, 32, 25]

# Fonction pour calculer la longueur de la liste sans utiliser la fonction système len()
def longueur(liste):
    compteur = 0
    for nombre in liste:
        compteur += 1
    return compteur

# Fonction pour trier la liste dans l'ordre croissant sans utiliser une fonction système
def trier(liste):
    echange = True  # Échange effectué
    coups = 0  # Initialiser le compteur de coups à 0

    while echange:
        echange = False  # On initialise l'échange à False avant chaque nouvelle itération
        index = 1  # Commence à l'index 1 pour qu'il puisse comparer avec l'index 0
        while index < longueur(liste):
            # Comparaison et échange si le chiffre n'est pas en ordre croissant
            if liste[index - 1] > liste[index]:
                liste[index - 1], liste[index] = liste[index], liste[index - 1]
                echange = True  # Si un échange est fait, on le repasse en True
                coups += 1  # Incrémenter le compteur de coups
            index += 1

    # Afficher le nombre total de coups nécessaires pour trier la liste
    print("Nombre total de coups pour trier la liste :", coups)

    return liste

print(trier(L))
