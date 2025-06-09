import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path)

    targets = [
        'boissons fraiches', 'boissons chaudes', 'snacks sucrés',
        'snacks salés', 'produits laitiers frais', 'produits de jardinage',
        'ustensiles jetables', 'crème solaire', 'équipements d urgence',
        'soins hygiene', 'soins hydratants', 'Charbon',
        'produits anti_moustiques'
    ]

    drop_cols = ['date'] + targets
    X = df.drop(columns=drop_cols)
    y = df[targets]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    return X_train, X_test, y_train, y_test
