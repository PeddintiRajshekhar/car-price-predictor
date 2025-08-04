# 🚗 Car Price Predictor App

A **Streamlit web application** that predicts the **resale price of a used car** based on key features like fuel type, ownership, kilometers driven, transmission type, and more. Built using a **Linear Regression pipeline** with **scikit-learn**, and designed for easy, real-time predictions.

---

## 📌 Features

- 💻 Streamlit-based UI for user-friendly interaction
- 🧠 Trained ML model using:
  - OneHotEncoding (for categorical variables)
  - Feature scaling (StandardScaler)
  - Linear Regression (baseline model)
- 🔄 Easily extendable to Random Forest or XGBoost
- 🗃️ Ready for deployment on Streamlit Cloud

---

## 📊 Input Features

| Feature         | Description                           |
|----------------|---------------------------------------|
| `year`          | Year of manufacture                   |
| `km_driven`     | Kilometers driven by the car          |
| `fuel`          | Fuel type (Petrol, Diesel, CNG, etc.) |
| `seller_type`   | Individual or Dealer                  |
| `transmission`  | Manual or Automatic                   |
| `owner`         | Ownership history                     |

---

## 🧠 Model

The machine learning pipeline uses:

- **Preprocessing**: 
  - OneHotEncoder for categorical variables
  - StandardScaler for numeric variables
- **Model**: 
  - Linear Regression from `sklearn.linear_model`

> Note: Model saved as `model.pkl` and loaded into `app.py`

---

## 🚀 Running the App Locally

### 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
