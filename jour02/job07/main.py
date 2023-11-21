
chaine = "abcdefghijklmnopqrstuvwxyz" * 10 #crea de la chaine en repetant la sequence 10x

for i in range(1, len(chaine), 2): #boucle for pour determiner quels indice elle va pacourir
    print(chaine[:i])


#explication en details de la boucle for 
#range(1, len(chaine), 2) : C'est une fonction en Python qui génère une séquence d'entiers dans un intervalle donné. Dans ce cas particulier :
#Le premier argument (1) est le point de départ de la séquence. La séquence commence à l'indice 1.
#Le deuxième argument (len(chaine)) est la limite supérieure de la séquence. La séquence s'arrête juste avant la longueur totale de la chaîne.
#Le troisième argument (2) est le pas, c'est-à-dire de combien la séquence avance à chaque itération. En utilisant un pas de 2, la séquence inclura uniquement les indices impairs.
#Ainsi, range(1, len(chaine), 2) crée une séquence d'indices commençant à 1, s'arrêtant juste avant la longueur totale de la chaîne, et incluant uniquement les indices impairs.