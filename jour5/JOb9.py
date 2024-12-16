def min_max():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

    val_max = max(L)

    val_min = min(L)
    
    return val_max , val_min

val_max , val_min = min_max()
print("la valeur maximal de L est" , val_max)
print("la valeur minimal de L est", val_min)


