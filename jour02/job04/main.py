n = int(input("saisir un entier superieur a 0 :"))

if n>0:
    for i in range (1,11):
        print (f"{i} x {n} = {i*n}")

else: 
    print ("vous avez saisi 0, ce n'est pas valide")
