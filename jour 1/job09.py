# Création de variables pour un article de supermarché
nom_produit = "Pomme"
prix_produit = 0.99  # en euros
quantite_produit = 5  # nombre d'articles



# Affichage des informations sur l'article
print(f"Article : {nom_produit}")
print(f"Prix : {prix_produit} €")
print(f"Quantité : {quantite_produit} pièces")


#ajout de produit au stock
quantite_produit = quantite_produit + 10


#demander au client de rentrer le nombre d'article qu'il souhaite acheter
achat_produit = int(input(f"Combien de {nom_produit} souhaitez-vous acheter ? "))


# Vérifier si la quantité demandée est disponible en stock
if achat_produit <= quantite_produit:
    # Calculer le prix total
    prix_total = prix_produit * achat_produit

    # Mettre à jour le stock
    quantite_produit = quantite_produit - achat_produit
    print("stock restant=", quantite_produit)
else:
    # Si la quantité demandée est trop grande
    print(f"Désolé, il n'y a pas assez de {nom_produit} en stock. Stock disponible : {quantite_produit} pièces.")
    #inflation: augmentation de 10% du prix
inflation_produit = 0.1 * prix_produit
nouveau_prix = prix_produit + inflation_produit
print("nouveau prix=", nouveau_prix)

#recaputilatif
print(f" Récapitulatif PRODUIT ")
print(f"Article : {nom_produit}")
print(f"Prix : {nouveau_prix} €")
print(f"Quantité_initiale: {quantite_produit} pièces")
print(f"Quantité acheté : {achat_produit } pièces") 
print(f"stock restant : { quantite_produit} pièces") 