import streamlit as st
import mysql.connector as connection
import pandas as pd


def app():
    st.title('SQL Company Metrics Analysis: Attrition Prediction')

    # streamlit_app.py


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return connection.connect(**st.secrets["mysql"])


conn = init_connection()

mydb = conn
query = "Select * from LGBRAND;"
result_dataFrame = pd.read_sql(query, mydb)
mydb.close()  # close the connection

st.dataframe(result_dataFrame)
