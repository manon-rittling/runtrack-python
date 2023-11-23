def my_long_word(chiffre, chaine):  #la fonction prend deux paramètres "number(chiffre entier)" et text
    mots = chaine.split()   #découpe de la chaîne text en une liste de mots en utilisant l'expace comme séparateur et stocke ces mots ces mots dans la variable "words"
    resultat = ""    #Initialisation d'une chaine vide "result" qui stockera les mots plus longs que "number"

    for mot in mots:  #boucle qui parcourt chaque mot dans dans la liste "words"
        compteur = 0  #initialisation d'un compteur "word_length" à zéro
        for lettre in mot:   #boucle qui parcourt chaque caractère dans le mot actuel
            compteur += 1    #pour chaque caractère, elle incrémente le compteur "word_length" de 1
        
        if compteur > chiffre:     #après avoir parcouru tous les caractères du mot, elle vérifie si "word_length" est supérieur à "number"
            resultat += mot + " "  #si la longueur du mot est supérieure au chiffre donnée, elle ajoute ce mot à la chaîne "result" suivie d'un espace à l'aide de guillemets " "

    return resultat     #la fonction retourne la chaîne de caractères 

chaine_trier = my_long_word(4, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(chaine_trier)

        

        
        