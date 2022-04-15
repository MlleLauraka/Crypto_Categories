#Import dependencies
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

with st.sidebar:
    choose = option_menu("Menu", ["About", "DeFi Analytic Paper - ML Regression Model", "Crypto Categories Vizualization - Engineering with Python", "Crypto Exchanges Analysis with Tableau", "Business Performance Analysis with SQL"], #https://icons.getbootstrap.com/
                         icons=['battery-charging','lightbulb', 'currency-bitcoin','bar-chart-line','activity'],
                         menu_icon="caret-down-fill", default_index=0,

    )
if choose == "About":

    #Set top part = Title and profile
    st.markdown(""" <style> .font {
            font-size:45px ; font-family: 'Cooper Black'; color:#C3DCE7  ;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Laura Kouadio Profile </p>', unsafe_allow_html=True)
    column1, column2 = st.columns([0.6, 0.4])
    current_picture = Image.open("test_linkedin.png")
    column1.image(current_picture, width=400)
    column2.info("""
    Fast paced learner and natural investigator, I am directing my skills toward data sciences and analytics to extract the best insights out of data and help you make meaningful decisions.
    I believe that working in a challenging business is vital for personal achievement.
    With international communication skills and a good team spirit, I have a great capacity to adapt to new environments, cultures, and methods.
    \n\n[Laura's LinkedIn](https://www.linkedin.com/in/laura-kouadio-083374131/) - [Laura's' GitHub](https://github.com/MlleLauraka/)""")

    #Create new columns for the main part
    def txt(a,b):
        col1, col2 =st.columns([3.65, 1.35])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)
    st.markdown("""---""")
    st.markdown('**<div style="text-align: justify"> SKILLS</div>**', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown("""
    - **Tools and Languages:** ARCHER, Excel, Google Sheets, JIRA, R, Power BI, PowerPoint, Python, SQL, Tableau, World
    - **Quantitative Research:**  Data Optimization -Scraping, Cleaning, Visualization, Analysis and Data Modeling 
    - **Softwares:** ARCHER, Google Cloud, JIRA, Jupyter, PyCharm, Anaconda, WebScraper, IBMWatsonStudio, GoogleCollab, Rstudio, Dune Analytics
    - **Communication:** English, French (Native Language), Spanish (Reading and Writing), Italian (Reading and Writing)
    - **Certificates:** IBM Data Science Professional 
    """)
    st.markdown("""---""")
    st.markdown('**<div style="text-align: justify"> PROFESSIONAL EXPERIENCE</div>**', unsafe_allow_html=True)
    st.markdown("""---""")
    txt("**SOCIETE GENERALE CIB - New York, United States of America**","*January 2020 - July 2021*")
    st.markdown("""
    *RISK ANALYST IN PERMANENT CONTROL COORDINATION (Enterprise Risk Management), FULL TIME*
    - Maintained risk at the accepted level by assisting manager in the design of Level 1 controls and the change management around permanent control (project delivery, SG Group standard and norms update...)
    - Ensured the completeness and integration of the various control mechanisms and assess the alignment of SG America's permanent control framework with the Enterprise Risk Management framework
    - Contributed to the production of dashboards and metrics for Level 1 and Level 2 control analysis
    - Identified areas of vulnerability from different angles, consolidated and monitored anomalies and action plans for performance assessment
    - Developed user requirements for project in issue management, interactions with developer’s (JIRA tool)
    - Performed User Acceptance Testing (UAT) for the elements of the tool’s framework (ARCHER GRC tool)
    """)

    txt("**SFR - Paris, France**", "*September 2018 - August 2019*")
    st.markdown("""
        *BUSINESS ANALYST (Commission/Finance), APPRENTICESHIP*
        - Elaborated reliable commission strategies: Analysed and arbitrated the performance of service providers and studied the remuneration strategy of commissioned service providers
        - Collected and analysed data from different IS sources and reporting
        - Produced cycles of commission for the internal control: Guarantee of reliability, conformity of calculations, control of deadlines and deliverables
          """)

    txt("**META CONSEIL - Chessy, France**","*October 2016 - April 2017*")
    st.markdown("""
        *RISK ANALYST IN PERMANENT CONTROL COORDINATION (Enterprise Risk Management), FULL TIME*
        - Created grant files: Help writing business plan for SMEs (technologic, digital, metallurgic, medical, retail sectors)
        - Analysed the client’s financial situation: maintained financial model and drafted forecast analysis with project profitability
        - Researched financial mechanism valuable for the client business project: grant, non-refundable advance, tax credit, leveraged financing and acquisition financing
        - Identified areas of vulnerability from different angles, consolidated and monitored anomalies and action plans     resulting from risk and control performance assessments
        """)

    st.markdown("""---""")
    st.markdown('**<div style="text-align: justify"> EDUCATION</div>**', unsafe_allow_html=True)
    st.markdown("""---""")
    txt("**Master’s Degree - Management Science and Quantitative Methods (GPA 3.9)**	", "*September 2021 - April 2022*")
    st.markdown(""" - SOUTHERN NEW HAMPSHIRE UNIVERSITY - New Hampshire, United States\n\n""")

    txt("**Master’s Degree - Audit, Management Accounting & Finance (GPA 3.6)**","*September 2017 - May 2019*")
    st.markdown(""" - SKEMA BUSINESS SCHOOL (AACSB Accredited) - Suzhou, China & Sophia Antipolis, France\n\n""")

    txt("**Bachelor’s Degree - Economics and Law**","*September 2013 - June 2016*")
    st.markdown(""" - PARIS NANTERRE UNIVERSITY - Nanterre, France""")

    st.markdown("""---""")
    st.markdown('**<div style="text-align: justify"> EXTRA CURRICULAR ACTIVITIES & AWARDS</div>**', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown(""" 
    - **SNHU Cursus:** Award of Academic Excellence - Graduated in only two semesters (1 year) with a GPA of 3.9
    - **Global Young Leader Program 2019:** Hackathon at Ben Gourion University of the Neguev, Israel (3rd place Award)
    - **SKEMA Gala Organizer:** Setting up the Communication Style, Planning Operation and Entertainment, Hosting the Event
    - **Road Trip & Backpacking:** Travel in Asia (China, Indonesia, Malaysia, Thailand)
    - **Sport:** Weightlifting and Hit Workout
    """)

    #Download Resume
    with open("Resume_LK.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="Resume_LK.pdf",

        )


if choose == "DeFi Analytic Paper - ML Regression Model":
#Begin by uploading all datasets and APIs

    #Exploit Dataframe from TheBlockcrypto
    Exploit_theblockcrypto = pd.read_excel("Exploit_theblockcrypto.xlsx")
    Exploit_theblockcrypto['Timestamp'] = pd.to_datetime(Exploit_theblockcrypto['Timestamp'], unit='s')
    Exploit_theblockcrypto.rename({'Result': "Exploit"}, axis='columns', inplace=True)
    Exploit_fig = px.histogram(x=Exploit_theblockcrypto['Timestamp'], y=Exploit_theblockcrypto['Exploit'],
                               title="DeFi Exploit History- March 2020 to February 2022")
    Exploit_fig.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="DeFi Exploits (sum lost in USD)",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    #The DeFi TVL from defillama API extracted in April 2022
    History_Tlv = pd.read_excel("Hist_Tlv.xlsx")
    History_Tlv.rename({"totalLiquidityUSD": "TLV"}, axis=1, inplace=True)
    for i in list(range(len(History_Tlv.index))):  # get the list of the df
        if i > 1213 or i <= 148:  # Select the rows you want to get rid off
            History_Tlv.drop(index=i, axis=0, inplace=True)
    History_Tlv = History_Tlv.reset_index(drop=True)

    #Ethereum TVL from defillama API extracted in April 2022
    History_TlvChain = pd.read_excel("etheurem_hist.xlsx")
    History_TlvChain.rename({"totalLiquidityUSD": "Eth_TLV"}, axis=1, inplace=True)
    for i in list(range(len(History_TlvChain.index))):  # get the list of the df
        if i > 1213 or i <= 148:  # Select the rows you want to get rid off
            History_TlvChain.drop(index=i, axis=0, inplace=True)
    History_TlvChain = History_TlvChain.reset_index(drop=True)

    #Inflation: Average CPI from Bureau of Labor and Statistics
    Inflation = pd.read_excel("Inflation_clean.xlsx")
    fig_Inflation = px.line(x=Inflation['Date'], y=Inflation['Rate'],
                            title="Consumption Price Index History - April 2019 to February 2022")
    fig_Inflation.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="Consumption Price Index Value",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    #Bitcoin MarketCap History from data.nasdaq
    blockchain = pd.read_csv("BCHAIN-MKTCP.csv")
    blockchain = blockchain.loc[::-1].set_index(blockchain.index)  # reindexing from downup(reverse)
    for i in list(range(len(blockchain.index))):  # get the list of the df
        if i > 1069 or i <= 4:  # Select the rows you want to get rid off
            blockchain.drop(index=i, axis=0, inplace=True)
    blockchain['Date'] = pd.to_datetime(blockchain['Date'], format='%Y-%m-%d')
    # Bitcoin MarketCap Chart
    fig_bitcoin = px.line(x=blockchain['Date'], y=blockchain['Value'],
                          title="Bitcoin Market Capitalization History - April 2019 to February 2022").update_xaxes(
        categoryorder="total descending")
    fig_bitcoin.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="Bitcoin Market Capitalization (USD)",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    #Ethereum GasPrice in Wei from Etherscan
    GasPrice = pd.read_csv("Pictures & Dataset Used/AvgGasPrice.csv")
    GasPrice["Value (Wei)"] = GasPrice["Value (Wei)"] / 100000000 * 0.00000035 #Giving it its USD value
    GasPrice['Date(UTC)'] = pd.to_datetime(GasPrice['Date(UTC)'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
    GasPrice['Date(UTC)'] = pd.to_datetime(GasPrice['Date(UTC)'], format='%Y-%m-%d')
    # Ethereum gas Chart
    fig_GasPrice = px.line(x=GasPrice['Date(UTC)'], y=GasPrice['Value (Wei)'],
                           title="Average Daily Wei Price History - April 2019 to February 2022")
    fig_GasPrice.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="Wei price (USD)",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    # Visualization Fig Ethereum and DeFi TVL + Bitcoin Mcap
    fig_TVLEthereum_data = px.line(x=History_TlvChain['date'], y=[History_TlvChain['Eth_TLV']],color=px.Constant("Ethereum Historical TLV"),title="DeFi TLV, Ethereum TLV Performance from April 2019 to February 2022").update_xaxes(categoryorder="total descending")
    fig_TVLEthereum_data.add_traces(go.Scatter(x=History_TlvChain['date'], y=History_Tlv['TLV'], name='Defi Historical TLV'))
    fig_TVLEthereum_data.update_layout(
        autosize=False,
        width=725,
        height=400,
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Value in USD",
        xaxis_title="Date",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    #Visualization Fig Ethereum and DeFi TVL + Bitcoin Mcap
    fig_Historical_data = px.line(x=History_TlvChain['date'], y=[History_TlvChain['Eth_TLV']],color=px.Constant("Ethereum Historical TLV"),title="DeFi TLV, Ethereum TLV and Bitcoin Market Cap Performance from April 2019 to February 2022").update_xaxes(categoryorder="total descending")
    fig_Historical_data.add_traces(go.Scatter(x=History_TlvChain['date'], y=History_Tlv['TLV'], name='Defi Historical TLV'))
    fig_Historical_data.add_traces(go.Scatter(x=History_TlvChain['date'], y=blockchain['Value'], name='Bitcoin Historical Market Cap'))
    fig_Historical_data.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis_title="Value in USD",
        xaxis_title="Date",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )

    #Gather Data in only 1 dataframe for model preparation
    df_model = Exploit_theblockcrypto

    for i in list(df_model['Timestamp']):
        for j in list(History_Tlv['date']):  # get the list of the df
            if i == j:
                df_model['Defi_TVL'] = History_Tlv['TLV']

    for i in list(df_model['Timestamp']):
        for j in list(blockchain['Date']):  # get the list of the df
            if i == j:
                df_model['Bitcoin'] = blockchain['Value']

    for i in list(df_model['Timestamp']):
        for j in list(Inflation['Date']):  # get the list of the df
            if i == j:
                df_model['Inflation'] = Inflation['Rate']

    for i in list(df_model['Timestamp']):
        for j in list(GasPrice['Date(UTC)']):  # get the list of the df
            if i == j:
                df_model['GasPrice(Wei)'] = GasPrice["Value (Wei)"]

    df_model2 = df_model.dropna(axis=0)


#Begin writing text
#-Set the Style for the title
    st.markdown(""" <style> .font { font-size:35px ; font-family: 'Cooper Black'; color: #C3DCE7 ;} </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font"> Decentralized finance: An analysis of the potential and threats to its growth</p>', unsafe_allow_html=True)
#ABSTRACT PART
    st.markdown("""---""")
    st.title("ABSTRACT")
    st.markdown('<div style="text-align: justify"> Decentralized Finance system grew of 250% in a year and represents a Total Value Locked (TVL) of $235B as of April 6th, 2022, according to analytics firm Defillama. At the intersection between finance and blockchain technology, it offers its community the opportunity to access financial services free of intermediary. That freedom is a benefit for many populations underbanked or totally excluded from the exclusive and government’s centralized traditional financial systems as well as for investors looking for more independence. The sector is still free willing and largely unregulated which offers to several opportunities but also uncountable risks. Therefore, it is important to evaluate the parameters influencing Decentralized Finance (DeFi)’s growth to forecast its future value. This analytical research paper creates a simple regression model to predict Defi’s performance. For this, we would lay the foundation of DeFi(I) by analyzing the underlying technologies structuring the ecosystem, defining the principles of DeFi and comparing DeFi to the traditional financial system. We would also observe Defi performance from 2019 to April 2020 and construct a multilinear regression model to understand how inflation, Bitcoin value, gas fees prices and cybersecurity exploits impacts on DeFi’s TVL performance (II). Finally, we would submit a study of futures events and systems such as Cyber Security Breach, Cryptocurrency Regulations, Environmental Social Governance (ESG), Central Bank Digital Currencies (CBDC) that could redefine the path to expect for DeFi’s Future Performance (III).  </div>', unsafe_allow_html=True)

#INTRO PART
    st.title("INTRO")
    st.markdown('<div style="text-align: justify"> Decentralized Finance (DeFi) has become vernacular, and its name is often mingled with other new age denominations such as Digital Asset, Web3, Disintermediation or even Blockchain, but many don’t have a clear idea of its meaning neither what its promise really encompasses. Fundamentally, DeFi provides financial services. Although, those are categorized as “Decentralized” because it doesn’t use the traditional financial system to provide these financial services. Instead, DeFi uses the Blockchain Technology to achieve that purpose and offering a service deemed as trustful. Financial Services are now accessible everywhere with an internet connection. Consequently, the term “decentralized” is used to differentiate DeFi with the traditional finance that operates with a centralized protocol (system of large financial intermediaries) to interact between supply and demand on the market. That shift of financial system methods and processes is important since for the first time the party trusted to monitor the money’s custody changed. As you might understand DeFi is not a place, it is a utility born out of many applications offering different types of financial services totally independent from a middleman. Users can utilize those applications called Decentralized application (Dapps) to use Decentralized financial services. It is this whole ecosystem of application that we qualify as “DeFi”.</div>', unsafe_allow_html=True)
#PART I: Roots: The foundations of DeFi
    st.title("I.	 Roots: The foundations of DeFi")
#PART I - A : Technology Underpining DeFi
    st.subheader("A.	Technology Underpining DeFi")
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 1. DeFi pyramidic system </div>',unsafe_allow_html=True)
    st.markdown("""---""")
    DeFi_Structure = Image.open("Pictures & Dataset Used/DeFi_Structure.png")
    st.image(DeFi_Structure, width=700)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> DeFi industry uses Artificial intelligence, Cloud, and Distributed Networks like Blockchain as a supporting structure to produce this end-to-end self-monitored ecosystem.</div>', unsafe_allow_html=True)
    st.markdown('**<div style="text-align: justify"> Blockchains </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> Blockchains are a decentralized Ledgers Technology (DLT) that have no governing authority, these are the layer on which those application decentralized are built. Indeed, DeFi is a group of Decentralized Applications created by different engineers to provide financial services to users and those Dapps are built on top of Blockchains (B.Hor and al.2021). Financial services created on those app trigger transactions on the Dapp layout that would be registered on the Blockchain almost simultaneously (Figure 1). Without the existence of that blockchain Technology, no Dapps would have been created and therefore no DeFi would never have existed, at least not through those conditions.</div>', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Cross-Chain and Multi-Chain Infrastructures </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> As many Dapps with different purpose exist (decentralized exchanges, lending platform, insurance..), many blockchains exist as well. Dapps can interact with several blockchains at same the time but blockchains interacting together is still an issue being solved essentially with cross-chain and multi-chain infrastructures. On a multi-chain effort, some blockchains are Ethereum Virtual Machine (EVM) compatible, making it very easy for them to spin up a version of existing Dapps. This include Fantom, Binance Smart Chain, and Avalanche networks. Being EVM compatible is major since Ethereum is the most used blockchain on the DeFi ecosystem, thus it attracts a substantial number of users. For the non EVM compatible blockchains, bridges platforms can connect some blockchains together and create that path needed for scalability. Cross-chain infrastructures are platforms like bridges that don’t offer DeFi services but help the different blockchains to be interconnected together to let the liquidity DeFi transit between blockchain networks. Moreover, Ethereum blockchain currently uses a Proof-of-work (POW) consensus that leads to scalability issues (high demands on the chain slower transactions process) and creates nonviable gas prices. The network is concurrently saving that issue by creating cross connections. They work on scaling to second layers (layer 2), which offer the same security to the users, without the congestion of the layer 1 blockchain and on upgrading from POW consensus to Proof-of-Stake (POS) to limit the lack of scalability and high gas fee prices. These cases help tremendously the DeFi sector to provide services to more users and scale efficiently even if many of those projects are currently on beta production.</div>', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Oracles and Data Aggregators </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> DeFi is also powered by third party services like Oracles and Data aggregators that serves for getting the real-world data not stored on the blockchain into Dapps and register them on chain. This is necessary for information like real time asset prices, trade data or order books. To keep the process trustful, data entering on-chain from the real world are voted on a consensus mechanism where validators agree for the most accurate data. Main Oracles are Chainlink and Maker Dao. Oracle act as the interface between data from the real word and the blockchain while Data Aggregators gather, and process information received from the Oracle to fit it into the Blockchain.</div>', unsafe_allow_html=True)

#PART I - B : DeFi Principles
    st.subheader("B.	DeFi Principles")
    st.markdown('<div style="text-align: justify"> Decentralized finance is made of several principles, but we will enumerate the most important here: DeFi aims to be Accessible, Transparent, Interoperable and Business Processes Automated.</div>', unsafe_allow_html=True)
    st.markdown('**<div style="text-align: justify"> Accessibility </div>**', unsafe_allow_html=True)

    st.markdown('<div style="text-align: justify"> Accessibility encompasses the horizontal and vertical aspect of accessibility. The horizontal aspect of Accessibility is Inclusivity. DeFi aims to allow everybody to use DeFi platforms no matter their identity or their localization in the world. To this end, price to access the platforms are lower enough to avoid discrimination of entry and Know Your Customer (KYC) process is removed to keep privacy of identity. The downside from that principle is that could lead to Anti Money Laundering (AML) issues and other financial frauds.\n\n'
                'Nevertheless, this presents a structural limit comparatively to traditional Finance. (C. Crenshaw, 2021) The system doesn’t offer any efficient method for determining the actual identity of users. Since the market is not regulated and the identity of user is anonymous, it is difficult to know if the price of assets and the trading volume reflect organic interest or if it is the result of trading manipulation from investors: users or group of users trading collusively can have many public addresses and IP addresses to manipulate, trades, and creates bots to their advantage.\n\n '
                'The vertical aspect of accessibility is the Scalability. Scalability of DeFi platform is the capacity to keep effectiveness and security while providing a service of quality to an exponential population of users at the same time. For instance, if several people from all over the world use a Decentralized Application simultaneously, will the Dapp be able to process the transaction as fast as before and with no error neither breach of security? This matter is still being worked on and would be greatly analyzed in the potential risks.</div>\n\n', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Transparency </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> Another principle of DeFi is Transparency. Transparency in smart contracts allows anyone to review the code of a smart contract, Daap, or Network. (X. Meegan and al. 2021) That principle benefits the fast-paced ecosystem evolution: engineers find open information on how to provide the exact services and can use it to reproduce and innovate faster. The availability of the code makes it also easier for the platforms to be audited.  </div>\n\n', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Interoperability </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> Interoperability is rooted in DeFi since Dapps on the DeFi sector creates the DeFi ecosystem altogether. Indeed, Decentralized Applications provide financial services built on top of distributed networks that have no governing authority and each Dapps is part of DeFi ecosystem. Therefore, the purpose is to make those applications interact and be connected in many aspects to enhance user interaction and increase liquidity in the sector. New protocols like bridges and layers are being created to bound major blockchains from one another. </div>\n\n', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Business Process Automated </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> Finally, Business Process Automated must be the most obvious principles. It allows the DeFi Industry to be totally self-operational without need for intermediation or any kind of human intervention thanks to the technology of artificial intelligence, cloud computer, DLT which are fundamental technologies of DeFi. </div>\n\n', unsafe_allow_html=True)

#PART I - C : TradFi VS DeFi
    st.subheader("C.	Traditional Finance System VS Decentralized Finance system")
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 2. Traditional financial system and Decentralized financial system </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    TradFi_DeFi = Image.open("TradFi_DeFi.png")

    st.image(TradFi_DeFi, width=700)
    st.markdown('<div style="text-align: justify"> Source: Stably </div>', unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('<div style="text-align: justify"> Traditional finance encompasses 3 core principles not present in DeFi ones. The system is Centralized, Regulated, and has high entry barriers. </div>', unsafe_allow_html=True)
    st.markdown('**<div style="text-align: justify"> Centralization </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> The traditional Finance is centralized which means that stakeholders of the market use intermediaries such as bankers, brokers, and all kind of middlemen to make both side of a market to interact with each other. All intermediary roles are regulated by the law which creates trust in the system. To incentivize the middlemen and pay for that regulation system that create trust, the services require fees to be paid by both sides of the transactions. On the opposite, Decentralized finance is built on technology. And every smart contract created are registered on a blockchain protocol that share the information of the smart contract transaction with all other computers connected to the Blockchain too. This system of shares by computer annihilates the need for an intermediary such as what there is in traditional finance, leading to disintermediation. People don’t enter in contact with an intermediary but connect themselves to the blockchain via a Decentralized applications that would trigger a smart contract to execute transactions between 2 public addresses or more. </div>', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Exclusivity </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> Entry in traditional finance is very selective: Entrepreneurs that wants to create a new institution need to get all validations and reunite the right amount of money to begin a business in the sector. Same for users, the access to services is often permissioned by the amount of founds owned as well as the geographic location. For example, remittances fees between different country are greatly expensive limiting users in the amount of money to be sent out from place to another one. Moreover, same services are not offer in every country: Many developing countries such as India cannot access long term loans or even the most trivial underbanked services. This situation wrongs them and limit their financial options. '
                'On the contrary, DeFi is inclusive and offer to every users the same opportunities with lower fees. This promises an open financial system that could benefit people from countries with illiquid currencies or huge boundaries to financial services access due to undeveloped financial infrastructures, corrupted or unregulated field, inducing high transaction fees of all sorts to the detriment of the user. All protocol being open source, it also allows everybody able to code to enter on the DeFi sector and create a blockchain or Decentralized application to develop this new market. </div>', unsafe_allow_html=True)

#PART II - DeFi Performance
    st.title("II.	 DeFi Performance")
#PART II - A: TVL and Market Cap
    st.subheader("A.	TVL and Market Capitalization")
    st.markdown('<div style="text-align: justify"> The metric of the DeFi’s Total Value Locked is the main way to calculate the performance on the sector. It is the overall value of crypto assets deposited in a decentralized finance protocol.  (B. Georges, 2022) TVL has emerged as a key metric for gauging interest in that sector of the crypto industry.\n\n'
                'TVL includes all the coins deposited in all the functions that DeFi protocols offers like Staking, Lending or Borrowing, and acting as and Providers in Liquidity pools. TVL does not reflect the yield that these deposits are expected to earn but only exposes the current amount deposits (or collateral) of digital asset invested in DeFi. Comparatively to the market capitalization, it does not measure the market value of the Dapps neither network. \n\n'
                'Per the definition from Coinmarketcap: To get the current market cap, the circulating supply is multiplied by the current price while TVL is calculated by multiplying the amount of funds that are locked as collateral in the ecosystem by the current price of the assets. The increase in volume locked in DeFi over time represents a growing confidence among the community enthusiasm for long-term potential of DeFi applications.\n\n'
                '*Market Capitalization=Circulating Supply x Price of Token*\n\n'
                '*Total Value Locked = Funds deposited x Price of Token* </div>', unsafe_allow_html=True)

#PART II - B: Current state of DeFi
    st.subheader("B.	Current state of DeFi as of April 6th, 2022")
    st.markdown('<div style="text-align: justify"> DeFi market capitalization is $168.15B according to Coinmarketcap.com on April 6th, 2022 which reveals a 13% dominance on the Crypto Currency Market.'
                'The Total Value locked in DeFi is USD 235B as of April 6th, 2022. It was USD 91.46B on April 6th, 2021, which is a rate of increase of 250% in a year according to analytics firm. At the start of 2020, the combined TVL across all DeFi platforms was around USD 610 millions, mainly owned by Maker Dao. On April 6th, 2022, Curve is the biggest Protocol in DeFi with USD 21.25B of TVL. </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 3. Total Value Locked by Category </div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
                #figure 3
    TLV_by_protocols = requests.get('https://api.llama.fi/protocols').text
    TLV_by_protocols = json.loads(TLV_by_protocols)
    TLV_protocols0 = TLV_by_protocols
    TLV_protocols = pd.DataFrame(TLV_protocols0, columns=[
        "id",
        "name",
        "address",
        "symbol",
        "url",
        "description",
        "chain",
        "logo",
        "audits",
        "audit_note",
        "gecko_id",
        "cmcId",
        "category",
        "chains",
        "module",
        "twitter",
        "audit_links",
        "oracles",
        "language",
        "slug",
        "tvl",
        "chainTvls",
        "change_1h",
        "change_1d",
        "change_7d",
        "staking",
        "fdv",
        "mcap",
        ])
    TLV_protocols_new = TLV_protocols.drop(columns=["address",
                                                    "url",
                                                    "logo",
                                                    "gecko_id",
                                                    "cmcId",
                                                    "module",
                                                    "twitter",
                                                    "audit_note",
                                                    "audit_links",
                                                    "slug"], axis=0)


    fig = px.histogram(TLV_protocols_new, x=TLV_protocols_new["category"], y=TLV_protocols_new["tvl"],
                       title="Total Value Locked by Categories").update_xaxes(categoryorder="total descending")
    fig.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Defi Categories",
        yaxis_title="Total Value Locked(USD)",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )
    st.plotly_chart(fig, use_container_width=True)



    st.markdown('<div style="text-align: justify"> We count 27 DeFi categories as of April 6th, 2022. The outstanding ones are the Decentralized exchanges (Dexes), the Lending platform and the Bridges that sum over USD 30B Locked in their protocols. These principal categories constitute more than 50% of the DeFi Total Value Locked. Nevertheless, many categories are very new, we saw last year the infatuation that created the NFT field or even the gaming industry with its Play-to-Earn opportunities. The result of it created new categories for DeFi. As the market is constantly moving and reinventing itself, we can expect to see new activities arise.\n\n'
                'Source: Defillama </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 3. Total Value Locked by Blockchains </div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
                # figure 4
    TVLallChain = requests.get('https://api.llama.fi/chains').text
    TVLallChain = json.loads(TVLallChain)
    TVL_Chain = TVLallChain
    Current_TVL_AllChain = pd.DataFrame(TVL_Chain, columns=[
        "gecko_id",
        "tvl",
        "tokenSymbol",
        "cmcId",
        "name", ])

    fig_TVL_AllChain = px.histogram(x=Current_TVL_AllChain["name"], y=Current_TVL_AllChain["tvl"],title="Total Value Locked by Blockchain").update_xaxes(categoryorder="total descending")
    fig_TVL_AllChain.update_layout(
        autosize=False,
        width=1000,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Blockchains",
        yaxis_title="Total Value Locked (USD)",
        legend_title="Legend",
        xaxis=(dict(showgrid=False))
    )
    st.plotly_chart(fig_TVL_AllChain, use_container_width=True)
    st.markdown('<div style="text-align: justify"> From a Network perspective, TVL is mainly concentrated in one notable Blockchain aggregating USD 127.7B: Ethereum. It’s dominance of 43% on the Total Value Locked is tremendous and makes of it a paramount asset for the DeFi ecosystem even though other capital networks thrive too: 102 Ledgers are counted in DeFi but Ethereum, Terra, Binance, Avalanche and Solana are respectively the preeminent ones.\n\n'
                'Source: Defillama </div>', unsafe_allow_html=True)

#PART II - C: DeFi performance Analysis
    st.subheader("C.	DeFi performance Analysis from April 2019 to February 28th, 2022")
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> We will use a regression model to evaluate the impact of Bitcoin, Inflation, Ethereum Gas Prices, and the value lost in Exploits on DeFi’s Total Value Locked performance.\n\n\n\n'
                'We gathered the data of Bitcoin Market Capitalization from 2019 to 2022 as well as the data of DeFi TVL and Ethereum TVL for comparison. Indeeed, DeFi being part of the CryptoCurrency sector, it might be influenced by the Bitcoin Market Capitalization. We also gathered the monthly average Consumer Price Index (CPI) From 2019 to 2022. Finally, we decided to use the history of Exploits impact as well as the average daily Ethereum gas price in Gwei to check their link with DeFi overall performance.\n\n'
                'First let’s visualize what happened on the Decentralized Finance market from April 2019 to February 28th, 2022. </div>', unsafe_allow_html=True)

    st.markdown('**<div style="text-align: justify"> Ethereum and Gas fees </div>**', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 5: DeFi and Ethereum TVL history </div>', unsafe_allow_html=True)
    st.markdown("""---""")
                #fig 5
    st.plotly_chart(fig_TVLEthereum_data)
    st.markdown('<div style="text-align: justify"> DeFi historical value began to rise during summer 2020 mainly through Ethereum network that was holding more than 90% of the TVL up until April 2021. Since then, the gap keeps increasing separating the overall DeFi TVL to the Ethereum TVL even though they obviously follow the same trend. On april 6th, 2021, Ethereum own 44% of DeFi TVL. Foremost, the positive trend of those 2 metrics indicates a steady uprise trend for DeFi market but the gap widening in Ethereum share is a sign of market dynamism. New networks enter on the Market to Challenge Ethereum ’status quo.\n\n'
                'Source: Defillama </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Ethereum’s huge gas price impact user’s portfolios. Those ones are tempted to invest in new blockchains, less trusted and with less liquidity but that can offer smaller transaction fees.  </div>', unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 6: Ethereum Gwei Price History </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    #figure  6
    st.plotly_chart(fig_GasPrice, use_container_width=True)
    st.markdown('<div style="text-align: justify"> These transaction fees on Etheureum platform, commonly denoted as Gwei represent the among of gas fees to be paid to perform activity on the chain. The Ethereum token is called Ether and is denoted by ETH. One Gwei is the same as 0.000000 001 ETH. For example, if a transaction cost is 0.000000020 ETH, you would say that the cost was 20 Gwei.Our chart is denoted in Wei, wich represent 1,000,000,000 Gwei. According to the chart those fees are very volatile. They slightly increased since May 2020, corresponding with the losses in Ethereum TVL’share to the benefit of other Chains. \n\n'
                'Source:Defillama </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Ethereum network fees more than tripled between October 2020 and March 2021. These transaction fees were very low up until 2020, when the Ethereum network started to cope with increasing amounts and complex transactions. This coincided with the growing importance of Decentralized Finance, with more services essentially putting more strain on the cryptocurrency''s network. Today''’s'' Ethereum fees represent more than 80% of the fees in Defi according to cryptofees.info. Besides, Ethereum Proof-of-Work consensus requires a lot of carbon usage which refrain institutional investors bounded by Environmental Social Governance (ESG) ethic from investing. </div>', unsafe_allow_html=True)
    st.markdown('**<div style="text-align: justify"> Cryptocurrency Impact and Inflation </div>**', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify"> Bitcoin market capitalization and Inflation index are also factors that could have impacted DeFi’s TVL. Bitcoin being the biggest cryptocurrency asset, its volatility leads the entire cryptocurrency Market of which DeFi tokens and coins are part of. That makes of it a paramount variable for the decentralized finance market too. The cryptocurrency market abides by external factors such as the inflation rate. Thus, comparing Bitcoin Market capitalization history as well as the History of CPI (base 100 in year 1984) to DeFi performance would allow us to get an understanding of their impact on Defi’s TVL. </div>', unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 7 and 8: Bitcoin History and Inflation History</div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
    # figure  7 & 8
    st.plotly_chart(fig_Historical_data, use_container_width=True)
    st.plotly_chart(fig_Inflation, use_container_width=True)
    st.markdown('<div style="text-align: justify"> We immediately recognize a trend between the four variables (DeFi TVL, Ethereum TVL, Bitcoin Market Capitalization and the CPI). January 2020, July 2020, January 2021, and January 2022 are months that registered a regression in CPI rate and indicated a dump in the market prices metrics. This let us believe they are correlated. July 2021 is an anomaly in that case, showing a contradictory trend.\n\n'
                'Source: Data.Nasdaq.com and Bureau of Labor and Statistics </div>', unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('**<div style="text-align: justify"> Exploits </div>**', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 9: DeFi exploits history</div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
    # figure  9
    st.plotly_chart(Exploit_fig, use_container_width=True)
    st.markdown('<div style="text-align: justify"> The rise in value of DeFi protocols has made the reward for successful exploits. More than $13.69B as of April 6th, 2022, has been stolen by DeFi attackers in exploit, scams and hacks according to theblockcrypto.com. The largest DeFi exploits happened to Axie Infinity Ronin’s Chain that got stolen $625m in March 2022. As the hacks keep increasing it is obvious that this situation can worsen in the future if DeFi doesn’t better mitigate this risk.\n\n'
                'Source: theblockcrypto </div>', unsafe_allow_html=True)
    st.markdown("""---""")

#PART II - D: Regression Model
    st.subheader("D.	Multiple Linear Regression Model")

    st.markdown('<div style="text-align: justify"> A regression model will be used to evaluate how much each variable explains the Total Value Locked in DeFi. Although Ethereum has been visualized, we will not integrate it in our model for multicollinearity avoidance with Bitcoin Market Cap variable. The multiple regression equation would describe how the dependent variable DeFi TVL (y) is related to the independent variables (x). Here is the data used: </div>', unsafe_allow_html=True)
    df_model2= df_model2.reset_index(drop=True)
    st.dataframe(df_model2)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 10: Correlation Chart between variables of the model</div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
    # figure  10 - Correlation

    corr_mat = df_model.corr(method='pearson')
    fig = plt.figure(figsize=(20, 10))
    ax = plt.axes()
    sns.heatmap(corr_mat, vmax=1, square=True, annot=True, cmap='cubehelix')
    ax.set_title('Correlation Between Parameters')
    st.pyplot(fig)

    st.markdown('<div style="text-align: justify"> As expected, Bitcoin is strongly correlated to DeFi TVL. Inflation and Exploits variables plays their role too even though it is weird to see the exploit value positively correlated to the TVL but the Gas Price value seems off, certainly because of its small values and the light variance in its distribution comparatively to the other variables. We will keep it in the model to avoid overfitting the model too much, which could fail to predict future reliably. \n\n'
                'Source: Laura Kouadio </div>', unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('<div style="text-align: justify"> We will use the OSL of Least Squares method of Regression that is used to develop an estimated multiple regression equation: the method uses sample data to provide the values of b0,b1,b2,…bn that minimize the sum of squared residuals to better fit the data. </div>', unsafe_allow_html=True)
    #picture of model

    st.markdown('<div style="text-align: justify"> Estimated multiple linear regression:\n\n </div>', unsafe_allow_html=True)
    st.markdown('**_<div style="text-align: center">For ŷ = Dependent Variable and b0,b1,b2,…,bn=Estimates, the multiple regression equation describes how the mean value of y is related to x1,x2,…xn._**\n\n</div>', unsafe_allow_html=True)
    st.markdown('**_<div style="text-align: center">ŷ = b0+b1x1+b2x2+b3x3+b4x4+b5x5_**\n\n'
                "**_ŷ = DeFi Total Value Locked_**\n\n"
                "**_b0 = Constant,  			 x1=Timestamp,   			 x2=Exploit,  x3=Bitcoin MCap, 		 x4=Inflation,		x5=GasPrice(Wei)_** </div>", unsafe_allow_html=True)

    st.markdown('<div style="text-align: justify">Implementation:\n\n</div>', unsafe_allow_html=True)
    st.markdown('**_<div style="text-align: center">DeFi Total Value Locked = b0 + b1Timestamp + b2Exploit + b3Bitcoin Mcap + b4Inflation Rate + b5GasPrice(Wei)_**\n\n</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify">Model Results: </div>', unsafe_allow_html=True)

    #predict model summary add the picture
    model_summary = Image.open("model_summary.png")
    st.image(model_summary, width=700)

    st.markdown('<div style="text-align: justify"> Model Predicted:\n\n</div>', unsafe_allow_html=True)
    st.markdown('**_<div style="text-align: center">(DeFi Total Value Locked) = 581,594,813+163.087 Timestamp-0.014 Exploit+0.002 Bitcoin Mcap+424,669 Inflation Rate+17,388 GasPrice(Wei)_**\n\n', unsafe_allow_html=True)
    st.markdown('<div style="text-align: justify">Model is explaining 82% of the Total DeFi value according to statsmodel library and the model parameters. Exploits happened to be negatively correlated to DeFi and it makes more sense. </div>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 11: Multi linear regression prediction </div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
    # figure  11
    prediction_chart = Image.open("prediction_chart.png")
    st.image(prediction_chart, width=700)
    st.markdown('<div style="text-align: justify"> From the graph we see that the predicted value’s trend is quite close to the actual scatter point describing the actual value. Therefore, we can say that the date, the number of exploits, the bitcoin market capitalization value, the inflation rate as well as the gas price are parameters explaining the Total value Locked for DeFi.\n\n'
                'Source: Laura Kouadio </div>', unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('**<div style="text-align: justify"> The regulation factors </div>**', unsafe_allow_html=True)

    st.markdown('<div style="text-align: justify"> 18% is not explained by the model. It that gap remaining can be related to non-numerical data that affected the market in 2021 such as Regulation and Environmental Social Governance (ESG) concerns.\n\n'
    'In Mai 2020, China government declared they would ban the Cryptocurrency mining definitively from its country. According to M.Sigalos 2021, Beijing made it clear that crypto mining stands in the way of its aggressive climate targets, as it pushes to achieve carbon neutrality by 2060. Besides, the government also argue that it opens the door to financial crime.\n\n'
    'Unfortunately, this led to a huge crash of the Bitcoin price that created a domino effect on the crypto market in general. </div>', unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 12: Cambridge Bitcoin Electric Consumption Index by Country   </div>',
                unsafe_allow_html=True)
    st.markdown("""---""")
    # figure  12
    Hashrate_country = Image.open("Hashrate_country.png")
    st.image(Hashrate_country, width=700)
    st.markdown('<div style="text-align: justify"> 75.5% of the mining share were occurring from IP addresses located in China before the announcement. Today, this figures average zero percent for China.\n\n'
                'The graph unveils also the new importance of Kazakhstan in the bitcoin ecosystem as they own 13.1% of the mining space (network hash rate) which makes of them the second largest share older behind the United States of America (35.5%) as of April 2022, according to the Cambridge Center for Alternative Finance. This revelation urges to keep an eye on the political regulation in place in the country.\n\n'
                'Source: ccaf.io </div>', unsafe_allow_html=True)
    st.markdown("""---""")

#PART III - The future of DEFI
    st.title("III.	 The future of DEFI ")
    st.markdown('<div style="text-align: justify"> DeFi is at its infancy and will develop itself even more in the next time but will surely encounter many challenges. Before it becomes widely accepted and used, the sector needs to abide by the politic establishment. Cybersecurity, Tech Innovation, Environmental issues, Monetary policy, Crypto regulations, and CBDCs are topics that would be addressed to define future of DeFi. </div>', unsafe_allow_html=True)

#PART III - A: Cybersecurity
    st.subheader(' A.	Cybersecurity')
    st.markdown('<div style="text-align: justify"> DeFi Market TVL trend showed that despite the drawbacks, the sector intends to keep thriving to innovate and always offer better services to its users. To continuing performing Decentralized Finance must equip itself against hacking risk occurrence.\n\n'
                'First, it is of primary importance to recreate an environment of safety to limit exploits. The value lost to hacks and exploits crossed the billion-dollar in late 2021, making it clear that meaningful security remains a challenge for the industry. The proliferation of hasty forks, unaudited deployments, and outright scams led to hundreds of millions of dollars of unnecessary losses. '
                'Certik Auditor ‘s State of DeFi Security Report 2021 declared that Centralization issues were the common attack vector. '
                'Auditors came across 286 discrete centralization risks throughout the 1,737 audits performed in 2021. Centralization is antithetical to DeFi and poses major security risks as single points of failure can be exploited by dedicated hackers and malicious insiders alike. '
                'This underscores the importance of decentralization and highlights the fact that many projects still have work to do to reach this goal. Especially now that we saw the bound between exploits and DeFi.\n\n'
                ' The creation of multi-channel and cross channels can also be a risk for DeFi especially because of their poor code. The EVM is an important aspect of the cross-chain model that allows other networks to communicate with Ethereum. So far: four major EVM-compatible blockchains: Avalanche Contract Chain (C-Chain), Binance Smart Chain (BSC), Fantom and Polygon. '
                'The creation of rollups (zero-knowledge and optimistic roll-ups) or Layer 2 protocols, which enter in relationship with Layer 1 blockchains promise lower transaction fees and faster transactions while leveraging the security of the underlying base layer. In addition, with Polkadot and the Cosmos Inter-Blockchain Communication Protocol (IBC), there are efforts to establish a network of different blockchains capable of communicating with each other. Finally, interoperability between different blockchain ecosystems through bridges and cross-chain protocols is also being worked on diligently. '
                'Theses technologic improvements are a path toward a more user-friendly ecosystem that promote user adoption. Nevertheless, it still represents a risk to develop an even more complex environment creating more breaches from new service processes like Bridges. DeFi needs to be cautious to protect digital assets locked on their platforms. Indeed, the Ethereum Blockchain creator V. '
                'Buterin explained in a reddit post the reason why he believes the cross-chain can bring more damaging hacks than hacks happening on Layer 1 or layer 2 networks; As Bridges channels are not fully backed by any Blockchain consensus, they cannot retrieve users’ money if they get hacked, which make them vulnerable. '
                'On the contrary when the that same attack occurs on a blockchain, it would just have invalidated the transaction but at least the value of our money would still be the same. </div>', unsafe_allow_html=True)

#PART III - B: ESG
    st.subheader(' B.	Environmental Social Governance (ESG)')
    st.markdown('<div style="text-align: justify"> Ethereum’s transition from POW to POS consensus can be a growth opportunity for DeFi future performance. Ethereum that currently as a high carbon footprint due to POW method, which creates debates about the legitimacy of investing in the blockchain and in DeFi in general. This ESG concern is major notably for investors trying to avoid environmental risk but also influence risk and compliance risk from their respective governmental institutions. For instance, Tesla that announced in May 2021 that it will no longer accept Bitcoin over climate concerns. Once major Cryptocurrencies such as Bitcoin and Ethereum would be safer for the environment, more investors would be interested in their value. When Ethereum transitions, a powerful hardware would not be needed to create the transaction on the network, making that blockchain eco-friendly and opening the door to high value investors such as VC, hedge fund, Dao, private equity to increase the market capitalization of that coin and lead to a greater DeFi influence. Moreover, transaction fees on the channel would be less expensive and therefore would lead to enlarge the community usage. </div>', unsafe_allow_html=True)

#PART III - C: The Inflation

    st.subheader(' C.	The Inflation')
    st.markdown('<div style="text-align: justify"> As seen in our regression model, DeFi is react to inflation fluctuations and therefore inflation’s trend would certainly impact DeFi Total Value performance in the future. The price of Inflation has been anomaly high these last two year mainly because of the global covid outbreak but the prices have been predicted by many authorities to go back to its normal state. </div>', unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown(
        '<div style="text-align: justify"> Figure 13: IMF, FOMC, European Commission, OECD and USDA’s Inflation Prediction    </div>',
        unsafe_allow_html=True)
    st.markdown("""---""")
    # figure  13
    CPI_predictions = Image.open("CPI_predictions.png")
    st.image(CPI_predictions, width=700)
    st.markdown('<div style="text-align: justify"> Indeed, according to the Inflation prediction aggregator Knoema the IMF, The FOMC, the European Commission and the OECD and the USDA, put the US CPI inflation within the range of 1.69% to 4.30% percent in 2022 and around 2.5% in 2023. Almost all agencies predicted that CPI inflation will decrease in 2022 compared to 2021. According to the regressor model that we used, that change would lower the increase of DeFi TVL.\n\n'
                'Source: Knoema </div>', unsafe_allow_html=True)
    st.markdown("""---""")

#PART III - D: Crypto Regulations
    st.subheader('D.	Crypto Regulations')

    st.markdown('<div style="text-align: justify"> The regulation aspect is the variable that could create the biggest impact on DeFi. It would redefine the rules of investment and deposits of collateral in Dapps. Fear uncertainty and doubt results from not knowing whether a country would one day release a regulation in favor or in disfavor of DeFi.  </div>', unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown(
        '<div style="text-align: justify"> Figure 14: Global States of Cryptocurrency Regulation by Country    </div>',
        unsafe_allow_html=True)
    st.markdown("""---""")
    #figure 14
    Regulation_States = Image.open("Regulation_States.png")
    st.image(Regulation_States, width=700)

    st.markdown('<div style="text-align: justify">Many Countries already declared themselves favorable to the crypto currency adoption such as El Salvador where Bitcoin has been declared official currency since 2021 by populist president N. Bukele. On the other hand, China decided to outlaw cryptocurrencies according to the Law Library of Congress, 9 other countries decided to forbit access to the Crypto currency market from their citizen by totally banning it.\n\n'
                'Source: Library of Congress. </div>',unsafe_allow_html=True)
    st.markdown("""---""")

    st.markdown('<div style="text-align: justify"> On a US focus, we are waiting for the Lummis bill to be enacted. That regulation would govern the cryptocurrency market, protect the crypto investors and even regulate the stable coins. As federal bill, it would be overseen by the Security and Exchange Commission as well as the Commodity Futures Trading Commission.\n\n'
                'The bill created by Ron Wyden and Cynthia Lummis senators advocating for innovation could be auspicious for the crypto stakeholders but result of it would depend on its final version adopted by the senate.\n\n'
                '“Digital assets are here to stay in our financial system and the decisions we make now will have impacts far into the future,” Senator Lummis said. “We need to be fostering innovation, not stifling it, if we are going to maintain America’s position as the global financial leader. I’m proud to introduce this bipartisan bill to ensure that our tax system reflects the realities of digital assets and distributed ledger technology.” \n\n'
                'Regarding the European Union, the Market in Crypto-Asset (MiCA) regulation is currently in creation by the parliamentarian Stefan Berger. According to the European Parliament, the initiative aims to support innovation and fair competition by creating a framework for the issuance, and provision of services related to crypto assets. In addition, it aims to ensure a high level of consumer and investor protection and market integrity in the crypto-asset markets, as well as address financial stability and monetary policy risks that could arise from a wide use of crypto-assets and DLT-based solutions in financial markets. \n\n'
                'All these regulations happened during 2021 or are currently on the blink of happening. It premises many changes that could propel DeFi ecosystem to a faster maturation by leading to less volatility in the market and a steadier increase but also reinsure investors now that the market is regulated.</div>',unsafe_allow_html=True)

#PART III - E: CBDC
    st.subheader(' E.	CBDC')
    st.markdown('<div style="text-align: justify"> Last be not least, many countries got inspired by the blockchain technology and plan to creates a new type of token based digital money called Central Bank Digital Assets (CBDC). This would be an alternative payment pegged on sovereign currencies to the already existing current card and bank base payment system. \n\n'
                'According to Citi Bank report on FUTURE OF MONEY Crypto, CBDCs and 21st Century Cash (2021), government token could improve targeting of monetary and fiscal policy, promotes inclusion and universality, reduce cost especially for remittances transfer costs, and improve efficiency in domestic payments. Moreover, comparatively to the Decentralized Finance, it improves management of financial crime risks and informal economy.\n\n'
                'Only Bahamas and Nigeria have created their CBDC. The Central Bank of Nigeria (CBN) launched the eNaira in 2021. That CBDC is a liability of the CBN. It also uses the blockchain technology and is stored in digital wallets.  It can be used for payment transactions, and it can be transferred digitally to anyone in the world with an eNaira wallet (J.Ree, 2021). However, the eNaira features stringent access right controlled by the central bank. Moreover, unlike crypto assets, the eNaira is not a financial asset in itself but a digital form of a national currency and draws its value from the physical naira, to which it is pegged at parity.\n\n'
                'Biggest world economy like China started developing its Digital Currency Electronic Payment (DCEP) CBDC in 2014 and tested a pilot in 2020. We expect China’s sprint to a cashless society will drive DCEP adoption for retail use within five years. USA with the Diem and European Union with the digital Euro still are on a state of research so far.</div>', unsafe_allow_html=True)

    st.markdown("""---""")
    st.markdown('<div style="text-align: justify"> Figure 15: Central Bank Digital Currencies Status – April 2022   </div>',unsafe_allow_html=True)
    st.markdown("""---""")
    # figure 15
    CBDC_states = Image.open("CBDC_states.png")
    st.image(CBDC_states, width=700)
    st.markdown('<div style="text-align: justify"> As seen on the chart, CBDC is still at its genesis and will be an impactful innovation in the traditional financial system. The future tokenized and account-based money, centralized and decentralized systems, will all co-exist which might greatly impact DeFi performance in the future.\n\n'
                'Source: cbdctracker.org </div>', unsafe_allow_html=True)
    st.markdown("""---""")

#PART IV - Conclusion
    st.title('IV. Conclusion')
    st.markdown('<div style="text-align: justify"> DeFi offers many good opportunities to its users but like every revolution as its commencement, it hurt itself to decisive interrogations for it future. The concerns discussed before such as security, ESG, inflation, and technologic evolution would determine the exact Total Value Locked that we could expect in DeFi for the next years. The sector increase of more than 250% in two year and that phenomenon can potentially continue to increase as such until regulation and new monetary systems entry arise, but it would certainly reduce its rate of increase after those events unfold. That would be a sign of market stability, with less volatility, more security and a regulation frame well established to protect its users. Moreover, we can prepare ourselves to attend an unprecedented financial system shift as for the first time ever, the world would experience, the traditional financial system, the decentralized financial system, and the government’s digital money.</div>', unsafe_allow_html=True)

#Reference
    st.title(' Reference')
    st.markdown('<div style="text-align: justify">Crenshaw, C. (2021, November 9). Statement on DeFi Risks, Regulations, and Opportunities. SEC Emblem. https://www.sec.gov/news/statement/crenshaw-defi-20211109\n\n'
                'Meegan, X and al. (2021).  Lessons Learned from Decentralised Finance. ING Wholesale Banking. https://www.ingwb.com/binaries/content/assets/insights/themes/distributed-ledger-technology/defi_white_paper_v2.0.pdf\n\n'
                'Stably (2019). Decentralized Finance vs. Traditional Finance: What You Need To Know. Medium.  https://medium.com/stably-blog/decentralized-finance-vs-traditional-finance-what-you-need-to-know-3b57aed7a0c2 \n\n'
                'B. Georges (2022). Why TVL Matters in DeFi: Total Value Locked Explained. Coindesk. https://www.coindesk.com/learn/why-tvl-matters-in-defi-total-value-locked-explained/#:~:text=Total%20value%20locked%20(TVL)%20is,sector%20of%20the%20crypto%20industry\n\n'
                'M. Sigalos (2021), Inside China’s underground crypto mining operation, where people are risking it all to make bitcoin https://www.cnbc.com/2021/12/18/chinas-underground-bitcoin-miners-.html \n\n'
                'Cambridge Center for alternative finance, 2022 https://ccaf.io/cbeci/mining_map\n\n'
                'Certik. (2021). State of Defi Security Report 2021. www.certik.com\n\n'
                'Vitalik Buterin (2021) Reddit. https://old.reddit.com/r/ethereum/comments/rwojtk/ama_we_are_the_efs_research_team_pt_7_07_january/hrngyk8/ \n\n'
                "Knoema.com (2021). https://knoema.com/kyaewad/us-inflation-forecast-2022-2023-and-long-term-to-2030-data-and-charts#:~:text=Different%20agencies'%20predictions%20differ%2C%20putting,in%202022%20compared%20to%202021\n\n"
                "Law Library of Congress (2021). Regulation of Cryptocurrency Around the World: November 2021 Update Law Library of Congress. Global Legal Research Directorate. https://tile.loc.gov/storage-services/service/ll/llglrd/2021687419/2021687419.pdf\n\n"
                "Cynthia Lummis. (2021). Wyden & Lummis introduce Bill to fix broker definition for digital assets. Senate Gov. https://www.lummis.senate.gov/press-releases/wyden-lummis-introduce-bill-to-fix-broker-definition-for-digital-assets/\n\n"
                "Stefan Berger. (2022). Proposal for a regulation of the European Parliament and of the council on markets in Crypto-Assets. European Parliament. https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-crypto-assets-1\n\n"
                "J.Ree. (2021). Five Observations on Nigeria’s Central Bank Digital Currency. IMF. https://www.imf.org/en/News/Articles/2021/11/15/na111621-five-observations-on-nigerias-central-bank-digital-currency \n\n"
                "I.Michalev and al. (2022). Today's Central Bank Digital Currencies Status. Cbdctracker. https://cbdctracker.org/\n\n"
                "R. Ghose, Y. Tian, R. Shah, J. Zhang, K. Master. (2021). Citi Future of Money: Crypto, CBDCs and 21st Century Cash. Citi Bank. Citi GPS: Global Perspectives & Solutions.\n\n"
                "https://defillama.com/docs/api\n\n"
                "https://etherscan.io/chart/gasprice\n\n"
                "https://data.nasdaq.com/data/BCHAIN/MKTCP-bitcoin-market-capitalization\n\n"
                "https://data.bls.gov/pdq/SurveyOutputServlet\n\n"
                "https://coinmarketcap.com/\n\n"
                "https://cryptofees.info/\n\n"
                "https://theblockcrypto.com/ </div>", unsafe_allow_html=True)





if choose == "Crypto Categories Vizualization - Engineering with Python":

    #Page Layout
    st.title(":bar_chart: Crypto Categories Dashboard")
    st.markdown("This app retrieves the Categories performance on the Crypto Market from **CoinGecko**!")

    #About
    expander_bar = st.expander("About")
    expander_bar.markdown("""
    * **Objectif:** Learn whose industries are being currently disrupted by the Blockchain Technolgy and what are their value on the Crypto Market as of today.
    * **Python libraries:** Pandas, Streamlit, Numpy, Plotly.express, Json
    * **Data source:** [CoinGecko](https://www.coingecko.com/).
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
                              title="Top 15 Crypto Market Capitalization",
                              template="plotly_white").update_yaxes(
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

elif choose =="Crypto Exchanges Analysis with Tableau":
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
         html_temp = """<div class='tableauPlaceholder' id='viz1650000855821' style='position: relative'>
            <noscript>
            <a href='#'>
            <img alt='Top 100 crypto Exchanges by Traded VolumeHave you ever wondered which crypto-currency exchanges are the most successful and from where they work their magic from?This dashboard presents an analysis of the top 100 crypto-currency exchanges listed on Coi ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;Top100CryptoExchanges&#47;Story1&#47;1_rss.png' style='border: none' />
            </a>
            </noscript>
            <object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='Top100CryptoExchanges&#47;Story1' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;Top100CryptoExchanges&#47;Story1&#47;1.png' /> 
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
            <param name='filter' value='publish=yes' />
            </object>
            </div>                
            <script type='text/javascript'>                   
        
            var divElement = document.getElementById('viz1650000855821');                    
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
            f'Link to the dashboard on Tableau Public [here](https://public.tableau.com/views/Top100CryptoExchanges/Story1?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)')
        st.markdown(
            f"**Data source and information about data collect can be found on [Coin Gecko - API](https://www.coingecko.com/en/api)**")
        max_width_str = f"max-width: 1030px;"
        st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",
                    unsafe_allow_html=True)

        # the controller


    def load_page():
        sidebar_info()
        main()



elif choose =="Business Performance Analysis with SQL":

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
