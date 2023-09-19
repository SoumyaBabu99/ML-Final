import streamlit as st
import numpy as np
import pickle

with open("rf_model.pickle",'rb') as f:
    model = pickle.load(f)
f.close()

st.title("Crimes against Women")
st.subheader('Predicting domestic violence against women')


dowry = st.number_input('Dowry daeths:', min_value=0)
murder = st.number_input('Murder with Rape :', min_value=0)
acid =  st.number_input('Acid Attack :', min_value=0)
kidnap = st.number_input('Kidnapping & Abduction :', min_value=0)
procure = st.number_input('Procuration of Minor Girls :', min_value=0)
child = st.number_input('Sexual Assault of Children :', min_value=0)
year = st.selectbox("Select a Year:", list(range(2010, 2025)))
total = st.number_input('Total crimes:', min_value=0)

def predict():
    input_val = np.array([dowry, murder, acid, kidnap, procure, child, year, total]).reshape(1,-1)
    return int(model.predict(input_val).round())

if st.button("Submit"):
    output = "The number of predicted crimes : " + str(predict())
    st.write(output)
