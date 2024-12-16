def fruit_legume_saison(type, saison):
    if type== "fruit" and saison=="hiver":
        print("« orange, mandarine , kiwi")
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("Aucun aliment trouvé pour cette combinaison.")
# Appel de la foction
fruit_legume_saison("fruit", "hiver")      
fruit_legume_saison("fruit","été")      
fruit_legume_saison("fruit", "printemps")      
fruit_legume_saison("légume", "hiver")      
fruit_legume_saison("légume", "été")      