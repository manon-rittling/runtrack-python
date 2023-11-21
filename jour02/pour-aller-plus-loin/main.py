# Demander à l'utilisateur les trois longueurs

a = int(input ("entrez la longueur a :"))
b = int(input ("entrez la longueur b :"))
c = int(input("entrez la longueur c :"))

# verifie si les longueurs peuvent former un triangle

if a + b > c and a + c > b and b + c > a :
    print("ces longueurs peuvent faire un triangle")
    
    # Identifier le type de triangle
    
    if a == b == c :
        print("triangle équilateral")

    elif a == b or a == c or b ==c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 ==a**2:
            print("triangle isocèle rectangle")
        else:
            print("triangle isocèle")
        
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 ==a**2:
        print("triangle rectangle")

    else:
        print("triangle quelconque")

else:
    print("ce n'est pas un triangle") 