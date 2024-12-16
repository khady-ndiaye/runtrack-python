
def somme_des_termes_pairs():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]    
    somme = 0
    for i in range(0 ,len(L)):
        if L[i] % 2 == 0:
            somme = somme + L[i]   
    return somme
ressultat = somme_des_termes_pairs()        
print("la somme de tous les nombres pairs de la liste est", ressultat)