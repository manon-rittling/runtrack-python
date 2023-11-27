# Définition de la fonction draw_rectangle qui génère un rectangle en utilisant des caractères "|", "-" et des espaces
def draw_rectangle(width, height):
    lignes = []  # Liste pour stocker chaque ligne du rectangle

    for i in range(height):
        # Condition pour la première et la dernière ligne du rectangle
        if i == 0 or i == height - 1:
            ligne = "|" + "-" * (width - 2) + "|"  # Construction de la ligne horizontale du rectangle
        else:
            ligne = "|" + " " * (width - 2) + "|"  # Construction des lignes intermédiaires avec des espaces
        lignes.append(ligne)  # Ajout de la ligne à la liste lignes

    return lignes  # Retourne la liste de lignes représentant le rectangle

# Appel de la fonction draw_rectangle avec une largeur de 10 et une hauteur de 4
rectangle = draw_rectangle(10, 4)

# Affichage du rectangle en imprimant chaque ligne
for dessin in rectangle:
    print(dessin)


# Explication détaillée :

# Fonction draw_rectangle(width, height):
# Définit une fonction qui prend deux paramètres, width (largeur) et height (hauteur), représentant les dimensions du rectangle.
# Initialise une liste lignes pour stocker chaque ligne du rectangle.
# Boucle for i in range(height):
# Itère sur chaque ligne du rectangle en fonction de la hauteur spécifiée.
# Conditions pour la première et la dernière ligne du rectangle (if i == 0 or i == height - 1):
# Construit la ligne horizontale du rectangle avec des caractères "|" à chaque extrémité et des caractères "-" entre elles pour la première et la dernière ligne.
# Pour les lignes intermédiaires, construit la ligne avec des espaces entre les caractères "|".
# Ajout de chaque ligne à la liste lignes (lignes.append(ligne)):
# Ajoute chaque ligne générée à la liste lignes.
# Retourne la liste lignes représentant le rectangle (return lignes):
# La fonction renvoie la liste de lignes représentant le rectangle.
# Appel de la fonction et affichage du rectangle:
# Appelle la fonction draw_rectangle avec une largeur de 10 et une hauteur de 4, stocke le résultat dans la variable rectangle.
# Utilise une boucle for pour imprimer chaque ligne du rectangle.










    
