
   
import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Project 1 - Cryptocurrency Category Analysis", Crypto_Category.app)
app.add_app("Project 2 - Banking Industry Churn Prediction", Model_Bank_Defaulters.app)
app.add_app("Project 3 - Company Decision Support System", SQClassProject.app)
app.add_app("Project 4 - Cryptocurrency Exchanges Analysis", PycharmProjectsTableauCrypto_app.app)
# The main app
app.run(
