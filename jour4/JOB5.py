def calcul(num1, operator, num2):
    if operator == "+" :
        return num1 + num2
    elif operator =="-" :
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == "%":
        return num1 % num2
    else:
        return "Opérateur invalide"

# Appels de la fonction avec différents exemples
resultat1 = calcul(1, "+", 5)  # Addition
resultat2 = calcul(10, "-", 5)  # Soustraction
resultat3 = calcul(3, "*", 5)  # Multiplication
resultat4 = calcul(10, "/", 2)  # Division
resultat5 = calcul(10, "/", 0)  # Division par zéro
resultat6 = calcul(12, "%", 5)  # Modulo

# Affichage des résultats
print(resultat1) 
print(resultat2)  
print(resultat3)  
print(resultat4)  
print(resultat5)  
print(resultat6)




      
    