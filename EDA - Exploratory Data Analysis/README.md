
#  Exploratory Data Analysis (EDA) – Sales & Weather Predictor

> **Auteur :** Salma Souissi  
> **Date :** fin d'Avril 2025  
> **Contexte :** Analyse exploratoire d’un jeu de données synthétiques de ventes de produits de grande consommation, enrichi par des indicateurs météo et calendrier (Ramadan, Nouvel An, week‑ends, vacances scolaires, etc.).

---

##  Structure du notebook

1. **Chargement & structure des données**  
   - Lecture du CSV, conversion des dates, aperçu des dimensions et des types.  
   - Vérification de la **propreté** : **aucune valeur manquante**, pas de doublons.

2. **Statistiques descriptives & distributions**  
   - Histogrammes et boxplots pour :  
     - Variables climatiques (`température`, `humidity`, `vitesse_vent`, `precipitation`)  
     - Ventes quotidiennes moyennes par produit  
   - Identification des outliers et premières observations de forme.

3. **Analyse des corrélations**  
   - Heatmap des corrélations entre variables météo et ventes.  
   - Étude des **lags** (J‑1, J‑3, J‑7) : stabilité des corrélations dans le temps.  
   - Focus sur : crème solaire, ustensiles jetables, boissons chaudes, etc.

4. **Effets saisonniers & événements spéciaux**  
   - Comparaison des moyennes de ventes selon :  
     - Ramadan, Nouvel An, week‑ends/jours fériés  
     - Vacances scolaires  
   - Visualisations barplots et lineplots dédiés.

5. **Comparaison quotidienne autour des fêtes**  
   - Moyennes des ventes & températures sur 30 déc, 31 déc, 1 janv (toutes années).  
   - Faceted plots combinant barres (ventes) et courbes (température) pour plusieurs produits.

6. **Profil côtier & géographie**  
   - Analyse des ventes selon `profil_cotier` (Hors‑côtier, Côtière, Intérieure).  
   - Ajustement de coefficients synthétiques et interprétation des dynamiques régionales.

7. **Interactions météo–lag & combinatoire**  
   - Catégorisation “Aujourd’hui H/B” × “Lag H/B” → 4 combinaisons (BB, BH, HB, HH).  
   - Pointplots et barplots pour plusieurs produits (boissons, crème solaire, jardinage).

8. **Synthèse des patterns**  
   - Corrélations fortes positives (p. ex. crème solaire ↔ temp_lag1) et négatives (boissons chaudes ↔ temp).  
   - Corrélations faibles et explications supplémentaires (charbon, équipements d’urgence).

9. **Interprétation & implication commerciale**  
   - Traduction des insights en **recommandations :  
     - Promotions météo‑sensibles  
     - Bundles produits (“apéro estival”, “pause gourmande”, “packs prévention anti‑moustiques”)  
     - Optimisation des stocks et logistique selon les prévisions.**

10. **Conclusion & perspectives**  
    - Le jeu de données est **complet**, **cohérent**, prêt pour la modélisation.  
    - Mise en place d’une **infrastructure flexible** (modèle + UI) pour réentraîner rapidement sur données réelles.  

---

##  Prérequis

- Python ≥ 3.8  
- Packages : `pandas`, `numpy`, `matplotlib`, `seaborn`  
- Optionnel : `jupyter` ou `jupyterlab`

---

##  Utilisation

1. Cloner ce dépôt :  
   ```bash
   git clone https://github.com/souissi-salma/Sales_Weather_Predictor.git
   cd Sales_Weather_Predictor/EDA\ -\ Exploratory\ Data\ Analysis
   ```


2. Lancer le notebook :

   ```bash
   jupyter notebook Exploratory_Data_Analysis\ (EDA).ipynb
   ```
3. Exécuter les cellules dans l’ordre pour reproduire les analyses et visualisations
*  **télécharger le csv data.csv ici [DATA.csv](https://drive.google.com/drive/u/0/folders/1z5AtyTt7R6i-sNzT19i-5ZRhojKX4QfX)**

---

##  Insights clés

* **Effet immédiat et prolongé** de la météo (lag1, lag3, lag7) sur les ventes de produits météo‑sensibles (crème solaire, boissons fraîches, ustensiles jetables).
* **Pics de consommation** lors d’événements : Ramadan (+30 %), Nouvel An (+30 %), vacances scolaires (+13 % jardinage).
* **Corrélations croisées** révélant des opportunités de bundling (boissons + snacks salés, café + sucreries).
* **Faible sensibilité** de certaines catégories (charbon, hydratants) – à traiter via des événements plutôt que la météo.

---
## REMARQUE : 
**VOUS POUVEZ TROUVER TOUTES LES VISUAISATIONS [ICI.](https://github.com/souissi-salma/Sales_Weather_Predictor/tree/main/EDA%20-%20Exploratory%20Data%20Analysis/figure)**

##  Prochaines étapes

* **Modélisation prédictive** : régression linéaire, forêts aléatoires, réseaux neuronaux.
* **Déploiement** : création d’une interface  pour importer un CSV client, récupérer la météo, générer et visualiser des prévisions en temps réel.<br>
❗❗ **même si les données sont fictives, ce travail permet déjà de préparer un modèle flexible et de concevoir une infrastructure solide (modèle + interface utilisateur). Cela veut dire qu’à l’avenir, si des données réelles deviennent disponibles, il suffira de réentraîner le modèle sans tout recommencer de zéro. Cette approche rend le projet pérenne et facilement adaptable pour une utilisation réelle plus tard.**

---

> **Contact :** Salma Souissi – *Étudiante en Data Science*
> **Dépôt** : [https://github.com/souissi-salma/Sales\_Weather\_Predictor](https://github.com/souissi-salma/Sales_Weather_Predictor)

```
```

