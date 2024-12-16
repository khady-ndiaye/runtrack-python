chaine = "abcdefghijklmnopqrstuvwxyz" * 10   # La chaîne répétée 10 fois

  # On commence avec une seule lettre sur la première ligne
index = 0  # on initialise la variable qui nous indique la position actuelle dans la chaine
while index +2 <= len(chaine):
    print(chaine[0:index +1])
    index += 2
    