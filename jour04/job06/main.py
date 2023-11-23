def changeValeur():
    valeur=list(range(1,6))
    return valeur

print(changeValeur())

def changeValeur():
    valeur=list(range(1,6))
    valeur[0],valeur[4] = valeur[4],valeur[0]
    return valeur

print(changeValeur())