# Libraries

import pandas as pd 
import plotly.express as px
import streamlit as st
import numpy as np
from datetime import date
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as Rect
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.pylab as pylab
import database as db
from PIL import Image
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import os

# RECUP LA DATA
# Retrieve the path to the current folders
current_path = os.getcwd()

# Get the path to the csv file folder - in this case the 'data' file
csv_path = os.path.join(current_path, 'data')

# A EXPLIQUER ICI
for file in os.listdir(csv_path):
    fd = pd.read_csv(os.path.join(csv_path, file))
    globals()[file.rpartition(".")[0]] = fd

today = datetime.strftime(datetime.now(), "%d/%m/%Y")
t = today

# LOGO
st.set_page_config(page_title="ASTROTOOL", layout="wide")
logo = Image.open(r'logo.png')
epp = Image.open(r'ep.png')

col1, col2, col3 = st.columns([8, 7, 2])

with col1:
    st.write(' ')

with col2:
    st.image(logo)

with col3:
    st.write(' ')

# --- USER AUTHENTIFICATION ---

users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "astrotool_dashboard", "abcdef", cookie_expiry_days=30)

names, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username / Password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

# --- DASHBOARD ---

if authentication_status:

    st.markdown(f"Welcome aboard {names}, enjoy our Alpha Version!")

    m = fluchart.copy()
    helio = helio.copy()
    #helio = helio.iloc[::, helio.columns !='Date'].apply(np.floor)
    helio_cum = helio_cum.copy()
    heliox = heliox.copy()
    geox = geox.copy()
    geo = geo.copy()
    hm = helio_main.copy()
    gm = geo_main.copy()

    m1 = NatSq.copy()
    m2 = Spi.copy()
    m3 = TrTr.copy()
    m4 = TrNa.copy()
    m5 = addPrice.copy()
    m6 = Fib.copy()
    m7 = FutureDate.copy()
    m8 = Mult.copy()
    m9 = Natal.copy()
    m10 = PriceTime.copy()
    m11 = Retro.copy()
    m12 = Sq9.copy()

    mn1 = aspects_h_tr.copy()
    mn2 = aspects_h_na.copy()
    mn3 = aspects_g_tr.copy()
    mn4 = aspects_g_na.copy()
    mn5 = dec_lat.copy()
    mn6 = retro_asp.copy()
    mn6.fillna(' ', inplace=True)
    mn7 = tools.copy()
    mn7.fillna(' ', inplace=True)

    # ONGLETS

    help, main,chart,Method = st.tabs(["Info", "Main", "Chart","Method"])

    with help:

        col0,col00 = st.columns([4,3])

        with col0:
            st.title('AstroTool Info Page')
            
            gt = Image.open(r'gtlogo.png')

            st.markdown('''
            **This WebApp of Astrotool** is a gift from **[Geometric Thinking](https://geometricthinking.com "Geometric Thinking")** and the developpers **Amir & Sachith** to the world.  We have learned that there is a **very unique way** to *read price charts* for geometric support and resistance.  **AND** we have found that there are ways to discern, **far in advance, of the dates when turns are likely to occur**. We call those dates **ENERGY POINTS (EPs)**.  This WebApp will highlight future EPS for you.  *It will not tell you which way a market will break*, but **it will give you a heads up when to pay close attention to a chart for a trading opportunity**.
            * Most of the workings of the file is not available inside this **Web-App** and/or **locked** to prevent the user from breaking it.
            * The **CHART** page is self-explanatory.  The dates with the highest bars are the dates to watch the most.  Note that the ep dates should be viewed as +/- 1 day.  In other words, an ep may show up a day early or a day late.
            * The **MAIN** page is chock full of astrological data related to the passage of time since key dates in BTC history.  Those dates are visible on the left side of the page.  As of the date of publication, the last date entered was 06/18/22.  
            * If you study the data on the Main page, you will gain at least a glimmer of insight into the kind of things we look at.  For a more thorough and complete understanding, you should attend a class, if and when Geometric Thinking holds another class.  
            The founder of Geometric Thinking is no longer a young man and will not be involved with the markets for more than a few more years.  This workbook is given to help struggling traders by giving away some of the insights we PRAYED for, when we were starting out.  
            **We wish you the very best success in your trading career**.
            ''')
            st.header('Who are we?')

            st.image(gt)
            
            st.markdown('''
            We opened Geometric Thinking in July 2017 and have now taught literally many hundreds of traders worldwide the art of Geometric Thinking.  
            * Geometric Thinking focuses on a unique understanding of how geometry and natural law focuses the minds of traders (en masse) such that **there are points in time and price where we can forecast trend changes are most likely to occur.**

            * Knowing in advance, for example, that a coin like BTC will likely reach an Energy Point (ep) in time 2 weeks in advance gives the trader an almost “unfair advantage” over other traders.  It becomes even more unfair if the Geometric Thinker realizes not only that a date 2 weeks away is a prime time to wait and watch for, but also realizes that there are forecast-able prices associated with that date.
            * If you’ve been trading for awhile, you already know that this business is cut-throat. It is vicious and even very smart people typically lose everything over time.  If you are honest with yourself you know that **the classic trading techniques, divergences, moving averages, etc simply do not work consistently.**

            * So what does work consistently?  What will give you an unfair advantage over other traders?  **Geometry and natural law**.  

            * Knowing these things will not guarantee that you will win.  It simply gives you an advantage.  Look at the picture above of the man holding two aces in the hole.  Does this guarantee that he will win the hand?  **No.  There are still 100 ways to lose, even with a pair of aces in the hole.**  If he were playing against professional poker players he would still need to master the game right?  He would still need to hide his tells, learn to bluff, learn game mathematics, etc, in order to be a consistent winner.  So too with Geometric Thinking and trading.

            * But still, imagine if EVERY hand, or nearly every hand, that man was dealt two aces in the hole (without cheating).  **UNFAIR ADVANTAGE, right?**    We can arrange for you to be dealt two aces in the hole more often than not.  If you will combine that with the dedication to master this business, you can become a consistent winner.  **We believe this 100%**.
            ''')
            
            st.header('Why should you care?')
            st.markdown('''
            Whether you care to believe this or not, dates such as the 12/17/2017 high were seen weeks in advance as a date for a possible top.  The 3/12/2020 low was also forecasted as a possible low well more than a month in advance.  **WE LITERALLY TWEETED TO THE WORLD, AND BLOGGED, THAT THE NOV 2021 TOP WAS IN, A WEEK OR SO AFTER THE FACT, WHEN PRICE WAS STILL ~ 65000!**  To the best of our knowledge we are the only ones who did that. 

            Whether you choose to believe this or not, I assure you it is true that at the very least, several hundred geometric thinking traders know which dates to watch, and which prices, LONG before other traders do.  Does that seem fair to you?  Does that matter?  Should you care?  **We think so.**
            
            You can join us in our [Telegram Channel](https://t.me/joinchat/FKSNuqrZpjhlZTJi)
            ''')

        with col00:
                spa = Image.open(r'space.png')
                st.markdown('*The Solar System - Spirals everywhere* | taken from "A Little Book of Coincidence" by John Southcliffe Martineau')
                st.image(spa)
                astrotoologo = Image.open(r'astro.png')
                sva = Image.open(r'sva.png')
                st.image(sva)
                st.markdown('*Amir & Sachith logo*')
                st.markdown(''' This fully implemented Web-App, python ready has been created as part of a **Memory Paper** for **[DU Data Analytics @ University Panthéon Sorbonne Paris](https://formations.pantheonsorbonne.fr/fr/catalogue-des-formations/diplome-d-universite-DU/diplome-d-universite-KBVXM363/diplome-d-universite-sorbonne-data-analytics-KPMK3V7Z.html)**. The two developers are **[Amir Lehmam](https://fr.linkedin.com/in/amirlehmam)** & **[Sachith Galbokka](https://fr.linkedin.com/in/sachith-galbokka-b22187204)**. Both being passionate about trading & programming, they linked their passion to their interest to create this Web-App thanks to our mentor **[Jim Fredrickson](https://geometricthinking.com/about-us/)** - *creator of GeometricThinking* - that allowed us to translate Astrotool from excel to python and make a web-app off it... We also want to thanks **[Marc Arthure DIAYE](http://marc-arthur.diaye.monsite-orange.fr/)** - *director of DU Data Analytics* - for allowing us AstroTool as a memory paper subject!''')

    with main:

        h1,h2,h3,h4=st.tabs(["Helio", "Geo", "Tools", "Sq9"])

        with h1:

            col0,col00 = st.columns([4,3])
            
            with col0:
                    def highlight_everyother(s):
                        return ['background-color: yellow; color:black' if x%2==1 else ''
                            for x in range(len(s))]
                    st.dataframe(hm.style.apply(highlight_everyother))

            with col00:
                    st.markdown("**Transit Aspects**")
                    for col in mn1.columns[3:]:
                        mn1 = mn1.astype({col: int})
                    st.dataframe(mn1.style.background_gradient(cmap='Blues'))
                    st.markdown("**Natal Aspects**")
                    for col in mn2.columns[3:]:
                        mn2 = mn2.astype({col: int})
                    st.dataframe(mn2.style.background_gradient(cmap='Blues'))
                    st.markdown("7 = 7.5° & 22 = 22.5°")

            help1 = Image.open(r'mainhelp.png')
            st.image(help1)

        with h2:

            col0,col00 = st.columns([6.618,3])
            with col0:
                    def highlight_everyother(s):
                        return ['background-color: orange; color:black' if x%2==1 else ''
                            for x in range(len(s))]
                    st.dataframe(gm.style.apply(highlight_everyother))
            with col00:
                st.markdown("**Transit Aspects**")
                for col in mn3.columns[3:]:
                    mn3 = mn3.astype({col: int})
                st.dataframe(mn3.style.background_gradient(cmap='Blues'))
                st.markdown("**Natal Aspects**")
                for col in mn4.columns[3:]:
                    mn4 = mn4.astype({col: int})
                st.dataframe(mn4.style.background_gradient(cmap='Blues'))
                st.markdown("7 = 7.5° & 22 = 22.5°")

            help2 = Image.open(r'mainhelp.png')
            st.image(help2)
        
        with h3:

            col5, col9 = st.columns([6,4])
            with col5:
                st.markdown("**Retro**")
                st.dataframe(mn6.style.background_gradient(cmap='Blues'))
            with col9:
                for col in mn5.columns[1:]:
                    mn5 = mn5.astype({col: int})
                st.markdown("**Declination/Latitude**")
                st.dataframe(mn5.style.background_gradient(cmap='Blues'))

            st.markdown("**Moon/Node/Dec/Lat**")
            col7, col8 = st.columns([12,0.2])
            with col7:
                st.dataframe(mn7.style.background_gradient(cmap='Blues'))

        with h4:

            col0,col00 = st.columns([2,1])
            sq1 = Image.open(r'sq9.jpg')
            sq2 = Image.open(r'SQ2.png')

            with col0:
                st.image(sq1)

            with col00:
                st.image(sq2)
                st.markdown("Here is an aerial view of the **Khufru pyramid in Egypt**, some claim that the ancient builders bequeathed these pyramids to us as an *astro-calculator*, which **W.D Gann** calls the ***Square of 9***. It has been discovered that each **45°** row of this pyramid (**8 sides**) has a **small inclination**, was this intentional to reveal the importance of the **45° degree**? Or as they call it, an architectural coincidence...")
                original_title = '**<p style="font-family:sans-serif; color:Red; font-size: 20px;">**Heliocentric (H)**</p>**'
                st.markdown(original_title, unsafe_allow_html=True)
                for col in helio.columns[1:]:
                    helio = helio.astype({col: int})
                st.dataframe(helio)
                original_titles = '**<p style="font-family:sans-serif; color:Aqua; font-size: 20px;">**Geocentric (G)**</p>**'
                st.markdown(original_titles, unsafe_allow_html=True)
                for col in geo.columns[1:]:
                    geo = geo.astype({col: int})
                st.dataframe(geo) 

    with chart:
        st.title('**Energy Points Chart (next 3 months)**')
        figui = px.bar(m, x="Date", y="Magnitude", hover_data=['Date', 'Magnitude'], color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis,
             height=618).update_layout(xaxis={"rangeslider":{"visible":True}})
        st.plotly_chart(figui, use_container_width=True)
        st.markdown('**Energy Points Hits on BTC @ last 2 years**')
        df = btcusd_d.copy()

        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'])])
        fig.add_vline(x=1, x0="2020-12-05", x1="2020-12-05", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-01-08", x1="2021-01-08", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-01-22", x1="2021-01-22", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-02-26", x1="2021-02-26", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-03-14", x1="2021-03-14", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-03-24", x1="2021-03-24", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-04-15", x1="2021-04-15", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-05-05", x1="2021-05-05", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-05-18", x1="2021-05-18", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-06-10", x1="2021-06-10", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-06-19", x1="2021-06-19", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-07-06", x1="2021-07-06", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-07-18", x1="2021-07-18", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-08-02", x1="2021-08-02", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-08-20", x1="2021-08-20", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-09-03", x1="2021-09-03", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-09-24", x1="2021-09-24", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-10-20", x1="2021-10-20", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-10-30", x1="2021-10-30", line_width=1, line_color="blue")       
        fig.add_vline(x=1, x0="2021-11-10", x1="2021-11-10", line_width=1, line_color="blue")     
        fig.add_vline(x=1, x0="2021-12-05", x1="2021-12-05", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2021-12-30", x1="2021-12-30", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-01-13", x1="2022-01-13", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-01-25", x1="2022-01-25", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-02-08", x1="2022-02-08", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-02-17", x1="2022-02-17", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-02-24", x1="2022-02-24", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-03-02", x1="2022-03-02", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-03-20", x1="2022-03-20", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-04-06", x1="2022-04-06", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-04-19", x1="2022-04-19", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-05-16", x1="2022-05-16", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-06-06", x1="2022-06-06", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-06-20", x1="2022-06-20", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-07-11", x1="2022-07-11", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-07-29", x1="2022-07-29", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-08-12", x1="2022-08-12", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-09-07", x1="2022-09-07", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-09-14", x1="2022-09-14", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-09-28", x1="2022-09-28", line_width=1, line_color="blue")
        fig.add_vline(x=1, x0="2022-10-02", x1="2022-10-02", line_width=1, line_color="blue")

        fig.update_layout(
        autosize=False,
        width=1920,
        height=1080)

        fig.update_layout(plot_bgcolor="white")

        st.plotly_chart(fig, use_container_width=True)
        dataframe_c = dataframe_c.copy()
        st.markdown("Total Major EP since last 2 years")
        st.dataframe(dataframe_c.style.background_gradient(cmap='Blues'))
        fig1 = px.bar(dataframe_c, x='Date', y='Magnitude', color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis,
                    title="EP | Hits Chart")
        st.plotly_chart(fig1, use_container_width=True)

        # Dataframe EP

    with Method:
        
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12=st.tabs(["NatSq", "Spiral", "TrTr", "TrNa", "addPrice", "Fib", "FutDates", "Mult", "Natal", "PriceTime", "Retro", "Sq9"])
        
        with o1:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m1.style.background_gradient(cmap='Blues'))
            with col2:
                fig1 = px.bar(m1, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="NatSq | Hits Chart")
                st.plotly_chart(fig1, use_container_width=True)

        with o2:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m2.style.background_gradient(cmap='Blues'))
            with col2:
                fig2 = px.bar(m2, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Spiral | Hits Chart")
                st.plotly_chart(fig2, use_container_width=True)

        with o3:
            col1, col2 = st.columns([1,2.9])

            with col1:
                st.dataframe(m3.style.background_gradient(cmap='Blues'))
            with col2:
                fig3 = px.bar(m3, x='Date', y='Hit',
                        title="TrTr | Hits Chart")
                st.plotly_chart(fig3, use_container_width=True)

        with o4:
            col1, col2 = st.columns([1,2.9])

            with col1:
                st.dataframe(m4.style.background_gradient(cmap='Blues'))
            with col2:
                fig4 = px.bar(m4, x='Date', y='Hit',
                        title="TrNa | Hits Chart")
                st.plotly_chart(fig4, use_container_width=True)

        with o5:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m5.style.background_gradient(cmap='Blues'))
            with col2:
                fig5 = px.bar(m5, x='Date', y='Hit', title="addPrice | Hits Chart")
                st.plotly_chart(fig5, use_container_width=True)

        with o6:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m6.style.background_gradient(cmap='Blues'))
            with col2:
                fig6 = px.bar(m6, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Fib | Hits Chart")
                st.plotly_chart(fig6, use_container_width=True)

        with o7:
            col1, col2 = st.columns([2,3.80])

            with col1:
                st.dataframe(m7.style.background_gradient(cmap='Blues'))
            with col2:
                fig7 = px.bar(m7, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="FutDates | Hits Chart")
                st.plotly_chart(fig7, use_container_width=True)

        with o8:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m8.style.background_gradient(cmap='Blues'))
            with col2:
                fig8 = px.bar(m8, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Mult | Hits Chart")
                st.plotly_chart(fig8, use_container_width=True)

        with o9:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m9.style.background_gradient(cmap='Blues'))
            with col2:
                fig9 = px.bar(m9, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Natal | Hits Chart")
                st.plotly_chart(fig9, use_container_width=True)

        with o10:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m10.style.background_gradient(cmap='Blues'))
            with col2:
                fig10 = px.bar(m10, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="PriceTime | Hits Chart")
                st.plotly_chart(fig10, use_container_width=True)

        with o11:
            col1, col2 = st.columns([1,2.8])

            with col1:
                st.dataframe(m11.style.background_gradient(cmap='Blues'))
            with col2:
                fig11 = px.bar(m11, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Retro | Hits Chart")
                st.plotly_chart(fig11, use_container_width=True)

        with o12:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m12.style.background_gradient(cmap='Blues'))
            with col2:
                fig12 = px.bar(m12, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Sq9 | Hits Chart")
                st.plotly_chart(fig12, use_container_width=True)

    col1, col2, col3 = st.columns([8, 7, 2])
    with col1:
        st.write(' ')
    with col2:
        authenticator.logout("Logout", "main")
    with col3:
        st.write(' ')