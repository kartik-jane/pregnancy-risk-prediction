# 🤰 Pregnancy Risk Prediction System
A machine learning-based web application that predicts pregnancy risk level (Low, Medium, or High) using maternal and fetal health parameters.

Developed as a capstone project by Kartik Jane from Priyadarshini College of Engineering, Nagpur.

## 📌 Problem Statement
Early prediction of pregnancy-related complications is crucial for ensuring maternal and fetal health. Manual assessments are time-consuming and subjective. This project aims to build an intelligent ML-based system that automatically classifies pregnancy risk level based on medical data.

## 💡 Proposed Solution
This system takes 24 clinical input features related to the mother and fetus, and predicts the pregnancy risk level (Low, Medium, or High) using classification algorithms. The solution is deployed as an interactive web app using Streamlit.

## 🔧 Technologies Used
Python

Scikit-learn

Pandas, NumPy

imbalanced-learn (SMOTE)

Joblib (Model Saving)

Streamlit (Web App)

## 📊 Features Used
Maternal Age, Blood Pressure, Heart Rate, Blood Sugar, Temperature

Fetal Heart Rate, ECG, Movements, Position

Pregnancy History (Multiple pregnancy, Preterm labor, etc.)

Total: 24 features from maternal and fetal records

## 🧠 Machine Learning Models
Model	Accuracy	Notes
Logistic Regression	70.0%	--Best pre-SMOTE
Random Forest + SMOTE	44.0%--	Better class-wise balance
Gradient Boosting	58.0%	--Balanced, slower training
SVM	54.0%	--Requires feature scaling
Naive Bayes	50.0%--	Fast but lower performance

Model selection was based on both accuracy and class-wise F1-score. Final deployment used Logistic Regression.
#
PregnancyRiskPrediction/


├── app.py                    # Streamlit web application

├── main.py                   # Model training and prediction runner

├── requirements.txt          # Python dependencies

├── README.md                 # Project documentation

├── .gitignore                # Git ignore rules

├── data/

   └── Maternal fetal data.xlsx    # Raw input dataset

├── models/

   └── best_model.pkl              # Saved trained ML model

├── src/                            # Source code

   ── preprocessing.py            # Data preprocessing script
   
   ── model.py                    # ML model training and evaluation


## 🚀 How to Run Locally
Clone the repo:

bash
Copy
Edit
git clone https://github.com/kartik-jane/pregnancy-risk-prediction.git
cd pregnancy-risk-prediction
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # On Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py



## 📚 Dataset
The dataset consists of 1,000 anonymized maternal-fetal records with 24 clinical features. (Included in /data/)

🙋 Author
Name: Kartik Wasudeo Jane

College: Priyadarshini College of Engineering, Nagpur

Email: kartikjane26@gmail.com
