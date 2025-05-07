# 🩺 Diabetes Prediction Web App

This project is a machine learning-based web application that predicts whether a person has diabetes based on health input data. It uses the Pima Indians Diabetes dataset and Flask for the user interface.

## 🚀 Features

- Predicts diabetes using a trained ML model
- Web interface built with Flask and HTML
- Trained model saved using `pickle`
- Clean input form for easy user interaction

## 🛠️ Project Structure

```
ML_project/
├── app.py                          # Flask web application
├── diabetes_model.pkl              # Trained machine learning model (saved using pickle)
├── pima-indians-diabetes.data.csv # Dataset used for training
├── train_model.py                  # Script to train and export the model
└── templates/
    └── index.html                  # HTML template for user input form
```

## 💻 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app/ML_project
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model (optional if `diabetes_model.pkl` exists)
```bash
python train_model.py
```

### 5. Run the Flask app
```bash
python app.py
```

### 6. Open your browser and visit
```
http://127.0.0.1:5000/
```

## 📦 Requirements

The project uses the following Python libraries:

```
Flask==2.3.2
pandas==2.2.1
scikit-learn==1.4.1
numpy==1.26.4
```

Install with:
```bash
pip install -r requirements.txt
```

## 📷 Screenshots

_Add screenshots here if you'd like to show the web UI._

## 📄 License

This project is licensed under the MIT License.

## 🙋‍♂️ Author

- **Your Name** – [@your_github](https://github.com/your-username)
