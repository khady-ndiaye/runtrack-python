def time_to_text(minutes):
    # Vérification que minutes est un nombre entier positif
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60  
        minutes_restantes = minutes % 60  # les minutes sont le reste de la division par 60
        print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif.")
time_to_text(145)
time_to_text(30)
time_to_text(120)