import pickle
import pytest
import pandas as pd

# Charger le modèle et le scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Nouvelles données à tester
new_data = {
    'customer_id': 7442532,
    'credit_lines_outstanding': 5,
    'loan_amt_outstanding': 1958.928726,
    'total_debt_outstanding': 8228.752520,
    'income': 26648.43525,
    'years_employed': 2,
    'fico_score': 572
}

# Convertir le dictionnaire en DataFrame
new_data_df = pd.DataFrame([new_data])

# Appliquer la transformation (scaling) si nécessaire
new_data_scaled = scaler.transform(new_data_df)  # Utilisation du scaler pour normaliser les données

def test_predict():
    # Faire la prédiction avec les données normalisées
    prediction = model.predict(new_data_scaled)
    assert prediction[0] == 1, "Incorrect prediction"

