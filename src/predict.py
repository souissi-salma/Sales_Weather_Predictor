import numpy as np

def predict_hybride(global_model, specific_model, X_test, X_test_eq):
    y_pred_global = global_model.predict(X_test)
    y_pred_eq = specific_model.predict(X_test_eq).reshape(-1, 1)
    return np.concatenate([y_pred_global, y_pred_eq], axis=1)
