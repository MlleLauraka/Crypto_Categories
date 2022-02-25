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
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '{
  "type": "service_account",
  "project_id": "cryptoexchanges-342000",
  "private_key_id": "e51abbfb4d833551004aaf30621ab67a20b8b6e2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWNEETXhRE6Obf\ntjYKjAXddHw+AyUYmRgCz7RNCkGmb0d9Cm+nCB0RJr2MhWO0a8SdYGncvLGUO/VP\njzrOfUpaq7LlHPeorktxjJlZYCvfhWkFco+heQgdwJZTBgluNxZbtTWcfEj9tad/\n9mqBhISFF6yX532g/0B8NlmWe+DfOYoBWWRdj/s7QAlixq5hyNAZ+1e7qj7QTYvf\nGtUJjhL0Em8Zt7mzqF0A/zznL0ePhqvH4Uq5TKoaXEErTOHvubiWKRqxqG/uzrRs\n8GrasZpCstPB+teTX5zGtw0Z5fzG506Bcb65llB6TLAxOH1lvcGLRU8vJRbxSz8A\nuWtKblgDAgMBAAECggEAFYY7sdAG1mPW60z6gjXO0xGE+JBFVoLvxDyN4B3zOd+9\nvcViMdUhYptTeb7fpX4czDmneZxmdcBOprd8T8qMQa82M0qlYkhdYWQg9rewwO29\nf2QjJbUtSRwUnvQg13fmocGESRy+EuyBj9y5mBkyXdNirwL+f0KW/sRRXUtGbffB\no9zB5Aw4oj6sVeCGaan6YHZdWy+h9cRpp8aKLxyqLnGYow1iX8YI++nkXMRDu/ds\nFY1gQTZ5g4/EIMLuScsYoJDIydDvWWwUGksY2ufOvBhb26Wfg/XLOhyNc+iLSjHP\nFTqloirR+vnt7zmujRt2Humtq4VcRYP1cRvjaq0j5QKBgQDrAZkp+StemlxEjQ2s\nnvQJ9qPyPyHE/hf4Be3Jc7/UUP4IzfStMvGqiivjzciAfjcGGxKnwthC+24Xjlmc\nuIwFoS9xMQOYKbb4Az03a1InEvQMDTR/YTrX8GocaUJQirxtt4ZYPvm8iMbpQJYp\nqJbxLtjBJKxF23yES8qSPNFjJwKBgQDpVu2fS5tgkhErdVeAXS6H4oLEQe6cF4GA\nBAG4+TrdWjhpnSRt5MbqrUq3mBCsWkolBl9teDlnX0E1PDFAe9VN5kjaSNohtmHJ\n4zDQbLkgClN44+3Gb/Cr4lckVa0NkH/OL7g/l+yD25n+o64OW7caSJFOasKHTvsu\nvaqpwuV9xQKBgQDT3PYDNCJYQFsMZgm85PRngxZcj3PXT6e2L0onQpXfSEEtGNgL\nyRC7yaM11VB8Hs1mUMPpwCwNfvTKgcfiFTIO5TiLGEAATyMnxmvK6ZL/rQOdVc5N\nRA+zm4deI7roN5sWYszYA7ZLtRd2M4bs+ZNSzgQVZAV3WR+ReW6flfrDIwKBgQCL\nuMTDDRf2JKDpX/NMZv+02HqrIDvL9ftSd5O8emi4IQ0EmNc2grZl0eyasRDS06Hw\nN7euqj3dW1mFkgx/62bXpZxcMSGE7Fvz8vnI5EGaIPTIv9siZuc7VWYO2MquA6e0\nBDkUw1kZv8afhs1zxZGHyIpR5XWkZjPcUjA+RPj8bQKBgGedU/Dp6APp8zC973ef\nLP/JdLr7ncHm5MVJAWeTaWKfMFQIA4ztKXf9ae0kXQYra+pnyEiTu8zy35uH3uoV\nTWp2wzuNIdcgksxA+15U5D59oMH/kolW0+qU0/rrByjkeP3Mn343NUmkXh47D1MG\nAUAEYochsjKTr1reigQT0Gtn\n-----END PRIVATE KEY-----\n",
  "client_email": "analytic@cryptoexchanges-342000.iam.gserviceaccount.com",
  "client_id": "110907387757423418496",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/analytic%40cryptoexchanges-342000.iam.gserviceaccount.com"
}'
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




