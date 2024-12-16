L = [8, 24,48,2,16]
def multiple_de_trois(L):
    compteur= 0
    for i in range(0 ,len(L)):
        if L[i] % 3==0:
            compteur +=1
    return compteur
ressultat = multiple_de_trois(L)        
print("le nombre de multiple de 3 est", ressultat)