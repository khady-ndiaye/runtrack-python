#job 11
# Créer la liste L
L = [7, 11, 42, 39, 2]

for i in range(len(L)):
    L[i] += 1

print(L)


#job 12
def trier_liste(L):
    for i in range(len(L)): 
        for j in range(i+1, len(L)): 
            if L[i] > L[j]: 
                L[i], L[j] = L[j], L[i]


ma_liste = [7, 11, 42, 39, 2]
trier_liste(ma_liste)
print(ma_liste)

#job 13 à revoir
def supprimer_doublon():
    L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    nouvelle_liste = []
    for  x in enumerate(L): # Utilisation de enumerate pour parcourir la liste
        # Si l'élément n'est pas déjà dans la nouvelle liste, on l'ajoute
        existe_deja = False
        for item in nouvelle_liste:
            if item == x :                
                existe_deja = True
                break
        if not existe_deja:
            nouvelle_liste.append(x)
    
    return nouvelle_liste



ma_liste_sans_doublons = supprimer_doublon()
print(ma_liste_sans_doublons)

   
#L = [x for i, x in enumerate(L) if x not in L[:i]]
