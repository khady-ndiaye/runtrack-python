values = input("entrer 3 nombres separés par des espaces ")
a,b,c = values
if a + b > c and b+c > a and a + c > b : # on verifie les conditions pour que abc forme un triangle
    print("il est possible de construire un triangle avec (a,b,c)")
else:
    print("il n'est pas possible de construire un triangle avec ces valeurs")    
   


