
nom= "baguette"
prix_unitaire= 1
quantité_en_stock= 30

resultat= f'produit:{nom} prix:{prix_unitaire} stock:{quantité_en_stock}'
print (resultat)

quantité_acheté= int(input(f'combien de {nom} voulez vous acheter?'))


prix_unitaire *= 1.1
quantité_en_stock -= quantité_acheté

print ( f'produit {nom} prix:{prix_unitaire}€ stock a jour {quantité_en_stock}')



