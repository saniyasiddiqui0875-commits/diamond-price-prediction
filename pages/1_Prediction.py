import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("diamond_model.pkl", "rb"))

st.title("💎 Diamond Price Prediction")

st.write("Enter the diamond details below and click **Predict Price.")

st.markdown("---")

carat = st.number_input("Carat", min_value=0.0, value=1.0)

cut = st.number_input("Cut (Encoded)", min_value=0, value=0)

color = st.number_input("Color (Encoded)", min_value=0, value=0)

clarity = st.number_input("Clarity (Encoded)", min_value=0, value=0)

depth = st.number_input("Depth", value=61.5)

table = st.number_input("Table", value=57.0)

x = st.number_input("Length (x)", value=5.5)

y = st.number_input("Width (y)", value=5.5)

z = st.number_input("Depth (z)", value=3.5)

if st.button("Predict Price"):
    data = pd.DataFrame({"carat" : [carat], "cut" : [cut], "color" : [color], "clarity" : [clarity], "depth" : [depth], "table" : [table], "x" : [x], "y" : [y], "z" : [z]})

prediction = model.predict(data)

st.success("Prediction Successful! 🎉")
st.subheader(f"💰 Predicted Diamond Price : ${round(prediction[0])}")