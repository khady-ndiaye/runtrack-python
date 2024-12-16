for i in range(2, 1001): # on commence par 2 car on sait que 1 n'est pas premier
    
    for j in range(2, i): # Boucle pour vérifier si i est divisible par un autre nombre que 1 et i
        if i % j == 0:  # Si i est divisible par j, alors ce n'est pas un nombre premier
            break  # Si un diviseur est trouvé, on arrête de vérifier et on passe au prochain nombre
    else:
        # Si la boucle intérieure se termine sans trouver de diviseur, i est premier
        print(i)