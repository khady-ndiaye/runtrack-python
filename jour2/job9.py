#nombre pair et impair de 1 à 30
for i in range(1, 31):
    if i % 2 == 0:
        print(f"{i} est pair")
    else:
        print(f"{i} est impair")
        
 # affichage par liste de pair et liste d'impair separé
print("liste des nombres pairs de 1 à 30")
      
for i in range(1 , 30):
    if i % 2 == 0:
        print(i)
print("liste des nombres impairs de 1 à 30")
for i in range(1 , 30):
    if i % 2 != 0:
        print(i)