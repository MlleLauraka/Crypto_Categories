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


#Set environment variables for your notebook
import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/Laura/Desktop/PYTHON/GoogleCloud/cryptoexchanges-342000-e51abbfb4d83.json'
#Imports google cloud client library and initiates BQ service
from google.cloud import bigquery
bigquery_client = bigquery.Client()
#Write Query on BQ
QUERY = """
SELECT name, market_cap, market_cap_change_24h, content, volume_24h, updated_at
FROM crypto_categories.id;
  """
#Run the query and write result to a pandas data frame
Query_Results = bigquery_client.query(QUERY)
df_new = Query_Results.to_dataframe()
#View top few rows of result
df_new.head()


# In[21]:


st.dataframe(df_new)


# In[ ]:




