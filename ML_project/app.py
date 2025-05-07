from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("diabetes_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data.get(key, 0) for key in [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
    ]]
    prediction = model.predict([features])[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
