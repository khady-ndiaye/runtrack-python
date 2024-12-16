# Initialisation du compteur
i = 0

# Boucle while pour parcourir les nombres de 0 à 100
while i <= 100:
    # Vérifier si le nombre n'est pas 27, 37 ou 88
    if i not in [27, 37, 88]:
        print(i)  # Afficher le nombre
    i += 1  # passer au suivant

#autre methode
# Parcourir les nombres de 0 à 100 inclus
for i in range(101):
    # Vérifier si le nombre n'est pas 27, 37 ou 88
    if i not in [27, 37, 88]:
        print(i)  # Afficher le nombre