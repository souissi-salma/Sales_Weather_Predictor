from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def eval_produit_par_produit(y_true, y_pred):
    for i, produit in enumerate(y_true.columns):
        r2 = r2_score(y_true.iloc[:, i], y_pred[:, i])
        mse = mean_squared_error(y_true.iloc[:, i], y_pred[:, i])
        print(f"Produit : {produit} → R² : {r2:.2f} | MSE : {mse:.2f}")

def eval_global(y_true, y_pred):
    r2 = r2_score(y_true, y_pred, multioutput='uniform_average')
    mse = mean_squared_error(y_true, y_pred, multioutput='uniform_average')
    print(f"\nÉvaluation globale du modèle hybride :\n → R² moyen : {r2:.2f}\n → MSE moyen : {mse:.2f}")
