import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
import pandas as pd
import joblib


model = joblib.load("models/best_model.pkl")

st.write("Merhaba !")

st.sidebar.write("Bu bir sidebar yazısıdır.")

education = st.sidebar.selectbox("Eğitim Durumu",['Bachelors', 'Masters', 'PHD'])
year = st.sidebar.slider("Joining Year", 2010, 2018, 2015)
city = st.sidebar.selectbox("City ",['Bangalore', 'Pune', 'New Delhi']) 
PaymentTier = st.sidebar.number_input("Payment Tier", min_value=1, max_value=10, value=1)
age = st.sidebar.slider("Age", 18, 55, 25)
Gender = st.sidebar.radio("Gender",["Male","Female"])
EverBenched = st.sidebar.radio("EverBenched",["Yes","No"])
ExperienceInCurrentDomain = st.sidebar.number_input("Experiment", min_value=1, max_value=10, value=1)

df = pd.DataFrame(
    {
        'Education' : [education], 
        'JoiningYear':[year],
        'City':[city],
        'PaymentTier':[PaymentTier],
         'Age':[age],
        'Gender':[Gender],
       'EverBenched':[EverBenched], 
       'ExperienceInCurrentDomain':[ExperienceInCurrentDomain]
       })
st.write(df)
sonuc = model.predict(df)
if (sonuc==[0]):
    st.error("Bu kişi istifa edebilir.")
else:
    st.success("Bu kişi istifa etmeyecektir.")