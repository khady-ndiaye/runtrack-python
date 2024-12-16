def initialiser_grille():
    return [["-" for _ in range(3)] for _ in range(3)]


def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 5)  # Pour séparer les lignes
        

afficher_grille(initialiser_grille)