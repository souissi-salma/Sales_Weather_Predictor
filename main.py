from src.data_loader import load_data
from src.preprocessing import get_preprocessor, get_preprocessor_eq
from src.models import build_global_model, build_specific_model
from src.predict import predict_hybride
from src.evaluation import eval_produit_par_produit, eval_global
import pandas as pd

# Chargement des données
X_train, X_test, y_train, y_test = load_data('data/DATA.csv')

# Ciblage
y_train_eq = y_train[['équipements d urgence']]
y_test_eq = y_test[['équipements d urgence']]
y_train_global = y_train.drop(columns='équipements d urgence')
y_test_global = y_test.drop(columns='équipements d urgence')

# Variables pour le modèle spécifique
cols_eq = ['température', 'humidity', 'vitesse_vent', 'precipitation', 'temp_lag1',
           'vitesse_vent_lag1', 'precip_lag1', 'vitesse_vent_lag3', 'temp_lag7',
           'vitesse_vent_lag7', 'urgence_active', 'Indice de sécheresse',
           'Indice de Tempête', 'Indice de Pluie Intense', 'city', 'profil_cotier']

X_train_eq = X_train[cols_eq]
X_test_eq = X_test[cols_eq]

# Prétraitement et modèles
preprocessor = get_preprocessor()
preprocessor_eq = get_preprocessor_eq()

global_model = build_global_model(preprocessor)
specific_model = build_specific_model(preprocessor_eq)

# Entraînement
global_model.fit(X_train, y_train_global)
specific_model.fit(X_train_eq, y_train_eq)

# Prédiction et évaluation
y_pred = predict_hybride(global_model, specific_model, X_test, X_test_eq)
y_test_total = pd.concat([y_test_global, y_test_eq], axis=1)

eval_produit_par_produit(y_test_total, y_pred)
eval_global(y_test_total, y_pred)
