#importe la bibliothèque requests, qui est utilisée pour envoyer des requêtes HTTP en Python
import requests
# Liste des 24 gouvernorats de la Tunisie
gouvernorats = [
    "Tunis", "Ariana", "Ben Arous", "Manouba", "Nabeul", "Zaghouan", "Bizerte", "Beja", "Jendouba", "Kef",
    "Siliana", "Kasserine", "Sidi Bouzid", "Kairouan", "Kébili", "Tozeur", "Gabès", "Medenine", "Tataouine",
    "Mahdia", "Monastir", "Sousse", "Kairouan", "Sfax", "Gafsa"
]

# Fonction pour obtenir les coordonnées d'un lieu via l'API Nominatim
def get_coordinates(city_name):
    url = f"https://nominatim.openstreetmap.org/search?q={city_name},Tunisia&format=json&addressdetails=1"
    headers = {
        'User-Agent': 'MyApp/1.0 (souissisalma.fsm@gmail.com)'  #  User-Agent 
    }
    réponse = requests.get(url ,headers=headers) #récupèrer la réponse de l'API et la stocke dans la variable réponse
    data = réponse.json() #transformer la réponse de l'API en format JSON en un dictionnaire Python.

    if data: #si data n'est pas vide
        #l'API retourne une liste signifie que même si on attend à un seul résultat on doit accéder au premier élément de cette liste pour obtenir les informations souhaitées.
        lat = float(data[0]["lat"])#extraire la latitude ("lat") et la convertit également en un nombre décimal (float).
        lon = float(data[0]["lon"])#extraire la longitude ("lon") et la convertit également en un nombre décimal (float).
        return lat, lon
    else:
        return None, None

# Récupérer et afficher les coordonnées pour chaque gouvernorat
for gouvernorat in gouvernorats:
    lat, lon = get_coordinates(gouvernorat)
    if lat and lon:
        print(f"Coordonnées de {gouvernorat}: Latitude = {lat}, Longitude = {lon}")
    else:
        print(f"Coordonnées non trouvées pour {gouvernorat}")


#stocker les données des gouvernorats dans une base de données SQL 
import psycopg2
from psycopg2 import sql
# Connexion à la base de données PostgreSQL
conn = None
cur = None
try:
    conn = psycopg2.connect(
        dbname="meteo_data",  
        user="postgres", 
        password="", 
        host="localhost",  
        port="5432" )
    cur = conn.cursor() # pour exécuter des commandes SQL.

    # Insérer les données dans la table 'gouvernorats'
    for gouvernorat in gouvernorats:
        lat, lon = get_coordinates(gouvernorat)
        if lat and lon:
            #Gestion des erreurs
            try:
                cur.execute(
                    sql.SQL("INSERT INTO gouvernorats (nom, latitude, longitude) VALUES (%s, %s, %s)"),
                    [gouvernorat, lat, lon]
                )
                print(f"Coordonnées de {gouvernorat} insérées avec succès.")
            except Exception as e:
                print(f"Erreur d'insertion pour {gouvernorat}: {e}")
        else:
            print(f"Coordonnées non trouvées pour {gouvernorat}")
    
    # Commit des changements et fermer la connexion
    conn.commit()

except Exception as e:
    print(f"Erreur de connexion à la base de données : {e}")
#Fermeture de la connexion
finally:
    # Vérifier si la connexion et le curseur existent avant de les fermer
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
