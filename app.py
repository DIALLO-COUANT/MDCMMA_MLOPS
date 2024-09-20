from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Charger le modèle et le scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        customer_id = int(request.form['customer_id'])
        credit_lines_outstanding = int(request.form['credit_lines_outstanding'])
        loan_amt_outstanding = float(request.form['loan_amt_outstanding'])
        total_debt_outstanding = float(request.form['total_debt_outstanding'])
        income = float(request.form['income'])
        years_employed = int(request.form['years_employed'])
        fico_score = int(request.form['fico_score'])

        # Créer un tableau avec les valeurs saisies
        features = [[customer_id, credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score]]

        # Appliquer le scaler pour normaliser les données
        scaled_features = scaler.transform(features)

        # Faire une prédiction avec le modèle
        prediction = model.predict(scaled_features)

        # Préparer le texte de la prédiction pour l'afficher dans l'interface utilisateur
        if prediction[0] == 1:
            prediction_text = "Le client présente un risque de défaut de paiement"
        else:
            prediction_text = "Le client ne présente pas de risque de défaut de paiement"

        # Renvoyer le formulaire et afficher la prédiction
        return render_template("index.html", prediction_text=prediction_text)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
