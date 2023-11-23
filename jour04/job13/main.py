def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons +=[element]

    return liste_sans_doublons

# Liste donnée
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Appel de la fonction pour supprimer les doublons
resultat = supprimer_doublons(ma_liste)

# Affichage du résultat
print("Liste sans doublons:", resultat)
