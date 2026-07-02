import streamlit as st

st.set_page_config(page_title="Diamond Price Prediction", page_icon="💎")

st.title("💎 Diamond Price Prediction System")

st.markdown("---")

st.header("📌About the Project")

st.write("""This project predicts the price of a diamond based on its physical and quality characteristics using Machine Learing. The dataset was cleaned, analyzed, and used to train multiple regression models.""")

st.header("📊dataset information")

st.write("""
         - Dataset : Diamonds Dataset
         - Total Records : 53,920
         - Features Used :
             - Carat
             - Cut
             - Color
             - Clarity
             - Depth
             - Table
             - x
             - y
             - z
         - Target Variable :
             - Price
         """ )

st.header("🤖Machine Learning Models")

st.write("""
         - Linear Regression
         - Decision Tree Regressor
         - Random Forest Regressor ( Best Model)
         """)

st.header("🏆Model Performance")

st.write("""
         - Linear Regression R² Score : 0.88
         - Decision Tree R² Score : 0.999966
         - Random Forest R² Score : 0.999971
         """ )

st.success("Use the 'Page 1' option from the sidebar to predict diamond prices.")