def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3
note1 =float(input("entrer votre 1ere note"))
note2= float(input("entrer votre 2eme note"))
note3= float(input("entrer votre 3eme note"))

moyenne_etudiant=moyenne(note1 ,note2  ,note3)
print(f"La moyenne de l'étudiant est : {moyenne_etudiant:.2f}")
if 15 <= moyenne()<= 20:
    print("Tres bon éléve")
elif 11 <= moyenne_etudiant < 15:
    print("Bon élève")
elif 8 <= moyenne_etudiant < 11:
    print("Élève moyen")
elif 0 <= moyenne_etudiant < 8:
    print("Élève devant faire des efforts")
else:
    print("Note invalide")



   