def distance(nombreMarche, hauteurMarche):
    distance_parcourue=2 * nombreMarche * hauteurMarche * 5 / 100 *7 #calcul la distance 
    return f"le gardien parcourt {distance_parcourue:.2f} m par semaine"

nombreMarche= 10
hauteurMarche=50

print(distance(nombreMarche, hauteurMarche))


# explication du calcul

# hauteurMarche: La hauteur de chaque marche en centimètres.
# 5 / 100: La fréquence des visites aux toilettes par jour (5 fois par jour), exprimée en fraction.
# 7: Le nombre de jours dans une semaine.
# Ainsi, le calcul s'effectue comme suit :

# Descente et remontée des marches (2 * nombreMarche * hauteurMarche) :

# Multiplie le nombre total de marches par la hauteur de chaque marche pour obtenir la distance totale parcourue lors de la descente et de la remontée des marches.
# Fréquence des visites aux toilettes (5 / 100) :

# Multiplie la distance totale par la fraction 5 / 100, représentant le nombre de fois que le gardien va aux toilettes par jour.
# Nombre de jours dans une semaine (* 7) :

# Multiplie le résultat par 7 pour obtenir la distance totale parcourue en une semaine.
# Ainsi, la formule complète calcule la distance totale parcourue par le gardien en une semaine pour aller aux toilettes en tenant compte de la descente, 
# de la remontée, de la fréquence quotidienne et du nombre de jours dans une semaine




