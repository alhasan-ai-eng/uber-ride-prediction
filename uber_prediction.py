import streamlit as st
import pickle

st.title("Uber Ride Prediction")
ppw=st.number_input("Enter Price:")
p=st.number_input("Enter Population:")
mi=st.number_input("Enter Monthly Income:")
appm=st.number_input("Enter Average Parking Per Month:")
btn=st.button("Predict!")

if btn:
    model=pickle.load(open("uber.pkl","rb"))
    res=model.predict([[ppw,p,mi,appm]])[0]

    st.markdown(f"No. of Weekly Riders: {res}")
