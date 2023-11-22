def affiche_produits(type, saison):
    if type == "fruits" and saison == "hiver":
            print("Orange, mandarine et kiwi")
    elif saison == "ete":
        print("Poire, fraise, cassis")  
    elif type == "legume"and saison == "hiver":
            print("Carotte, topinambour, endive")
    elif saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("aucun produit ne correspond")
    


affiche_produits("fruits", "hiver")  
affiche_produits("fruits", "ete")    
affiche_produits("legume", "hiver")  
affiche_produits("legume", "ete")    
   
