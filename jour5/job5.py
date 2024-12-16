def operation_sur_liste():
    L=[1,2,3,4,5]
    print(L[1])
    L[3]= L[2] +L[4]
    print(L)
    print(L[-1])

operation_sur_liste()



# methode plus général
def operation_sur_liste():
    n = int(input("entrez un entier superieur ou egal à 5"))
    L= list(range(1, n+1))
    print(L)
    L[3]= L[2] +L[4]
    print(L)
    print(L[-1])

operation_sur_liste()