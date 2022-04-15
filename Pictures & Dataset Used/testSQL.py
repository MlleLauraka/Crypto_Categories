import streamlit as st
import mysql.connector as connection
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid
from PIL import Image

st.title('SQL Company Metrics Analysis: Attrition Prediction')
# About
expander_bar = st.expander("About")
expander_bar.markdown("""
    * **Objectif:** This Projects is an example of a Decision support tool that can be used for performance analysis. The purpose is to demonstrates my ability to work on relational databases with the SQL language.
        * **Language used:** Python 3.9, SQL(MySQL)
    * **Data source and Code:** Database given by our RDBM Professor - Database on my [Github](https://github.com/MlleLauraka).
    * **Credit:** Websites Plotly, Pandas, StackOverflow and Youtube Channel Data Professor : *[SATSifaction](https://www.youtube.com/watch?v=_7BYZ5X57sU)*).
    * **Contact:** *[Laura Kouadio](https://www.linkedin.com/in/laura-kouadio-083374131/)*
    """)
st.markdown("""---""")
    # Sidebar
st.sidebar.title("Project Description")
st.sidebar.markdown("""This Project shows 9 tables extracted from a Company's relational database:\n\n
                    **LGBRAND**\n\n
                    **LGCUSTOMER**\n\n
                    **LGDEPARTMENT**\n\n
                    **LGEMPLOYEE**\n\n
                    **LGINVOICE**\n\n
                    **LGPRODUCT**\n\n
                    **LGLINE**\n\n
                    **LGSUPPLIES**\n\n
                    **LGVENDOR**\n\n
                    We'll use SQL and Python languages to extracts and aggregate information from these datasets.\n\n
                    From it, we'll make Analysis on the company performance and and take decisions.\n\n

                    """)
st.header('Entity  Relational Dashboard picture')
st.write('**This picture is the ERD of the 9 tables to be analyzed**')

    # Put the st.image of the ERD
image = Image.open('Image-ERD.png')
st.image(image, width = 750)
st.header('Data Visualization on the datasets')

    #LGBRAND
mydb = connection.connect(host="localhost", user="root", passwd="Msnexpl0reR", database="LargeCo", use_pure=True)
query = "Select * from LGBRAND;"
result_dataFrameLGBRAND = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGBRAND)

query = "Select * from LGCUSTOMER;"
result_dataFrameLGCUSTOMER = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGCUSTOMER)

query = "Select * from LGDEPARTMENT;"
result_dataFrameLGDEPARTMENT = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGDEPARTMENT)

query = "Select * from LGEMPLOYEE;"
result_dataFrameLGEMPLOYEE = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGEMPLOYEE)

query = "Select * from LGINVOICE;"
result_dataFrameLGINVOICE = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGINVOICE)

query = "Select * from LGPRODUCT;"
result_dataFrameLGPRODUCT = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGPRODUCT)

query = "Select * from LGLINE;"
result_dataFrameLGLINE = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGLINE)

query = "Select * from LGSUPPLIES;"
result_dataFrameLGSUPPLIES = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGSUPPLIES)

query = "Select * from LGVENDOR;"
result_dataFrameLGVENDOR = pd.read_sql(query, mydb)
st.dataframe(result_dataFrameLGVENDOR)

mydb.close()  # close the connection

st.subheader("LGCUSTOMER Table")
st.write("**Customer and Balance Geographical Repartition: The company has** " + str(result_dataFrameLGCUSTOMER["CUST_LNAME"].count()) +" **customers. The biggest market is in New-York, Pennsilvania and North Carolina**" )

fig_mc_cg = px.bar(result_dataFrameLGCUSTOMER, y=result_dataFrameLGCUSTOMER["CUST_BALANCE"], x=result_dataFrameLGCUSTOMER["CUST_STATE"], title="Customers Balance by States", template="plotly_white").update_xaxes(categoryorder="total ascending")
fig_mc_cg.update_layout(barmode='stack')
fig_mc_cg.update_layout(
        autosize=False,
        width=1100,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="States",
        yaxis_title="Balance",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
st.plotly_chart(fig_mc_cg, use_container_width=True)

left_column, right_column = st.columns(2)
right_column.subheader("LGBRAND Table")
right_column.write("**Brand name repartition by type: Table shows that we have more value brands than other brand. Premium ones are the less numerous**")
right_column.write(result_dataFrameLGBRAND ["BRAND_TYPE"].value_counts())

left_column.subheader("LGDEPARTMENT Table")
left_column.write("**Department Information: The company has** **" + str(result_dataFrameLGDEPARTMENT["DEPT_NAME"].count()) +"** **Departments**")
left_column.write(result_dataFrameLGDEPARTMENT["DEPT_NAME"].value_counts())

result_dataFrameLGEMPLOYEE["EMP_INDEX"]=1 # Adding a column for figure histogram (need an numerical object)

st.subheader("LGEMPLOYEE Table")
st.write("**Employees Information: The company has** **"+ str(result_dataFrameLGEMPLOYEE["EMP_INDEX"].count()) +"** **employees**.")
st.markdown("**They are mainly Associates, Driver, Freight Stocker and Load Specialist.**")

fig = px.bar(result_dataFrameLGEMPLOYEE, y=result_dataFrameLGEMPLOYEE["EMP_TITLE"], x=result_dataFrameLGEMPLOYEE["EMP_INDEX"], title="Employees by Title", template="plotly_white").update_yaxes(categoryorder="total ascending")
fig.update_layout(barmode='stack')
fig.update_layout(
        autosize=False,
        width=1100,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Employee count",
        yaxis_title="Job Title",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )

fig2 = px.pie(result_dataFrameLGEMPLOYEE, values=result_dataFrameLGEMPLOYEE["EMP_INDEX"], names=result_dataFrameLGEMPLOYEE["DEPT_NUM"],title="Employees by Department", hole=.3)

# 2columns visual for LGEMPLOYEE charts
left_column, right_column = st.columns(2)
right_column.plotly_chart(fig2, use_container_width=True)
left_column.plotly_chart(fig, use_container_width=True)

st.subheader("LGINVOICE and LINE Tables")
st.write("**The company has** **" + str((result_dataFrameLGINVOICE["INV_TOTAL"].sum())*(result_dataFrameLGLINE["LINE_QTY"].sum()))+"** **USD for Turnorver.**")
st.write("**The mean is:** **" + str(result_dataFrameLGINVOICE["INV_TOTAL"].mean())+"**")
st.write("**It seem that this company is not influenced by seasonality. Not higher sells in Christmas or during Summer for instance.**")


fig3 = px.bar(result_dataFrameLGINVOICE, x=result_dataFrameLGINVOICE["INV_DATE"], y=result_dataFrameLGINVOICE["INV_TOTAL"], title="Total Amount of Invoice by day Over the Time", template="plotly_white").update_xaxes(categoryorder="total ascending")
fig3.update_layout(barmode='stack')
fig3.update_layout(
        autosize=False,
        width=1900,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="Invoice Amount",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
st.plotly_chart(fig3, use_container_width=True)

result_dataFrameLGPRODUCT["PROD_INDEX"]=1 #Adding a column for figure histogram (need an numerical object)
fig4 = px.box(result_dataFrameLGPRODUCT, x=result_dataFrameLGPRODUCT['PROD_INDEX'], y=result_dataFrameLGPRODUCT['PROD_CATEGORY'])


result_dataFrameLGSUPPLIES["SUPPLIES_INDEX"]=1 #Adding a column for figure histogram (need an numerical object)

fig5 = px.box(result_dataFrameLGSUPPLIES, x=result_dataFrameLGSUPPLIES["SUPPLIES_INDEX"], y=result_dataFrameLGSUPPLIES["VEND_ID"])

left_column, right_column = st.columns(2)

left_column.subheader("LGPRODUCT Table")
left_column.write("**PRODUCTS Information: the company sell** **" + str(result_dataFrameLGPRODUCT["PROD_INDEX"].count()) +"** **differents products.**")
left_column.write("**90% Of those Product are Top Coats & Primers.**")
left_column.plotly_chart(fig4, use_container_width=True)

right_column.subheader("LGSUPPLIES Table")
right_column.write("**SUPPLIERS Information related to the products**")
right_column.write("**The company partner with 22 vendors to perform its business**")
right_column.plotly_chart(fig5, use_container_width=True)

st.subheader("LGVENDOR Table")
st.write("**SUPPLIERS Information detailed**")

result_dataFrameLGVENDOR["Vendor_INDEX"]=1 #Adding a column for figure histogram (need an numerical object)


fig7 = px.bar(result_dataFrameLGVENDOR, y=result_dataFrameLGVENDOR["Vendor_INDEX"], x=result_dataFrameLGVENDOR["VEND_STATE"], title="Suppliers location by States", template="plotly_white").update_xaxes(categoryorder="total ascending")
fig7.update_layout(barmode='stack')
fig7.update_layout(
        autosize=False,
        width=1900,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Market Cap Change over 24h",
        yaxis_title="Categories",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
st.plotly_chart(fig7, use_container_width=True)

st.markdown("""---""")
st.subheader('Deeper Analysis and Insight Raised from Joining Datasets')
st.markdown(""" **Now that we have a better understanding of the context and the performance of that company we can aggregate information from those different datasets to extract new information and make decision ont it. More precisely, it is needed to indentify the drivers of the performance too keep thriving in that virtuous circle. But, on the second hand, assessing the company issues is necessary too.**""")

#Q1
st.write("**1.    Who are the best 5 employees for the company?**")
st.write(" *The idea is to keep the employees that bring the most value to the companies, therefore incentivize those ones that brought the highest number of sells by looking at the total amount of invoice they got on the period.*")
st.write(" *The top 10% (36th first employees) needs to be incentived.*")
mydb = connection.connect(host="localhost", user="root", passwd="Msnexpl0reR", database="LargeCo", use_pure=True)
query = """
    SELECT EMP_LNAME, EMP_FNAME, EMP_NUM, SUM(INV_TOTAL)
    FROM LGEMPLOYEE JOIN LGINVOICE ON
    LGEMPLOYEE.EMP_NUM = LGINVOICE.EMPLOYEE_ID
    GROUP BY EMP_NUM ORDER BY SUM(INV_TOTAL) DESC LIMIT 36;
    """
result_dataFrameQ1 = pd.read_sql(query, mydb)
mydb.close()  # close the connection

AgGrid(result_dataFrameQ1)

#Q2
st.write("**2.	What supplier should they reconsider working with??**")
st.write("*Working with a supplier is beneficiary when the product has a high demand and when the company can be profitable out of it. The company should first flag the suppliers that offer the products less attractive and then match them with their cost to check if they should continue the partnership with the vendor for the next periods.*")
st.write("*For the purpose, the vendors with a Ratio (Total Invoice/Products of Product sold greater than 240) should be flagged since we see that they are the ones bringing less value to the company. On the other way around, The company should by more from the ones with the highest ratio.*")
mydb = connection.connect(host="localhost", user="root", passwd="Msnexpl0reR", database="LargeCo", use_pure=True)
query = """
    SELECT COUNT(LGLINE.PROD_SKU), LGSUPPLIES.VEND_ID, SUM(LGINVOICE.INV_TOTAL), (SUM(LGINVOICE.INV_TOTAL)/COUNT(LGLINE.PROD_SKU)) AS RATIO
    FROM LGPRODUCT JOIN LGLINE ON LGPRODUCT.PROD_SKU = LGLINE.PROD_SKU
    JOIN LGSUPPLIES ON LGPRODUCT.PROD_SKU = LGSUPPLIES.PROD_SKU
    JOIN LGINVOICE ON LGLINE.INV_NUM = LGINVOICE.INV_NUM
    GROUP BY LGSUPPLIES.VEND_ID
    ORDER BY RATIO ASC;
    """
result_dataFrameQ2 = pd.read_sql(query, mydb)
mydb.close()  # close the connection

AgGrid(result_dataFrameQ2)
result_dataFrameQ2.astype({"VEND_ID": object})

A=result_dataFrameQ2.info()
print(A) 

figq2 = px.bar(result_dataFrameQ2, y=result_dataFrameQ2["RATIO"], x=result_dataFrameQ2["VEND_ID"], title="Suppliers location by States", template="plotly_white").update_xaxes(categoryorder="total ascending")
figq2 .update_layout(barmode='stack')
figq2 .update_layout(
        autosize=False,
        width=1900,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Vendor ID",
        yaxis_title="Ratio",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
st.plotly_chart(figq2 , use_container_width=True)

    #Q3
st.write("**3.    Who are the customers eligibles for crosssales and dicounts?**")
st.write("*Customers with the highest balance should be eligible to cross sales to boost their sales and increase the benefit. Out of 336 customers, selecting the top 10% is a reasonable idea. Giving discounts to those loyal customer is also a good idea to increase their purchasing power and the company's sales.* ")
mydb = connection.connect(host="localhost", user="root", passwd="Msnexpl0reR", database="LargeCo", use_pure=True)
query = """
    SELECT sum(INV_TOTAL), LGCUSTOMER.CUST_CODE
    FROM LGINVOICE JOIN LGCUSTOMER ON
    LGINVOICE.CUST_CODE = LGCUSTOMER.CUST_CODE
    GROUP BY LGCUSTOMER.CUST_CODE
    ORDER BY sum(INV_TOTAL) DESC LIMIT 36;
    """
result_dataFrameQ3 = pd.read_sql(query, mydb)
mydb.close()  # close the connection

AgGrid(result_dataFrameQ3)

    #Q4a
st.write("**4.    Which are the less performing products?**")
st.write("*Instead of ceasing business with a supplier, the company can also look in detail the different product by category and compare the products to the average price in the same category. It helps for the product performance.*")
st.write("*For instance in the cleaner category, the average product is $8.60 and products are in the same range in term of purchase. Therefore the company should find a way to get more benefit from the less expensive products (increase price or reducing stocks).*")
mydb = connection.connect(host="localhost", user="root", passwd="Msnexpl0reR", database="LargeCo", use_pure=True)
query = """
    SELECT LGLINE.PROD_SKU, COUNT(LINE_QTY)*PROD_PRICE, PROD_PRICE, PROD_CATEGORY
    FROM LGLINE JOIN LGPRODUCT ON 
    LGLINE.PROD_SKU = LGPRODUCT.PROD_SKU
    GROUP BY LGLINE.PROD_SKU ORDER BY COUNT(LINE_QTY) DESC;
;
    """
result_dataFrameQ4a= pd.read_sql(query, mydb)
mydb.close()  # close the connection

AgGrid(result_dataFrameQ4a)


figq4 = px.bar(result_dataFrameQ4a, y=result_dataFrameQ4a["COUNT(LINE_QTY)*PROD_PRICE"], x=result_dataFrameQ4a["PROD_CATEGORY"], title="Sales by Category of Product", template="plotly_white").update_xaxes(categoryorder="total ascending")
figq4.update_layout(barmode='stack')
figq4.update_layout(
        autosize=False,
        width=1900,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Sales Amount",
        yaxis_title="Product Category",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
st.plotly_chart(figq4, use_container_width=True)

figq5 = px.box(result_dataFrameQ4a, y=result_dataFrameQ4a["PROD_PRICE"], x=result_dataFrameQ4a["PROD_CATEGORY"], title="Price Range by Product Category", template="plotly_white").update_xaxes(categoryorder="total ascending")
figq5.update_layout(barmode='stack')
figq5.update_layout(
        autosize=False,
        width=1900,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Price Range",
        yaxis_title="Product Category",
        legend_title="Legend Title",
        xaxis=(dict(showgrid=False))
    )
st.plotly_chart(figq5, use_container_width=True)