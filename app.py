import streamlit as st
import requests

st.title("🏡 Bengaluru Real Estate Price Predictor")
st.write("Enter the property details below to estimate the price in Lakhs (₹).")

# Create input fields for the Indian housing market
total_sqft = st.number_input("Total Square Feet", value=1200.0, step=100.0)
bhk = st.number_input("Number of Bedrooms (BHK)", value=2.0, step=1.0)
bath = st.number_input("Number of Bathrooms", value=2.0, step=1.0)
balcony = st.number_input("Number of Balconies", value=1.0, step=1.0)

if st.button("Estimate Price"):
    # Prepare the data payload
    payload = {
        "total_sqft": total_sqft,
        "bath": bath,
        "balcony": balcony,
        "bhk": bhk
    }
    
    # Send the data to your FastAPI backend
    try:
        response = requests.post("[https://bengaluru-api.onrender.com/predict](https://bengaluru-api.onrender.com/predict)", json=payload)
        result = response.json()
        estimated_value = result["estimated_value_in_lakhs"]
        
        st.success(f"### Estimated Price: ₹ {estimated_value:,.2f} Lakhs")
    except Exception as e:
        st.error("Error: Could not connect to the API. Is it running?")
