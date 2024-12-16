# afficher les tables de multiplications de 1 à 10
N = int(input( "entrez un entier entre 1 et 10"))
#pour aller plus loin on pourrai checker si l'utilisateur entre une valeur valide et lui demander de rentrer une nouvelle valeur sinon

for i in range(1, N + 1):
    print(f"\nTable de multiplication de {i}:")
    for j in range(1, 11):  # On affiche les multiples de 1 à 10
        print(f"{i} x {j} = {i * j}")