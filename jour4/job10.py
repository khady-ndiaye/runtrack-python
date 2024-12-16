# Définition de la fonction qui vérifie si un nombre est pair ou impair
def nombre_pair_impair(nombre):
    # Vérification si le nombre est un entier positif
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")

nombre_pair_impair(10)   
nombre_pair_impair(15)   
nombre_pair_impair(0)   
nombre_pair_impair(-5)  
nombre_pair_impair(7) 
nombre_pair_impair(22) 