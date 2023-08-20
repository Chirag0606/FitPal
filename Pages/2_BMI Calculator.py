import streamlit as st
import pickle
import numpy as np

st.title("BMI Calculator")
st.sidebar.success("You are currently viewing BMI Calculator")
st.write("##")
st.sidebar.subheader(
    "Success is usually the culmination of controlling failure.")


scaler = pickle.load(open("scaler_bmi.pkl", "rb"))
model = pickle.load(open("model_bmi.pkl", "rb"))


Height = st.number_input("Enter Height (inc)")
Weight = st.number_input("Enter Weight (lbs)")


if st.button("Predict"):
    query = np.array([Height, Weight])
    query = query.reshape(-1, 2)
    data = scaler.transform(query)
    value = model.predict(data)
    value = value[0, 0]
    st.markdown(f"<h1>{value}</h1>", unsafe_allow_html=True)
