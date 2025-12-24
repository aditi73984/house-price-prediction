# 🏠 House Price Prediction System

A full-stack Machine Learning web application that predicts house prices based on key property features using a real-world Kaggle dataset.  
The system is designed with a clean user interface and a robust backend API, making it easy for users to estimate house prices accurately.

---

## 📌 Project Overview

The House Price Prediction System uses a **machine learning regression model** trained on real housing data to predict the estimated price of a house.  
Users enter basic house details such as quality, living area, garage capacity, and basement area, and the system returns an estimated price instantly.

This project demonstrates:
- Practical use of Machine Learning
- Backend API development
- Frontend–Backend integration
- Real dataset usage
- Deployment-ready architecture

---

## 🎯 Objectives

- To predict house prices using historical data
- To apply machine learning in real-life scenarios
- To build a user-friendly web interface
- To integrate ML models with a web application
- To deploy the system for real-world usage

---

## 🧠 Machine Learning Details

- **Algorithm Used:** Linear Regression
- **Why Linear Regression?**
  - Simple and interpretable
  - Works well for continuous price prediction
  - Efficient for small to medium-sized datasets

- **Input Features:**
  - Overall Quality (1–10)
  - Living Area (sq ft)
  - Garage Capacity (number of cars)
  - Basement Area (sq ft)

- **Target Variable:**
  - Sale Price

- **Model Output:**
  - Predicted house price

---

## 📊 Dataset Information

- **Source:** Kaggle  
- **Dataset Name:** House Prices – Advanced Regression Techniques  
- **Link:** https://www.kaggle.com/c/house-prices-advanced-regression-techniques

The dataset contains detailed information about residential homes, including size, quality, and price.

---

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS
- JavaScript
- Font Awesome Icons

### Backend
- Python
- FastAPI
- Pydantic

### Machine Learning
- Pandas
- NumPy
- Scikit-learn

---

## 📁 Project Structure

house-price-prediction/
│
├── backend/
│ ├── model/
│ │ └── house_model.pkl
│ ├── main.py
│ ├── train_model.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── data/
│ └── train.csv
│
└── README.md




---

## ⚙️ How the System Works

1. User enters house details in the frontend form
2. Frontend sends data to backend API using HTTP POST request
3. Backend loads the trained ML model
4. Model predicts the house price
5. Predicted price is returned to frontend
6. Result is displayed to the user instantly

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/aditi73984/house-price-prediction.git
cd house-price-prediction
 ```
### 2️⃣ Train the Machine Learning Model
cd backend
python train_model.py


This will generate:

backend/model/house_model.pkl

### 3️⃣ Run Backend Server
uvicorn main:app --reload


Backend will run at:

http://127.0.0.1:8000


Swagger API Docs:

http://127.0.0.1:8000/docs

### 4️⃣ Run Frontend
cd frontend
python -m http.server 5500


Open in browser:

http://localhost:5500

🧪 Sample Input
{
  "OverallQual": 7,
  "GrLivArea": 1500,
  "GarageCars": 2,
  "TotalBsmtSF": 800
}

Sample Output
Predicted Price: ₹ 1,85,000

### ✨ Features

Real-world dataset

Instant price prediction

Clean and modern UI

User-friendly inputs

Backend API with FastAPI

Easy deployment

Academic project ready

### 🚀 Future Enhancements

Use advanced models (Random Forest, XGBoost)

Add more house features

Display model accuracy and graphs

Add user authentication

Improve prediction accuracy

Deploy with database support

### 🙏 Acknowledgement

Special thanks to all open-source contributors and Kaggle for providing the dataset that made this project possible.

## 👩‍💻 Developed By
**Aditi**
🔗 GitHub: https://github.com/aditi73984/
