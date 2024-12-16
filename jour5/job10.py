
def produit_intervalle(L, min_val, max_val):
    produit = 1  # Initialiser le produit à 1 (identité pour la multiplication)
    for i in L:
        if min_val <= i <= max_val:  # Vérifie si la valeur est dans l'intervalle [25, 90]
            produit *= i  # Multiplie l'élément au produit
    return produit

# Liste donnée
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = produit_intervalle(L, 25, 90)
print("Le produit des valeurs comprises dans l'intervalle [25, 90] est:", resultat)    