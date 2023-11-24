def draw_rectangle(width, height):
    lignes = [] #liste crée pour mettre es lignes

    for i in range(height):
        if i == 0 or i ==height - 1:  
            ligne =" " + "-" * (width - 2) + " "
        else:
            ligne = "|" + " " * (width - 2) + "|"
        lignes.append(ligne)

    return lignes

rectangle=draw_rectangle(10, 4)
for dessin in rectangle:
    print(dessin)









    
