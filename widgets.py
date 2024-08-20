import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your query: ")

age = st.slider("Select your age:",0,100)
st.write(f"Your age is, {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language:", options)
st.write(f"You selected, {choice}")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)   

uploaded_file = st.file_uploader("Choose a csv file",type='csv')

if uploaded_file is not None:
  df=pd.read_csv(uploaded_file)   