from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

def build_global_model(preprocessor):
    return Pipeline([
        ('preprocessing', preprocessor),
        ('regressor', XGBRegressor(
            colsample_bytree=1, gamma=1, learning_rate=0.1,
            max_depth=5, n_estimators=200, reg_alpha=0.1,
            reg_lambda=2, subsample=1, random_state=42, n_jobs=-1
        ))
    ])

def build_specific_model(preprocessor_eq):
    return Pipeline([
        ('preprocessing', preprocessor_eq),
        ('regressor', XGBRegressor(
            colsample_bytree=1, gamma=3, learning_rate=0.1,
            max_depth=4, n_estimators=None, reg_alpha=2,
            reg_lambda=2, subsample=1, random_state=42, n_jobs=-1
        ))
    ])
