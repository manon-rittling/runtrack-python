for i in range (1,101):
    # verifie les multiples de 3 et 5
    if i % 3 == 0 and i % 5 == 0:
        print ("fizzBuzz")
        # verifie le multiple de 3 est affiche fizz
    elif i % 3 == 0:
        print ("Fizz")
    
        # verifie le multiple de 5 est affiche buzz
    elif i % 5 == 0:
        print ("Buzz")

    else: 
        print(i)