from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def get_preprocessor():
    cat_col = ['profil_cotier','saison','city']
    return ColumnTransformer([
        ('cat_col', OneHotEncoder(handle_unknown='ignore'), cat_col)
    ], remainder='passthrough')

def get_preprocessor_eq():
    cat_col_eq = ['city', 'profil_cotier']
    return ColumnTransformer([
        ('cat_col_eq', OneHotEncoder(handle_unknown='ignore'), cat_col_eq)
    ], remainder='passthrough')
