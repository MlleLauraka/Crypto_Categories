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


# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

    mydb = conn
    query = "Select * from LGBRAND;"
    result_dataFrame = pd.read_sql(query, mydb)
    mydb.close()  # close the connection