def arrondir_et_trier(liste):
    # Arrondir les nombres dans la liste
    liste_arrondie = []
    for nombre in liste:
        partie_entiere = int(nombre)
        partie_decimale = nombre - partie_entiere
        if partie_decimale >= 0.5:
            nombre_arrondi = partie_entiere + 1
        else:
            nombre_arrondi = partie_entiere
        liste_arrondie += [nombre_arrondi]

    # Trier la liste arrondie dans l'ordre croissant sans utiliser sort()
    echange = True #echange effectué 
    while echange:
        echange = False # On initialise l'échange à False avant chaque nouvelle itération 
        index = 1 #commence a l'index 1 pour qu'il puisse comparé avec l'index0
        while index < longueur(liste_arrondie):
            # comparaison et échange si chiffre n'est pas en ordre croissant 
            if liste_arrondie[index-1] > liste_arrondie[index]:
                liste_arrondie[index-1], liste_arrondie[index] = liste_arrondie[index], liste_arrondie[index-1]
                echange = True #si un échange est fait, on le repasse en True
            index += 1

    return liste_arrondie

# Fonction pour calculer la longueur de la liste sans utiliser la fonction système len()
def longueur(liste):
    compteur = 0
    for nombre in liste:
        compteur += 1
    return compteur

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Appel de la fonction pour arrondir et trier la liste
resultat = arrondir_et_trier(ma_liste)

# Affichage du résultat
print("resultat :", resultat)