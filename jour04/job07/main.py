L=[8, 24, 48, 2, 16]

def multiple3 (liste):
    compte=0
    for nombre in liste:
        if nombre %3==0:
            compte += 1
    return compte
print(multiple3(L))
