#!/usr/bin/env python
# coding: utf-8

# In[19]:


import requests
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st 
import sqlite3
import google.cloud


# In[20]:


# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
bigquery_client = bigquery.Client()

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
QUERY = """
SELECT name, market_cap, market_cap_change_24h, content, volume_24h, updated_at
FROM crypto_categories.id;
  """

#Run the query and write result to a pandas data frame
Query_Results = bigquery_client.query(QUERY)
df_new = Query_Results.to_dataframe()
#View top few rows of result
df_new.head()

st.dataframe(df_new)







