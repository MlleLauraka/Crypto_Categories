import streamlit as st
import streamlit.components.v1 as components

def app():
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
        return sidebar_info()

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
        return main()
    
    if __name__ == "__main__":
        main()

        st.markdown(f'Link to the dashboard on Tableau Public [here](https://public.tableau.com/app/profile/laura5733/viz/Top100CryptoExchangesAnalysisDaily/Story1#1)')
        st.markdown(f"**Data source and information about data collect can be found on [Coin Gecko - API](https://www.coingecko.com/en/api)**")
        st.markdown( f"**Credit: [Okoh Anita](https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b)**")
        max_width_str = f"max-width: 1030px;"
        st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)


  
