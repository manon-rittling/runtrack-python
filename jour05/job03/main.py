
# Demande à l'utilisateur de saisir la hauteur du triangle
hauteur = int(input("Saisir le nombre des lignes:"))

# Définition de la fonction qui dessine le triangle en fonction de la hauteur
def dessin_triangle(hauteur):
    # Boucle qui itère sur chaque ligne du triangle
    for i in range(hauteur):
        # Condition pour la première ligne du triangle
        if i == 0:
            ligne = ' ' * (hauteur - i) + '/' + '\\'  # La ligne construit la première ligne du triangle en ajoutant des espaces avant '/', puis en plaçant '/' suivi de '\\', créant ainsi une diagonale ascendante de gauche à droite.
       
        elif i == hauteur - 1:  #La condition i == hauteur - 1 vérifie si la boucle itère sur la dernière ligne du triangle, permettant une construction spécifique de cette ligne.
            
            ligne = ' /' + '_' * (2 * hauteur - 2) + '\\' # Construction de la dernière ligne avec '/__\\' (underscore pour représenter '_')
        else:
            # Pour les lignes intermédiaires
            espaces = ' ' * (hauteur - i)  # Calcul des espaces avant et après le motif principal
            ligne = espaces + '/' + ' ' * (2 * i) + '\\' + espaces # Construction de la ligne avec '/' et '\\' et des espaces
        # Affichage de la ligne actuelle du triangle
        print(ligne)

# Appeler la fonction avec la hauteur fournie par l'utilisateur
dessin_triangle(hauteur)


#explication

# Ce code en Python permet à l'utilisateur de saisir la hauteur d'un triangle, puis utilise une fonction dessin_triangle pour afficher le triangle correspondant dans la console. Voici une explication détaillée du code :
# hauteur = int(input("Saisir le nombre des lignes:")): Demande à l'utilisateur de saisir un nombre, qui représente la hauteur du triangle, et convertit l'entrée en un entier.
# def dessin_triangle(hauteur):: Définit une fonction dessin_triangle qui prend la hauteur du triangle en tant que paramètre.
# for i in range(hauteur):: Utilise une boucle for pour itérer à travers chaque ligne du triangle, où i est l'indice de la ligne actuelle (commençant à zéro).
# if i == 0:: Condition pour la première ligne du triangle.
# ' ' * (hauteur - i) + '/' + '\\': Construit la première ligne avec des espaces avant '/' et '\\', créant ainsi une diagonale ascendante de gauche à droite.
# elif i == hauteur - 1:: Condition pour la dernière ligne du triangle.
# ' /' + '_' * (2 * hauteur - 2) + '\\': Construit la dernière ligne avec '/__\\' (underscore pour représenter '_'), formant ainsi la base du triangle.
# else:: Condition pour les lignes intermédiaires du triangle.
# espaces = ' ' * (hauteur - i): Calcul des espaces avant et après le motif principal.
# ligne = espaces + '/' + ' ' * (2 * i) + '\\' + espaces: Construction de la ligne avec '/', '\\', et des espaces pour aligner le motif principal.
# print(ligne): Affiche la ligne actuelle du triangle à la console.
# dessin_triangle(hauteur): Appelle la fonction dessin_triangle avec la hauteur fournie par l'utilisateur, déclenchant ainsi le dessin du triangle.