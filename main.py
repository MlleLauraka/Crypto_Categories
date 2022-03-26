##---------------------------------#
#Import dependencies
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier  , AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score as f1
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from math import sqrt
from PIL import Image
import requests
import json


with st.sidebar:
    choose = option_menu("Menu", ["About", "Project 1", "Project 2", "Project 3", "Project 4"], #https://icons.getbootstrap.com/
                         icons=['battery-charging', 'currency-bitcoin', 'bank', 'bar-chart-line','activity'],
                         menu_icon="caret-down-fill", default_index=0,
                         #styles={
        #"container": {"padding": "5!important", "background-color": "#fafafa"},
        #"icon": {"color": "orange", "font-size": "25px"},
        #"nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        #"nav-link-selected": {"background-color": "#2F2F31"},{"secondary-background-color": "#2F2F31"},{"primary-color": "#EFFF4B"},{"text-color": "#FEFEFF}
    #}
    )
if choose == "About":

    #with column2:  # To display the header text using css style
    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)
    column1, column2 = st.columns([0.6, 0.4])
    #with col1:  # To display brand log
        #st.image(logo, width=130)
    column2.write(
        "Laura Kouadio is a Data Scientist Enthusiat and Millenial Lifestyle Blogger. She writes Data Science tuturials and [articles](https://medium) on the Blockchain Economy, Web3 Technology and Topics of interest using Python, R, Tableau and other analytic tools .\n\n  She is also a workout advocate who loves healthy habits when it comes to the Mind, Body, Spirit And Money.\n\n[Laura's LinkedIn](https://www.linkedin.com/in/laura-kouadio-083374131/) - [Laura's' GitHub](https://github.com/MlleLauraka/)")
    current_picture=Image.open("current_picture.png")
    column1.image(current_picture, width=400)
    #st.image(profile, width=700)

if choose == "Project 1":

    # ---------------------------------#
    # Page Layout
    # st.set_page_config(page_title="Crypto Categories Dashboard", page_icon=":bar_chart:", layout="wide")
    # image = Image.open('/Users/Laura/Downloads/quantitatives-ZAIbez5LTrg-unsplash.jpg')
    st.title(":bar_chart: Crypto Categories Dashboard")
    st.markdown("This app retrieves the Categories performance on the Crypto Market from **CoinGecko**!")

    # About
    expander_bar = st.expander("About")
    expander_bar.markdown("""
    * **Objectif:** Learn whose industries are being currently disrupted by the Blockchain Technolgy and what are their value on the Crypto Market as of today.
    * **Python libraries:** Pandas, Streamlit, Numpy, Plotly.express, Json
    * **Data source:** [CoinGecko](https://www.coingecko.com/).
    * **Credit:** Youtube Channel Data Professor : *[Data Science Web App in Python](https://www.youtube.com/watch?v=ZZ4B0QUHuNc&t=338s)*).
    * **Contact:** *[Laura Kouadio](https://www.linkedin.com/in/laura-kouadio-083374131/)*
    * **Code:** *[Github](https://github.com/MlleLauraka/)*
    """)


    # Import Json file
    @st.cache
    def load_data():
        data = requests.get('https://api.coingecko.com/api/v3/coins/categories?order=market_cap_desc').text
        data = json.loads(data)
        return data


    data = load_data()

    # Turn it into Dataframe Pd
    df_0 = data
    df = pd.DataFrame(df_0, columns=['id', 'name',
                                     "market_cap",
                                     "market_cap_change_24h",
                                     "content",
                                     "top_3_coins",
                                     "volume_24h",
                                     "updated_at"])

    df = df.drop(columns=['top_3_coins'], axis=0)
    pd.options.display.float_format = '{:,}'.format
    df = np.round(df, decimals=2)

    # TOP KPI's
    number_categories = int(df["name"].count())
    average_rating_mc = round(df["market_cap_change_24h"].mean(), 1)
    average_rating_mc_usd = round(df["market_cap"].mean() / 1000000, 2)
    average_rating_vm = round(df["volume_24h"].mean(), 2)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.metric(label="Number of Category:", value=f" {number_categories:,}")
    with middle_column:
        st.metric(label="Market Cap 24h:", value=f"$ {average_rating_mc_usd:}MM", delta=(f"{average_rating_mc} %"))
    st.markdown("""---""")

    # ---------------------------------#
    # ---- Menu Bar (Side Bar) ---- Find the dropdown filters for categories and dates

    st.sidebar.header("Please Filter Here:")
    Name = st.sidebar.selectbox(
        "Select a Category:",
        options=df["id"].unique()
    )

    df_selection = df.query(
        "id == @Name"
    )

    # ---------------------------------#
    # Main page
    # ---- Display the DataFrame on Streamlit app ----
    st.subheader('Categories Analysis')
    df = df.drop(columns=['id'], axis=0)
    st.write('Here are the Crypto Categories created by CoinGecko: Crypto Industries and Ecosystems are listed')
    st.dataframe(df)

    # Combo MCap & Volume Graph
    fig_vl_mc = px.line(y=df["volume_24h"], x=df["name"], title="Daily Volume & Market by Categories (USD)",
                        template="plotly_white", color=px.Constant("Volume"))
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
    # --Vizu 3
    # Group the 10 Best Categories
    group_10 = df.nlargest(n=15, columns=['market_cap'])
    group_10["Color"] = np.where(group_10["market_cap_change_24h"] < -0.0000, 'Negative', 'Positive')

    # ---------------------------------#
    #Top 10 Best Crypto

    fig_mc_cg = px.histogram(y=group_10["name"], x=group_10["market_cap_change_24h"],
                             title="Top 15 Categories Market Cap Change 24h(%)", template="plotly_white",
                             color=group_10["Color"]).update_yaxes(categoryorder="total ascending")
    fig_mc_cg.update_traces(ybins_size=1)  # can add text=round(df_selection["volume_24h"], 1) if needed
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

    # --------Single Chosen---------)
    st.markdown("""---""")
    st.subheader('Single Category Analysis')
    st.write('**Please select a Crypto Category in the Sidebar to analyse its performance**')

    # Get Url for signl category coins
    df1 = (df_selection['id'].iloc[0])
    df1 = str(df1)
    data = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=" + df1 + "&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d").text
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
    ], axis=0)

    # For currenncy purpose change Int in Floats
    df_singl['market_cap'] = df_singl['market_cap'].astype(float)
    df_singl['total_volume'] = df_singl['total_volume'].astype(float)
    st.dataframe(df_singl)
    st.write("**The category has** **" + str(df_singl.size) + "** **digital assets as of today**")

    df_selection_group = df_singl.nlargest(n=15, columns=['market_cap'])

    fig_single = px.histogram(y=df_selection_group["name"], x=df_selection_group["market_cap"],
                              title="Top 15 Crypto Market Capitalization", template="plotly_white").update_yaxes(
        categoryorder="total ascending")
    fig_single.update_traces(ybins_size=1)  # can add text=round(df_selection["volume_24h"], 1) if needed
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

    fig_single2 = px.histogram(y=df_selection_group["name"], x=df_selection_group["current_price"],
                               title="Price of the Top 15 Crypto by Market Price",
                               template="plotly_white").update_yaxes(categoryorder="total ascending")
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


elif choose =="Project 2":
    
    st.title('Risk Analysis: Attrition Prediction')

    # About
    expander_bar = st.expander("About")
    expander_bar.markdown("""
    	* **Objectif:** This Algorithm predicts the Attrition(Churn) of a Client in the Banking Industry depending on the values selected. The results depend on the Dataset used as well as the ML Algoritm output.
    	* **Python libraries:** Pandas, Streamlit, Scikit.Learn, Plotly.express
    	* **Data source:** [Kaggle](https://www.kaggle.com/code/kmalit/bank-customer-churn-prediction/notebook).
    	* **Contact:** *[Laura Kouadio LindedIn](https://www.linkedin.com/in/laura-kouadio-083374131/)
    	* **Code:** *[Laura Kouadio GitHub](https://github.com/MlleLauraka)*
    	""")


    st.subheader('Multi Model Predictions')


    # Getting the Data
    @st.cache  # https://docs.streamlit.io/library/advanced-features/caching
    def load_data():
        df_data = pd.read_csv('Churn_Modelling.csv')
        df_data = df_data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)
        return df_data


    df_data = load_data()
    st.dataframe(df_data)

    # Encoding categorical variables
    one_hot = pd.get_dummies(df_data[['Geography', 'Gender']])
    df_data_good = df_data.drop(columns=['Geography', 'Gender'], axis=1)
    df_data_fixed = df_data_good.join(one_hot)

    # Upsampling
    oversample = SMOTE()
    X, y = oversample.fit_resample(df_data_fixed[df_data_fixed.columns[:-1]], df_data_fixed[df_data_fixed.columns[-1]])
    df_data1 = X.assign(Churn=y)


    # Sidebar Options:
    st.sidebar.subheader('Please Select your KYC Input')
    params = {
            'Client number of Products': st.sidebar.selectbox('NumOfProducts', (1, 2, 3, 4)),
            'Client Tenure': st.sidebar.selectbox('Tenure', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)),
            'Client Balance': st.sidebar.slider('Balance', min(df_data1['Balance']), max(df_data1['Balance'])),
            'Client Estimated Salary': st.sidebar.slider('EstimatedSalary', min(df_data1['EstimatedSalary']),
                                                     max(df_data1['EstimatedSalary'])),
            'Client Credit Score': st.sidebar.slider('CreditScore', 350, max(df_data1['CreditScore'])),
            'Client Age': st.sidebar.slider('Age', 18, max(df_data1['Age'])),
            'Is Active Member': 1 if st.sidebar.checkbox('IsActiveMember') else 0,
            'Is Female': 1 if st.sidebar.checkbox('Gender_Female') else 0,
            'Is Male ': 1 if st.sidebar.checkbox('Gender_Male') else 0,
            'Is French': 1 if st.sidebar.checkbox('Geography_France') else 0,
            'Is German': 1 if st.sidebar.checkbox('Geography_Germany') else 0,
            'Is Spanish': 1 if st.sidebar.checkbox('Geography_Spain') else 0,
            'Has a Credit Card': 1 if st.sidebar.checkbox('HasCrCard') else 0,
    }
    # could have put .unique() if it was for categorical variable
    test_size = st.sidebar.slider('Pick Test Size', 0.05, 0.65, 0.25, step=0.05)


    # Creating the models
    #@st.cache(allow_output_mutation=True)
    def get_models():
            y = df_data1['Exited']
            X = df_data1.drop(columns=['Exited'])
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, shuffle=True)
            models = [
                #SVC(kernel="linear", C=0.025),
                KNeighborsClassifier(8),
                RandomForestClassifier(max_depth=26, n_estimators=10, max_features=1),
                AdaBoostClassifier(n_estimators=60, learning_rate=1.2),
                ]
            df_models = pd.DataFrame()
            temp = {}
            print(X_test)

            # interating all models
            for model in models:
                print(model)
                m = str(model)
                temp['Model'] = m[:m.index('(')]
                model.fit(X_train, y_train)
                temp['F1_Score'] = sqrt(f1(y_test, model.predict(X_test)))
                temp['Pred Value'] = model.predict(pd.DataFrame(params, index=[0]))[0]
                print('F1 score', temp['F1_Score'])
                df_models = df_models.append([temp])
            df_models.set_index('Model', inplace=True)
            pred_value = df_models['Pred Value'].iloc[[df_models['F1_Score'].argmax()]].values.astype(float)
            return pred_value, df_models

    def run_data():
            #run_status()
            df_models = get_models()[0][0]
            if df_models == 1:
                A = " Attrited."
            else:
                A = " not Attrited."

            st.write('Given your parameters, the result is **{:.2f}**'.format(df_models), " Which means" + A)


    def show_ML():
            df_models = get_models()[1]
            df_models
            st.write('**This Histogram shows F1 score for all models**')
            st.bar_chart(df_models['F1_Price'])


    btn = st.sidebar.button("Predict")
    if btn:
        run_data()
    else:
        pass

    st.sidebar.subheader('Additional Information')

    if st.sidebar.checkbox('Show ML Models'):
        run_data()
        df_models = get_models()[1]
        df_models
        st.write('**This diagram shows the F1 Score for all models**')
        st.bar_chart(df_models['F1_Score'])

elif choose =="Project 3":
    # structuring the side bar menu
    def sidebar_info():
        st.sidebar.subheader('Top 100 Crypto Exchanges')
        st.sidebar.markdown("""
                            This visualization is based on the data from Coin Gecko API.\n\n
                            **Context**: Top 100 Cryptocurrency Exchanges from all over the world.\n\n
                            **Tool Used**: Tableau embedded.\n\n
                            **Graphs Description**:\n\n 
                            *The Map* gives the value of Crypto Exchanges Volumes by Country, hover on it and you'll see the exchanges that have their headquarters in that region.\n\n
                            *The Histogram* sorts the list of Exchanges by Daily Volume and match with the Map Chart to show the exact list of Exchanges by Country.\n\n
                            *The TreeMap* shows the Exchanges by Trust Score. Trust Score is a metric delivered by Coin Gecko giving an Idea of the Trust you can have in those Exchanges.\n\n 
                            **Legend**: You can also research an Exchange by it's Id.

                            """)

        # the body of the page


    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1647894688149' style='position: relative'>
            <noscript>
            <a href='#'>
            <img alt='Top 100 Crypto Exchanges Analysis (Daily)Have you ever asked yourself whose crypto exchange perform the best and from where they operate their magic?This Dashboard gives a daily analysis of the top 100 Crypto Exchanges listed on the CoinGecko Website.That is an interesting tool to anticipate the effect of countries regulation on the differents exchanges or, to get an idea of the best place to operate an Cryptoccurency Exchange.This tool can also be on an help for people looking for investing in Digital Assets since the Volume and Trust Score are indicators of Exchanges performance and investors can rely on: The Trust Score established by CoinGecko lead us to keep the difference between the CEX (Centralized Exchanges) and DEX (Decentralized Exchanges) in mind. Indeed, it appears that the majority of DEX exchanges have the lowest Trust Scores even though their daily Volume can be consequent (Please view the Uniswap Volume (v3)).
            ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;Top100CryptoExchangesAnalysisDaily&#47;Story1&#47;1_rss.png' style='border: none' />
            </a>
            </noscript><object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> <param name='site_root' value='' />
            <param name='name' value='Top100CryptoExchangesAnalysisDaily&#47;Story1' />
            <param name='tabs' value='no' /><param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;Top100CryptoExchangesAnalysisDaily&#47;Story1&#47;1.png' />
            <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                
            <script type='text/javascript'>                    
            var divElement = document.getElementById('viz1647894688149');                    
            var vizElement = divElement.getElementsByTagName('object')[0];                    
            vizElement.style.width='1016px';vizElement.style.height='991px';                    
            var scriptElement = document.createElement('script');                    
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
            vizElement.parentNode.insertBefore(scriptElement, vizElement);                
            </script>"""
        components.html(html_temp, width=1130, height=1100)


    if __name__ == "__main__":
        main()

        st.markdown(
            f'Link to the dashboard on Tableau Public [here](https://public.tableau.com/app/profile/laura5733/viz/Top100CryptoExchangesAnalysisDaily/Story1#1)')
        st.markdown(
            f"**Data source and information about data collect can be found on [Coin Gecko - API](https://www.coingecko.com/en/api)**")
        st.markdown(
            f"**Credit: [Okoh Anita](https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b)**")
        max_width_str = f"max-width: 1030px;"
        st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",
                    unsafe_allow_html=True)

        # the controller


    def load_page():
        sidebar_info()
        main()


elif choose =="Project 4":

    st.title("SQL with a Company'""s Database: Business Performance Analysis")
    # About
    expander_bar = st.expander("About")
    expander_bar.markdown("""
        * **Objectif:** This Projects is an example of a Decision support tool that can be used for performance analysis. The purpose is to demonstrates my ability to work on relational databases with the SQL language.
            * **Language used:** Python 3.9, SQL(MySQL)
        * **Data source and Code:** Database given by our RDBM Professor - Database on my [Github](https://github.com/MlleLauraka).
        * **Contact:** *[Laura Kouadio](https://www.linkedin.com/in/laura-kouadio-083374131/)*
        """)
    st.markdown("""---""")
    # Sidebar
    st.sidebar.title("Project Description")
    st.sidebar.markdown('This Project shows 9 tables extracted from a the relational database of Company:\n\n'
                        '**LGBRAND**\n\n'
                        '**LGCUSTOMER**\n\n'
                        '**LGDEPARTMENT**\n\n'
                        '**LGEMPLOYEE**\n\n'
                        '**LGINVOICE**\n\n'
                        '**LGPRODUCT**\n\n'
                        '**LGLINE**\n\n'
                        '**LGSUPPLIES**\n\n'
                        '**LGVENDOR**\n\n'
                        'We will use SQL and Python languages to extracts and aggregate information from these datasets.\n\n'
                        "From it, we will analyse the company's performance and and take decisions.\n\n"
                        )

    st.header('Entity  Relational Dashboard picture')
    st.write('**This picture is the ERD of the 9 tables to be analyzed**')

    # Put the st.image of the ERD
    image = Image.open('Image-ERD.png')
    st.image(image, width=750)
    st.header('Data Visualization on the datasets')
    st.write('**Each Table give basic information on its respective topic. Here are some metrics relative to the identity of the company:**\n\n'
             '**The Company sells nail beauty products in 24 states, but their biggest Market are New York with more than USD 100K  of sales made, Pennsylvania (>100K) and North Carolina (>55K). On the period 2015-2016, it registered 1362 customers.**\n\n'
             '**The company has 363 employees scattered in 8 departmennts. They are mainly Associates, Driver, Freight Stocker and Load Specialist.**\n\n'
             '**Moreover,the company partners with 22 vendors to sell 252 differents products. 90% Of those products are Top Coats & Primers according to the Charts below, it seems like the sales are not influenced by seasonality since we do not see any major trend appearing.**')

    Balance_by_sheet = Image.open('Balance by sheet.png')
    Invoice_by_Date = Image.open('Invoice amount by Date.png')
    st.image(Balance_by_sheet, width=750)
    st.image(Invoice_by_Date, width=750)

    st.markdown("""---""")
    st.subheader('Deeper Analysis and Insight Raised from Joining Datasets')

    st.write(
        '**Now that we have a better understanding of the context and the performance of that company we can aggregate information by crossing those tables to create performance indicators.**\n\n'
        '**More precisely, it is needed to indentify the drivers of the performance. But, on the second hand, assessing the company issues is necessary too.**\n\n'
        '\n\n'
        '\n\n'
        '\n\n'
        '**1.    Top Employees Metric:**\n\n'
        'Knowing who the best employees are is crucial for Business Performance. The idea is to keep motivated the 10% employees that bring most value to the companies, therefore incentivize those ones that brought the highest amount of sales on the period. Below is a picture of the dataset created giving the list of employees by decreasing sales amount.\n\n'
        '*For this we used the LGINVOICE and  LGEMPLOYEE Tables*\n\n'
    )
    Best_Employees = Image.open('Best Employees.png')
    st.image(Best_Employees, width=350)

    st.write(
        '**2.    Suppliers Performance Metric:**\n\n'
        'Working with a supplier is beneficial when the product has a high demand and when the company is profitable out of it. For the purpose, the vendors with a Ratio (Total Invoice/Price of Product sold greater than 240) should be flagged since we see that they are the ones bringing less value to the company. Also, The company should reinforce its partnership with the ones with the highest ratio.\n\n'
        '*For this we used the LGINVOICE and  LGVENDOR Tables*\n\n'
    )

    Best_Suppliers = Image.open('Best Supplier.png')
    st.image(Best_Suppliers, width=750)


    st.write(
        '**3.    Customers Cross Sales Metric:**\n\n'
        'Customers with the highest balance should be eligible to cross sales or discounts to boost their basket amount and increase the benefit. Out of 336 customers, selecting the top 10% is a reasonable idea. Also, flagging the 10% less loyal customers is also a good idea to incentivize them or understanding the reason why they do not buy that much from the company(survey).\n\n'
        '*For this we used the LGINVOICE and  LGCUSTOMER Tables*\n\n'
    )
    Best_Clients = Image.open('Best Clients.png')
    st.image(Best_Clients, width=350)


    st.write(
        '**4.    Product Performance Metric:**\n\n'
        'The company can look in detail the different products by category and compare the sales. Which ones are selling more ? What is the price range for each ? Sould it cease selling a whole category of product? Those are the questions that could be answered with that metric.\n\n'
        '*For this we used the LGLINE and  LGPRODUCT Tables*\n\n'
    )

    Product_Sales = Image.open('Product Category Sales Amount.png')
    st.image(Product_Sales, width=750)
    Product_Range= Image.open('Product Price Range.png')
    st.image(Product_Range, width=750)
