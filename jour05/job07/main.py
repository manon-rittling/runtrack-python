def arrondir_notes(liste):
    nouvelles_liste = []

    for note in liste:
        if note > 40:
            prochain_multiple_de_5 = ((note // 5) + 1) * 5 # prend la note actuelle, divise son quotient par 5, ajoute 1 pour obtenir le prochain multiple de 5, puis multiplie le résultat par 5 pour assurer que le nombre est un multiple de 5 supérieur ou égal à la note actuelle. Cela est utilisé pour arrondir les notes des étudiants ayant réussi le test.
            difference = prochain_multiple_de_5 - note

            if difference < 3:
                note = prochain_multiple_de_5

        nouvelles_liste.append(note)

    return nouvelles_liste

liste_notes = [ 43, 82, 93, 51]
resultat = arrondir_notes(liste_notes)
print(resultat)
