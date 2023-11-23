L = [7, 11, 42, 39, 2]
def addition(liste):
    nouvelleListe = [i + 1 for i in liste]
    return nouvelleListe
print(addition(L))


        
def list():
    L = [7, 11, 42, 39, 2]
    for i in range(len(L)):
        L[i] += 1
    print(L)
print(list())