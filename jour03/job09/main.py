def moyenne(note1,note2,note3):
    return (note1 + note2 + note3) /3

note1 = float(input("Saisir votre premiere note :"))
note2 = float(input("Saisr votre deuxieme note:"))
note3 = float(input("Saisir la troisieme note :"))

moyenne_etudiant = moyenne(note1,note2,note3)

print("La moyenne de l'etudiant est de:", moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20:
    print ("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 11:
    print("Elève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Elève devant faire des efforts")

