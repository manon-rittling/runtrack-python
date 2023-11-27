
def tapisserie(taille):
    # Le bord
    bord = "+"  # Initialisation de la bordure avec le premier caractère '+'
    for i in range(taille + 1):
        bord += "-"  # Ajout de caractères '-' en fonction de la taille
    bord += "+"  # Ajout du dernier caractère '+'

    print(bord) # Affichage du bord supérieur

    # La boucle d'affichage du motif de tapisserie
    for i in range(taille + 1):
        tapis = ""  # Initialisation de la ligne de tapis
        for j in range(taille - i):
            tapis += "#"  # Ajout de caractères '#' en fonction de la taille - i
        tapis += " "  # Ajout d'un espace
        for j in range(i):
            tapis += "#"  # Ajout de caractères '#' en fonction de i
        
        print("|" + tapis + "|") # Affichage de la ligne de tapis entre deux caractères '|'

   
    print(bord)  # Affichage du bord inférieur

# Appel la fonction tapisserie avec une taille de 10
tapisserie(10)



# Fonction tapisserie(taille):

# Une fonction appelée tapisserie qui crée un motif de tapisserie en fonction de la taille spécifiée.
# Construction du bord (bord):

# On commence par créer une variable appelée bord avec le premier caractère, un +.
# Ensuite, on utilise une boucle (for i in range(taille + 1)) pour ajouter autant de caractères - que la taille spécifiée.
# On termine en ajoutant le dernier caractère, un +.
# Affichage du bord (print(bord):

# On imprime la ligne du haut du motif de tapisserie qui est stockée dans la variable bord.
# Boucle d'affichage (for i in range(taille + 1):):

# On commence une boucle qui va de 0 à la taille spécifiée.
# Construction de la ligne de tapis (tapis):

# On crée une variable appelée tapis pour stocker la ligne de caractères # et d'espaces.
# À l'intérieur de cette boucle, on ajoute des caractères # à tapis en fonction de la valeur taille - i.
# On ajoute ensuite un espace à tapis.
# Enfin, on ajoute davantage de caractères # à tapis en fonction de la valeur i.
# Affichage de la ligne de tapis (print("|" + tapis + "|")):

# On imprime la ligne de tapis entre deux caractères |.
# Affichage du bord inférieur (print(bord):

# On imprime la ligne du bas du motif de tapisserie qui est stockée dans la variable bord.
# Appel de la fonction tapisserie(10):

# Enfin, on appelle la fonction tapisserie avec une taille de 10 pour créer un motif de tapisserie de taille 10.
# Le script crée essentiellement une bordure supérieure et inférieure du motif de tapisserie avec des caractères + et -. Ensuite, à l'intérieur de ces bordures, il construit une série de lignes diagonales vides avec des caractères # entre deux caractères |.
# La taille du motif de tapisserie est déterminée par l'argument passé à la fonction tapisserie.