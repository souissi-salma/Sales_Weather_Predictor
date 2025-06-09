## 1.  Collecte des Données Climatiques

###  Sources de données

- **Meteostat** : Librairie Python gratuite permettant un accès à des données météorologiques historiques détaillées (stations, résumés quotidiens, etc.).  
➡ Ce choix a été motivé par la **longue période d'historique accessible gratuitement**, essentielle pour des analyses temporelles fiables.

- Données extraites à l’aide de requêtes automatisées en Python
- Ciblage : **24 gouvernorats tunisiens**

---

###  Période couverte

- **De** : 2020  
- **À** : 2025   
- **Fréquence** : Journalière  
Chaque ligne du fichier correspond à une journée et une localisation (gouvernorat).

---

###  Variables collectées

- Température (°C)  
- Humidité (%)  
- Vitesse et direction du vent  
- Précipitations (mm)

---

###  Nouvelles Features Intégrées

####  Variables calendaires

- **Jour de la semaine**
- **Mois**
- **Saisons**
- **Week-ends** (colonne binaire)
- **Jours fériés nationaux**
- **Vacances scolaires**
- **Ramadan**
- **Nouvel An**

➡ Ces variables permettent de mieux modéliser les effets temporels sur les ventes.

####  Variables régionales

- Localisation (gouvernorat)
- Zone côtière (oui/non)
- Niveau d’urbanisation (métropole / ville moyenne / zone rurale)

➡ Permet de comparer les comportements selon le type de zone.

####  Indices météorologiques dérivés

- **Indice de Vague de Chaleur** : température > 35°C pendant 3 jours
- **Indice de Vague de Froid** : température < 9°C pendant 3 jours
- **Indice de Pluie Intense** : précipitations > 50 mm/jour
- **Indice de Tempête** : vitesse du vent > 60 km/h
- **Indice de Sécheresse** : précipitations < 10 mm sur les 20 derniers jours

####  Variables de décalage temporel (lag features)

- Ajout des valeurs météo précédentes à J-1, J-3 et J-7  
➡ Très utile pour la modélisation prédictive, notamment en séries temporelles.

---

## 2.  Génération des Données de Ventes Synthétiques

###  Méthodologie

####  Approche technique

Développement d’un **générateur modulaire Python** basé sur :
- Une **modélisation différente par catégorie de produit**
- Des **coefficients dynamiques** selon :
  - Conditions météo
  - Variables calendaires
  - Localisation géographique

Des mécanismes garantissent le réalisme :
- Plafonds journaliers de ventes
- Bruit aléatoire contrôlé
- Validation statistique

####  Méthode utilisée

- Règles métier simples, inspirées des comportements d'achat réels
- Pas de GAN ou de modèles statistiques avancés  
➡ Choix motivé par l’absence de données réelles

---

###  Produits modélisés

- Boissons (fraîches / chaudes)
- Produits d’hiver : charbon, produits laitiers
- Produits d’été : crèmes solaires, anti-moustiques
- Produits saisonniers : jardinage, …

Chaque produit suit une **logique météo** propre.

---

###  Résultats

- **13 variables synthétiques générées** :('boissons fraiches', 'boissons chaudes', 'snacks sucrés',
       'snacks salés', 'produits laitiers frais', 'produits de jardinage',
       'ustensiles jetables', 'crème solaire', 'équipements d urgence',
       'soins hygiene', 'soins hydratants', 'Charbon',
       'produits anti_moustiques')

- **4 saisons complètes** simulées
- **3 types de régions** intégrées
- **Visualisation des courbes de ventes** pour validation
- **Cohérence temporelle vérifiée**

---

## 3.  Préparation du Dataset Final

###  Fusion des données

- Jointure sur la **date** et le **gouvernorat**
- Chaque ligne : un jour, un gouvernorat, toutes les variables météo + les ventes simulées

###  Format de sortie

- **Fichiers CSV**  
➡ Facile à manipuler et compatible avec les outils de data science et de visualisation.

---


---

##  Auteure

**Souissi Salma**  
Master Data Science – 2025  
Université de Monastir

---




