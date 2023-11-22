def verifierPairImpair(nombre):
    if not isinstance(nombre, int) or nombre <0:
        print("entrer un nombre entier positif")
        return
    
    if nombre % 2 == 0:
        print(f"le nombre {nombre} est pair")
    else:
        print(f"le nombre {nombre} est impair")

verifierPairImpair(2)
verifierPairImpair(7)
verifierPairImpair(5)