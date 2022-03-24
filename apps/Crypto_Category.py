##---------------------------------#
#Import dependencies
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import json

#---------------------------------#
def app():
    #---------------------------------#
    # Page Layout
    #st.set_page_config(page_title="Crypto Categories Dashboard", page_icon=":bar_chart:", layout="wide")
    #image = Image.open('/Users/Laura/Downloads/quantitatives-ZAIbez5LTrg-unsplash.jpg')
    st.title(":bar_chart: Crypto Categories Dashboard")
    st.markdown("This app retrieves the Categories performance on the Crypto Market from **CoinGecko**!")


    # About
    expander_bar = st.expander("About")
    expander_bar.markdown("""
    * **Objectif:** Learn about the industries being currently disrupted by the Blockchain Technolgy and their value on the Crypto Market
    * **Python libraries:** Pandas, Streamlit, Numpy, Plotly.express, Json, St_AgGrid
    * **Data source:** [CoinGecko](https://www.coingecko.com/).
    * **Credit:** Websites Plotly, Pandas, StackOverflow and Youtube Channel Data Professor : *[Data Science Web App in Python](https://www.youtube.com/watch?v=ZZ4B0QUHuNc&t=338s)*).
    * **Contact:** *[Laura Kouadio](https://www.linkedin.com/in/laura-kouadio-083374131/)*
    """)

    # Import Json file
    @st.cache
    def load_data():
        data = requests.get('https://api.coingecko.com/api/v3/coins/categories?order=market_cap_desc').text
        data = json.loads(data)
        return data

    data=load_data()

    #Turn it into Dataframe Pd
    df_0 = data
    df = pd. DataFrame(df_0, columns = ['id', 'name',
        "market_cap",
        "market_cap_change_24h",
        "content",
        "top_3_coins",
        "volume_24h",
        "updated_at"] ) #create DataFrame from `data_list`

    df = df.drop(columns=['top_3_coins'], axis = 0)
    pd.options.display.float_format = '{:,}'.format
    df = np.round(df, decimals = 2)
    #df["market_cap_mean"]= df["market_cap"].mean()
    #df["market_cap_mean"] = '$' + (df["market_cap_mean"].astype(float)/1000000).astype(str) + 'MM'

    # TOP KPI's
    number_categories = int(df["name"].count())
    average_rating_mc = round(df["market_cap_change_24h"].mean(),1)
    average_rating_mc_usd = round(df["market_cap"].mean()/1000000, 2)
    average_rating_vm = round(df["volume_24h"].mean(), 2)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.metric(label="Number of Category:", value=f" {number_categories:,}")
    with middle_column:
        st.metric(label="Market Cap 24h:", value=f"$ {average_rating_mc_usd:}MM", delta=(f"{average_rating_mc} %"))
    st.markdown("""---""")

    #---------------------------------#
    # ---- Menu Bar (Side Bar) ---- Find the dropdown filters for categories and Dates

    st.sidebar.header("Please Filter Here:")
    Name = st.sidebar.selectbox(
        "Select a Category:",
        options=df["id"].unique()
    )

    df_selection = df.query(
        "id == @Name"
    )


    #---------------------------------#
    # Main page
    #---- Display the DataFrame on Streamlit app ----
    st.subheader('Categories Analysis')
    df = df.drop(columns=['id'], axis = 0)
    st.write('Here are the Crypto Categories created by CoinGecko: Crypto Industries and Ecosystems are listed')
    st.dataframe(df)

    #Combo MCap & Volume Graph
    fig_vl_mc = px.line(y=df["volume_24h"], x=df["name"], title="Daily Volume & Market by Categories (USD)", template="plotly_white", color=px.Constant("Volume"))
    fig_vl_mc.add_bar(x=df["name"], y=df["market_cap"], name="Market Cap")
    fig_vl_mc.update_layout(
        autosize=False,
        width=1100,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Categories",
        yaxis_title="Volume & Market Cap",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )
    st.plotly_chart(fig_vl_mc)

    st.markdown("""---""")
    st.subheader('Top 10 Category Focus')
    #--Vizu 3
    # Group the 10 Best Categories
    group_10=df.nlargest(n=15, columns=['market_cap'])
    group_10["Color"] = np.where(group_10["market_cap_change_24h"] < -0.0000, 'Negative', 'Positive')
    

    #---------------------------------#


    fig_mc_cg = px.histogram(y=group_10["name"], x=group_10["market_cap_change_24h"], title="Top 15 Categories Market Cap Change 24h(%)", template="plotly_white", color=group_10["Color"]).update_yaxes(categoryorder="total ascending")
    fig_mc_cg.update_traces(ybins_size=1) # can add text=round(df_selection["volume_24h"], 1) if needed
    fig_mc_cg.update_layout(barmode='stack')
    fig_mc_cg.update_layout(
        autosize=False,
        width=1100,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Market Cap Change over 24h",
        yaxis_title="Categories",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
    
    
    st.plotly_chart(fig_mc_cg, use_container_width=True)
    st.write('The Top 15 Cryptocurrencies are determined by Market Capitalization Value')
     
    #--------Single Chosen---------)
    st.markdown("""---""")
    st.subheader('Single Category Analysis')
    st.write('**Please select a Crypto Category in the Sidebar to analyse its performance**')

    #Get Url for signl category coins
    df1=(df_selection['id'].iloc[0])
    df1=str(df1)
    data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category="+df1+"&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d").text
    data = json.loads(data)
    df_single = data
    df_singl = pd.DataFrame(df_single, columns=['id',
                                                 'symbol',
                                                 'name',
                                                 'image',
                                                 'current_price',
                                                 'market_cap',
                                                 'market_cap_rank',
                                                 'fully_diluted_valuation',
                                                 'total_volume',
                                                 'high_24h',
                                                 'low_24h',
                                                 'price_change_24h',
                                                 'price_change_percentage_24h',
                                                 'market_cap_change_24h',
                                                 'market_cap_change_percentage_24h',
                                                 'circulating_supply',
                                                 'total_supply',
                                                 'max_supply',
                                                 'ath_change_percentage',
                                                 'ath_date', 'atl',
                                                 'atl_change_percentage',
                                                 'atl_date',
                                                 'roi',
                                                 'last_updated',
                                                 'price_change_percentage_1h_in_currency',
                                                 'price_change_percentage_24h_in_currency',
                                                 'price_change_percentage_7d_in_currency'
                                                 ])

    df_singl = df_singl.drop(columns=[
    'id',
    'image',
    'fully_diluted_valuation',
    'ath_change_percentage',
    'ath_change_percentage',
    'atl_change_percentage',
    'last_updated',
    'price_change_percentage_24h',
    'ath_date',
    'atl',
    'roi',
    'ath_change_percentage',
    'atl_date',
    'max_supply',
    'market_cap_rank'
    ], axis = 0)


    #For currenncy purpose change Int in Floats
    df_singl['market_cap'] = df_singl['market_cap'].astype(float)
    df_singl['total_volume'] = df_singl['total_volume'].astype(float)
    st.dataframe(df_singl)
    st.write("**The category has** **"+ str(df_singl.size)+"** **digital assets as of today**")
    
    df_selection_group=df_singl.nlargest(n=15, columns=['market_cap']) 

    fig_single = px.histogram(y=df_selection_group["name"], x=df_selection_group["market_cap"], title="Top 15 Crypto Market Capitalization", template="plotly_white").update_yaxes(categoryorder="total ascending")
    fig_single.update_traces(ybins_size=1) # can add text=round(df_selection["volume_24h"], 1) if needed
    fig_single.update_layout(barmode="stack")
    fig_single.update_layout(
        autosize=False,
        width=1100,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Market Capitalization in USD",
        yaxis_title="Top Assets in the Categories Chosen",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    
    fig_single2 = px.histogram(y=df_selection_group["name"], x=df_selection_group["current_price"], title="Price of the Top 15 Crypto by Market Price", template="plotly_white").update_yaxes(categoryorder="total ascending")
    fig_single2.update_traces(ybins_size=1)
    fig_single2.update_layout(barmode="stack")
    fig_single2.update_layout(
        autosize=False,
        width=1100,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Current Price in USD",
        yaxis_title="Top Assets in the Categories Chosen",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    left_column, right_column = st.columns(2)
    right_column.plotly_chart(fig_single2, use_container_width=True)
    left_column.plotly_chart(fig_single, use_container_width=True)
