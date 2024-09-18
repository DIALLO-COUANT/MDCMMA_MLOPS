from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

scaler = pickle.load(open('scaler.pkl', 'rb'))

def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return int(prediction[0])

# Route principale pour le formulaire
@app.route('/', methods=['GET'])
def Home():
	return render_template("index.html")
	
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        customer_id = int(request.form['customer_id'])
        credit_lines_outstanding = int(request.form['credit_lines_outstanding'])
        loan_amt_outstanding = float(request.form['loan_amt_outstanding'])
        total_debt_outstanding = float(request.form['total_debt_outstanding'])
        income = float(request.form['income'])
        years_employed = int(request.form['years_employed'])
        fico_score = int(request.form['fico_score'])
        prediction = model.predict(
			[[customer_id, credit_lines_outstanding, loan_amt_outstanding, total_debt_outstanding, income, years_employed, fico_score]]
		)
        if prediction[0] == 1:
            return render_template(
                "index.html",
                prediction_text="Le client présente un risque de défaut de paiement",
            )

        else:
            return render_template(
                "index.html", prediction_text="Le client ne présente pas de risque de défaut de paiement"
            )
	
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)






