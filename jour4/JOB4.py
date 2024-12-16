def gethello():
    print("hello la plateforme")
gethello()    
#methode avec return
def GetHello():
    return "Hello la Plateforme"

# Appel de la fonction et affichage du résultat
message = GetHello()
# Récupérer la valeur : La fonction GetHello renvoie (avec return) une valeur, ici la chaîne "Hello la Plateforme". Cette valeur peut ensuite être utilisée ailleurs dans le programme. Par exemple, on peut la stocker dans une variable (message dans ce cas), ou l'utiliser dans une autre fonction ou dans des calculs.
#Flexibilité : Cela permet une plus grande flexibilité. Vous pouvez décider d'utiliser la valeur retournée de différentes façons, comme l'afficher, l'ajouter à une autre chaîne, la transmettre à une autre fonction, etc.
#Fonction pure : Cette approche fait de la fonction GetHello une fonction "pure", qui produit un résultat basé uniquement sur ses paramètres (même si ici il n'y a pas de paramètres), sans effectuer directement une action (comme afficher quelque chose à l'écran).
print(message)

#return permet de renvoyer une valeur que vous pouvez stocker, manipuler ou passer à d'autres fonctions. Cela rend votre code plus flexible et réutilisable.


#print() affiche immédiatement quelque chose à l'écran, mais ne permet pas de manipuler ou de récupérer cette valeur pour d'autres usages dans le programme.

# Conclusion :
#Utilisez return lorsque vous avez besoin d'une valeur calculée ou produite par la fonction, que vous souhaitez utiliser plus tard ou manipuler dans le programme.
#Utilisez print() lorsque vous souhaitez simplement afficher quelque chose à l'écran sans avoir besoin de conserver cette information pour d'autres usages.