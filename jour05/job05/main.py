
def chiffrement_cesar(message, decalage):
    # Initialisation de la variable pour stocker le résultat chiffré
    resultat = ''

    # Parcours de chaque caractère dans le message
    for caractere in message:
        
        if caractere.isalpha(): # Vérification si le caractère est une lettre alphabétique
            
            alphabet = 'abcdefghijklmnopqrstuvwxyz' if caractere.islower() else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Détermination de l'alphabet approprié (minuscules ou majuscules)
            
            nouvel_index = (alphabet.find(caractere) + decalage) % 26 # Chiffrage du caractère en tenant compte du décalage et du dépassement de l'alphabet
            caractere_chiffre = alphabet[nouvel_index]
            resultat += caractere_chiffre # Ajout du caractère chiffré au résultat
        else:
            resultat += caractere # Si le caractère n'est pas une lettre, l'ajouter tel quel au résultat

    return resultat # Retour du résultat chiffré

# Exemple d'utilisation avec un message et un décalage de 3
message = "Jules César, général et stratège romain"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)

# Affichage du message chiffré
print("Message chiffré:", message_chiffre)



# Explication détaillée :

# But du Code :

# Le code vise à chiffrer un message en utilisant la méthode de chiffrement de César, où chaque lettre du message est déplacée vers la droite dans l'alphabet par un certain nombre de positions (décalage).
# Comment Fonctionne la Fonction :

# La fonction chiffrement_cesar prend deux informations en entrée : le message que vous souhaitez chiffrer et le décalage que vous souhaitez appliquer.
# Elle retourne le message chiffré.
# Étapes Principales :

# La fonction parcourt chaque lettre du message.
# Si la lettre est alphabétique, elle est chiffrée en fonction du décalage.
# Le résultat est stocké dans une nouvelle chaîne de caractères.
# Gestion du Dépassement :

# L'alphabet est utilisé pour déterminer quelle lettre vient après le décalage.
# Si une lettre atteint la fin de l'alphabet, elle revient au début.
# Par exemple, si vous chiffrez 'z' avec un décalage de 1, vous obtenez 'a'.
# Exemple d'Utilisation :

# Le code inclut un exemple où le message "Jules César, général et stratège romain" est chiffré avec un décalage de 3.
# Le résultat est affiché.
# En résumé, la fonction prend un message et un décalage, déplace chaque lettre du message en fonction du décalage, gère le dépassement de l'alphabet, et retourne le message chiffré.

# deuxieme possibilité :


# import string
# string.ascii_lowercase


# def chiffrage(mot, decalage):
#     mot_code = ""
#     for i in mot:
#         i = ord(i)
#         if 96 < i:
#             i += decalage
#             if i > 122:
#                 i -= 26
#         mot_code += chr(i)
#     print (mot_code)

# chiffrage("Jules César, général et stratège romain", 3)


