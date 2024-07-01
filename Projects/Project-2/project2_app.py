import pickle

file = open("sales_pred.pickle", 'rb')
model = pickle.load(file)
file.close()


import streamlit as st


st.write('# Sales Prediction App')

TV = st.number_input("TV sales")

if st.button('Total Sales'):
    y_pred = model.predict([[TV]])
    st.write(y_pred)