import streamlit 
import streamlit as st

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title("Welcome to my awesome data science project!")
    st.text("In this project I look into the transaction of this in NYC. ...")
    
with dataset:
    st.header("NYC taxi dataset")
    st.text("I found this dataset on blablabla.com, ....")
    
with features: 
    st.header("The features I created")

with model_training:
    st.header("Time to train the model!")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance changes!")