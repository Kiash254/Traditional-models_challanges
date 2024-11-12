from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the saved model
model = joblib.load('credit_score_model.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Credit Score Prediction System!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input features from the request JSON
        data = request.json
        a = float(data['Annual Income'])
        b = float(data['Monthly Inhand Salary'])
        c = float(data['Number of Bank Accounts'])
        d = float(data['Number of Credit cards'])
        e = float(data['Interest rate'])
        f = float(data['Number of Loans'])
        g = float(data['Average number of days delayed by the person'])
        h = float(data['Number of delayed payments'])
        i = float(data['Credit Mix'])  # Ensure numeric input
        j = float(data['Outstanding Debt'])
        k = float(data['Credit History Age'])
        l = float(data['Monthly Balance'])

        # Prepare the feature array for prediction
        features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        return jsonify({
            'Predicted Credit Score': int(prediction)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
