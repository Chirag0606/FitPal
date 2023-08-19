import streamlit as st
import pickle
import numpy as np 

df=pickle.load(open("fat_data.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))


st.title("FAT Predictor")
Weight=st.number_input("Enter Weight")
Height=st.number_input("Enter Height")
Chest=st.number_input("Enter Chest")
Abdomen=st.number_input("Enter Abdomen")
Hip=st.number_input("Enter Hip")
Thigh=st.number_input("Enter Thigh")




if st.button("Predict"):
    query=np.array([Weight, Height, Chest, Abdomen, Hip, Thigh])
    query=query.reshape(-1,6)
    data=scaler.transform(query)
    value=model.predict(data)
    
    st.text(value)
    
    