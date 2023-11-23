def L():
    liste=list(range(1,6))
    return liste
print(L())

def L():
    liste=list(range(1,6))
    return liste[1]
print(L())

def L():
    liste=list(range(1,6))
    liste[3]= liste[2]+liste[4]
    return liste
print(L())

def L():
    liste=list(range(1,6))
    liste[3]= liste[2]+liste[4]
    return liste[-1]
print(L())