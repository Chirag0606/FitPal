import streamlit as st
import pickle
import numpy as np 


st.title("Body Fat Calculator")
st.sidebar.success("You are currently viewing Body Fat Calculator")


df=pickle.load(open("fat_data.pkl","rb"))
scaler=pickle.load(open("scaler.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))


Weight=st.number_input("Enter Weight (lbs)")
Height=st.number_input("Enter Height (inc)")
Chest=st.number_input("Enter Chest (cm)")
Abdomen=st.number_input("Enter Abdomen (cm)")
Hip=st.number_input("Enter Hip (cm)")
Thigh=st.number_input("Enter Thigh (cm)")


if st.button("Predict"):
    query=np.array([Weight, Height, Chest, Abdomen, Hip, Thigh])
    query=query.reshape(-1,6)
    data=scaler.transform(query)
    value=model.predict(data)

    value=value[0,0]
    st.markdown(f"<h1>{value}</h1>", unsafe_allow_html=True)

    
    
