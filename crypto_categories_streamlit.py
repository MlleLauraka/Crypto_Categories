#!/usr/bin/env python
# coding: utf-8



st.set_page_config(page_title="Crypto Categories Dashboard", page_icon=":bar_chart:", layout="wide")


# ---- Get an Excel File with Streamlit ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="/Users/Laura/Desktop/PYTHON/Projects/Crypto_Categories/Crypto_Categories.xlsx",
        engine="openpyxl",
        sheet_name="Sheet1",
        skiprows=0,
        usecols="B:R",

    )

# add nrows=142, if issues in the future to retrieve data

    return df
df = get_data_from_excel()

# ---- Menu Bar (Side Bar) ----
st.sidebar.header("Please Filter Here:")
Name = st.sidebar.multiselect(
    "Select the Category:",
    options=df["name"].unique(),
    default=df["name"].unique()
)

df_selection = df.query(
    "name == @Name"
)

# ---- Main Page ----
st.title(":bar_chart: Crypto Categories Dashboard")
st.markdown("##")


# TOP KPI's
number_categories = int(df_selection["name"].count())
average_rating_mc = round(df_selection["market_cap_change_24h"].mean(),1)
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

#---- Display the DataFrame on Streamlit app ----
st.subheader('Categories Data')
st.dataframe(df)

st.subheader('Market Capitalization by Categories')
st.write('This is a bar_chart.')
fig_mc = px.histogram(y=df_selection["market_cap"], x=df_selection["name"], title="Daily Market Cap by Categories", template="plotly_white", color_discrete_sequence=px.colors.diverging.Spectral).update_xaxes(categoryorder="total descending")
fig_mc.update_traces(ybins_size=1)
fig_mc.update_layout(
    autosize=False,
    width=1100,
    height=500,
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Market Capitalization in USD",
    yaxis_title="Crypto Categories",
    legend_title="Legend Title",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_mc)

fig_vl = px.histogram(y=df_selection["volume_24h"], x=df_selection["name"], title="Daily Volume by Categories", template="plotly_white", color_discrete_sequence=px.colors.diverging.Spectral).update_xaxes(categoryorder="total descending")
fig_vl.update_traces(ybins_size=1) # can add text=round(df_selection["volume_24h"], 1) if needed
fig_vl.update_layout(
    autosize=False,
    width=1100,
    height=500,
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis_title="Crypto Categories",
    yaxis_title="Volume in USD",
    legend_title="Legend Title",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_vl)

""""" To put the dashboard side by side : 
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_mc, use_container_width=True) 
right_column.plotly_chart(fig_vl, use_container_width=True) 


"""
#The Line plot

"""
df = pandas.DataFrame(data=d)
print(df)

country_set = set(df['Country'])

plt.figure()
for country in country_set:
     selected_data = df.loc[df['Country'] == country]
     plt.plot(selected_data['Month'], selected_data['GDPA'], label=country)
     
plt.legend()
plt.show()

fig = px.line(
        df, #Data Frame
        x = "X_axis", #Columns from the data frame
        y = "Y_axis",
        title = "Line frame"
    )
fig.update_traces(line_color = "maroon")
st.plotly_chart(fig)

+ Add the list of coins related to each categories
"""""


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)





