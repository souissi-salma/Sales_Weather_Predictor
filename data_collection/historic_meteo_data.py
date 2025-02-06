import pandas as pd
import psycopg2
from meteostat import Daily, Stations
from datetime import datetime, timedelta

# Paramètres de connexion PostgreSQL
DB_PARAMS = {
    "dbname": "données_météorologiques",
    "user": "postgres",
    "password": "",
    "host": "localhost",
    "port": "5432"
}

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

# Connexion à PostgreSQL
conn = psycopg2.connect(**DB_PARAMS)
cursor = conn.cursor()
print(data.columns)  # Vérifie les noms des colonnes récupérées

# Récupération et insertion des données
for city, (lat, lon) in CITIES.items():
    print(f"Récupération des données pour {city}...")
    stations = Stations().nearby(lat, lon)
    station = stations.fetch(1).index[0]  # Prendre la station la plus proche
    
    data = Daily(station, START_DATE, END_DATE)
    data = data.fetch()
    
    for index, row in data.iterrows():
        cursor.execute('''
            INSERT INTO historic_meteo_data (city, date, temperature, precipitation, wind_speed)
            VALUES (%s, %s, %s, %s, %s)
        ''', (city, index.date(), row['tavg'], row['prcp'], row['wspd']))
    
    conn.commit()
    print(f"Données insérées pour {city} ✅")

# Fermeture de la connexion
cursor.close()
conn.close()
print("Importation terminée ")
