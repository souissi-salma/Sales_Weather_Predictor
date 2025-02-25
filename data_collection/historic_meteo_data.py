import pandas as pd
from meteostat import Hourly, Stations
from datetime import datetime, timedelta

# Liste des villes avec leurs coordonnées GPS (latitude, longitude)
CITIES = {
    "Tunis": (36.8002068, 10.1857757),
    "Ariana": (36.968573500000005, 10.121985506329507),
    "Ben Arous": (36.63064825, 10.210082703817534),
    "Manouba": (36.7624363, 9.833619078262766),
    "Nabeul": (36.4512897, 10.7355915),
    "Zaghouan": (36.3319504, 10.045299971877625),
    "Bizerte": (37.2720905, 9.8708565),
    "Beja": (36.7236755, 9.185382),
    "Jendouba": (36.67797255, 8.752646965460535),
    "Kef": (36.03576425, 8.72493808761197),
    "Siliana": (35.9715323, 9.3577128756367),
    "Kasserine": (35.1687646, 8.8365654),
    "Sidi Bouzid": (34.881181, 9.526359847182345),
    "Kairouan": (35.6710101, 10.10062),
    "Kébili": (33.33877015, 8.703290964584628),
    "Tozeur": (33.9239001, 8.1370639),
    "Gabès": (33.8878082, 10.10044),
    "Medenine": (32.981998700000005, 11.287025364730832),
    "Tataouine": (31.7317009, 9.770219749624271),
    "Mahdia": (35.503642, 11.0682429),
    "Monastir": (35.7707582, 10.8280511),
    "Sousse": (35.8288284, 10.6405254),
    "Sfax": (34.7394361, 10.7604024),
    "Gafsa": (34.4224374, 8.7843862)
}

# Définition de la période (5 dernières années)
END_DATE = datetime.today()
START_DATE = END_DATE - timedelta(days=5*365)

# Liste pour stocker toutes les données
all_data = []

# Récupération et extraction des données horaires pour chaque ville
for city, (lat, lon) in CITIES.items():
    print(f"Récupération des données horaires pour {city}...")
    stations = Stations().nearby(lat, lon)
    station = stations.fetch(1).index[0]  # Prendre la station la plus proche

    data = Hourly(station, START_DATE, END_DATE)
    data = data.fetch()

    # Vérifier si des données sont récupérées
    if not data.empty:
        # Transformation des données en DataFrame
        df = pd.DataFrame(data)

        # Extraire la date et l'heure
        df['date'] = df.index.date
        df['hour'] = df.index.hour

        # Ajouter la colonne "city" avec le nom de la ville
        df['city'] = city

        # Ajouter les données de cette ville dans la liste all_data
        all_data.append(df)

        print(f"Données horaires extraites pour {city} ")
    else:
        print(f"Aucune donnée récupérée pour {city}")

# Concaténer toutes les données en un seul DataFrame
final_df = pd.concat(all_data)

# Sauvegarde des données dans un fichier CSV
final_df.to_csv("data_all_cities_hourly.csv", index=False)

print("Extraction des données terminée pour toutes les villes.")
