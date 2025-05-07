# Diabetes_prediction model
# 🩺 Diabetes Prediction Web App

This project is a simple machine learning-based web application that predicts whether a person has diabetes based on medical input data. It uses the Pima Indians Diabetes dataset and is built with Flask for the web interface.

## 🚀 Features

- Trained a machine learning model using the Pima Indians dataset
- Web app built with Flask to accept user input
- Model is saved using `pickle` for fast prediction
- HTML form to input data such as glucose level, BMI, age, etc.

## 🧠 Machine Learning

- Dataset: `pima-indians-diabetes.data.csv`
- Features include: pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age
- Model: Logistic Regression or other classification algorithm
- Tools: `pandas`, `scikit-learn`, `pickle`

## 🛠️ Project Structure
ML_project/
├── app.py # Flask web app
├── diabetes_model.pkl # Trained ML model
├── pima-indians-diabetes.data.csv # Dataset
├── train_model.py # Script to train and save the model
└── templates/
└── index.html # HTML form for user input


## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/diabetes-prediction-app.git
   cd diabetes-prediction-app
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv venv\Scripts\activate  # On Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Train the model (optional if diabetes_model.pkl already exists):
   ```bash
   python train_model.py
5. Run the Flask app:
   ```bash
   python app.py
6. Open your browser and go to:
   ```bash
   http://127.0.0.1:5000/

## 📷 Screenshots
![Screenshot 2025-05-07 081454](https://github.com/user-attachments/assets/24d2ef73-f39e-4194-861a-5f2594c926ec)
![Screenshot 2025-05-07 081510](https://github.com/user-attachments/assets/b6f75af8-79af-46f4-a077-b2bdb00dbb4a)

## 📦 Dependencies
- Flask
- pandas
- scikit-learn
- pickle (standard library)

## 🙋‍♂️ Author
Your Name - Raghav077


