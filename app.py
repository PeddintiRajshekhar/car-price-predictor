import streamlit as st
import pandas as pd
import pickle

# Load the trained pipeline
with open("model.pkl", "rb") as f: 
    model = pickle.load(f)

st.title("🚗 Car Price Predictor")

# User input form
st.subheader("Enter Car Details")
year = st.number_input("Year of Manufacture", 1990, 2025, 2017)
km_driven = st.number_input("Kilometers Driven", 0, 500000, 40000)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

# When user clicks Predict
if st.button("Predict Selling Price"):
    input_df = pd.DataFrame([{
        "year": year,
        "km_driven": km_driven,
        "fuel": fuel,
        "seller_type": seller_type,
        "transmission": transmission,
        "owner": owner
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Selling Price: ₹{round(prediction):,}")
