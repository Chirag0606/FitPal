import streamlit as st
import pickle
import numpy as np 

#df=pickle.load(open("bmi_data.pkl","rb"))
scaler=pickle.load(open("scaler_bmi.pkl","rb"))
model=pickle.load(open("model_bmi.pkl","rb"))


st.title("FAT Predictor")
Height=st.number_input("Enter Height in inches")
Weight=st.number_input("Enter Weight in pounds")





if st.button("Predict"):
    query=np.array([Height, Weight])
    query=query.reshape(-1,2)
    data=scaler.transform(query)
    value=model.predict(data)
    value=value[0,0]
    st.markdown(f"<h1>{value}</h1>", unsafe_allow_html=True)
    
    