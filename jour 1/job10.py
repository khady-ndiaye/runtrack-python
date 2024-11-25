montant_investissement = 2000 # Montant de l'investissement
taux_rendement_annuel = 5  # taux de rendement annuel en %
#calcul du gain annuel
gain_annuel = montant_investissement * ( taux_rendement_annuel / 100)
print(f"montant de l'investissement : {montant_investissement} € ")
print(f"taux de rendement annuel : {taux_rendement_annuel } %")
print(f"gain annuel en fonction du taux de rendement : { gain_annuel} €")

#augmentation de  l'investissement et du taux de rendement
montant_investissement = montant_investissement + 5000
taux_rendement_annuel = taux_rendement_annuel + 2
new_gain_annuel = montant_investissement * ( taux_rendement_annuel / 100)
print(f"montant de l'investissement : {montant_investissement} € ")
print(f"taux de rendement annuel : {taux_rendement_annuel } %")
print(f"new_gain annuel en fonction du taux de rendement : { new_gain_annuel} €")

#retrait de 10% de l'investissement
montant_investissement = (montant_investissement + new_gain_annuel) - ( montant_investissement * 0.1)
taux_rendement_annuel = taux_rendement_annuel - 1
new_gain_annuel = montant_investissement * ( taux_rendement_annuel / 100)
print(f"montant de l'investissement : {montant_investissement} € ")
print(f"taux de rendement annuel : {taux_rendement_annuel } %")
print(f"new_gain annuel en fonction du taux de rendement : { new_gain_annuel} €")
