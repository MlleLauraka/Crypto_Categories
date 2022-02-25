#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st 


# In[4]:


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Crypto Categories Dashboard", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="Crypto_Categories.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="B:R",
        nrows=143,
    )

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
Name = st.sidebar.multiselect(
    "Select the Category:",
    options=df["name"].unique(),
    default=df["name"].unique()
)


df_selection = df.query(
    "Name == @name"
)

# ---- MAINPAGE ----
st.title(":bar_chart: Crypto Categories Dashboard")
st.markdown("##")

total_sales = int(df_selection["name"].count())
total_sales 
# TOP KPI's
number_categories = int(df_selection["name"].count())
average_rating_mc = round(df_selection["market_cap_change_24h"].mean(), 1)
average_rating_vm = round(df_selection["volume_24h"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Categories Number:")
    st.subheader(f" {number_categories:,}")
with middle_column:
    st.subheader("Market Capitalization Change (24h):")
    st.subheader(f"US ${average_rating_mc}")
with right_column:
    st.subheader("Average Market Volume:")
    st.subheader(f"US $ {average_rating_vm}")

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
market_cap_chart = (
    df_selection.groupby(by=["name"])[["market_cap"]].sort_values(by="market_cap").sum()
)
fig_product_sales = px.bar(
    market_cap_chart,
    x="market_cap",
    y=market_cap_chart.index,
    orientation="h",
    title="<b>Market Capitalization by Category </b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# SALES BY HOUR [BAR CHART]
volume_chart = df_selection.groupby(by=["name"]).sum()[["volume_24h"]]
fig_hourly_sales = px.bar(
    volume_chart,
    x=volume_chart.index,
    y="name",
    title="<b>Volume by Category</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# In[ ]:




