# Libraries

import pandas as pd 
import plotly.express as px
import numpy as np
from datetime import date
from datetime import datetime
from datetime import timedelta
from deta import Deta
import matplotlib.pyplot as plt
import streamlit_authenticator as stauth
import streamlit.components.v1 as components
import streamlit as st
import database as db
from PIL import Image
import plotly.graph_objects as go
import os
import gettext
_ = gettext.gettext


st.set_page_config(page_title="ASTROTOOL©", layout="wide")

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

logo = Image.open(r'images//logo.png')

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

    st.markdown(_(f"Welcome aboard **{names}**, enjoy the Alpha version of **AstroTool©**"))
        
    # LOGO

    heliox = heliox.copy()
    geox = geox.copy()
    geo = geo.copy()
    hm = helio_main.copy()
    gm = geo_main.copy()
    m = fluchart.copy()
    chart = dataframe_c.copy()
    gdeg = final_sentiment.copy()
    gdeg = gdeg.iloc[: , 1:]

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

    info, help, main, chart, Sentimental, Method = st.tabs(["Introduction", "Help", "Main", "Chart", "Sentiment Analysis", "Method"])

    with info:

        col0,col00 = st.columns([5,3.5])

        with col0:
            st.title('AstroTool© Info Page')
                
            gt = Image.open(r'images//gtlogo.png')

            st.markdown(_('''
            **This WebApp of Astrotool©** is a gift from **[Geometric Thinking](https://geometricthinking.com "Geometric Thinking")** and the developers **Amir & Sachith** to the world.  We have learned that there is a **unique way** to *read price charts* for geometric support and resistance.  **AND** we have found that there are ways to project, **far in advance, the dates when pivot turns are likely to occur in the market**. We call those dates **ENERGY POINTS (EPs)**.  This WebApp will highlight future EPS for you.  *It will not tell you which way a market will break*, but **it will give you a upindication when to pay close attention to a chart for price volatility**.
            * The **MAIN** page is absolutely full of key astrological data related to key dates in BTC history, all neatly summarized in an easy-to-read table. The dates are easily found on the left side of the table and the aspects on the right. The data on the Main page, will give you insight into the types of date we research for this WebApp. For a more thorough and complete understanding, we encourage all users to attend a class, if and when Geometric Thinking holds another class. As of the date of publication, the last date entered was 06/18/22.
            * The **CHART** page is self-explanatory. The dates with the highest bars are the dates to watch the most. Note that the EP dates should be viewed as +/- 1 day. In other words, an EP may show up a day before or a day after the highlighted date.
            The founder of Geometric Thinking (GT) has been involved in the market for a very long time and will not be available to teach for more than a few more years. This WebApp is given to help GT students by giving away some of the insights we PRAYED for, when we were starting out. We wish you the very best success in your trading career! 
            **We wish you the very best success in your trading career**.
            '''))
            st.header(_('Who are we?'))

            st.image(gt)
                
            st.markdown(_('''
            We opened Geometric Thinking in July 2017 and have now taught literally hundreds of traders worldwide the art of Geometric Thinking.  

            * Geometric Thinking focuses on a unique understanding of how geometry and natural law focuses the minds of traders (en masse) such that **there are points in time and price where we can forecast trend changes are most likely to occur.**

            * Knowing in advance, for example, that a coin like BTC will likely reach an Energy Point (EP) in time 2 weeks in advance gives the trader almost an “unfair advantage” over other traders. It becomes advantageous for the Geometric Thinker to realize that a projected date 2 weeks in advance is a prime time to observe and plan for, but also analyze the “forecast-able” prices associated with that date.
            
            * If you’ve been trading for a while, you already know that this business is cut-throat. It is vicious and even very smart people typically lose everything over time. If you are honest with yourself, you know that **the classic trading techniques, divergences, moving averages, etc. simply do not work consistently.**

            * Therefore, what does work consistently? What will give you an unfair advantage over other traders? **Geometry and natural law.**

            * Having this powerful knowledge will not guarantee that you will win, it gives you an cutting-edge advantage. Look at the picture above of the man holding two aces in the hole. Does this guarantee that he will win the hand? **No. There are still 100 ways to lose, even with a pair of aces in the hole**. If he were playing against other professional poker players he would still need to master the game right? He would still need to hide his tells, learn to bluff, learn game mathematics, etc., to be a consistent winner. The same applies to Geometric Thinking and trading.

            * Now, imagine what Geometric Thinking can do for you. I can give you two Aces on nearly every hand without cheating! **That is a CUTTING-EDGE ADVANTAGE, right?** AstroTool and Geometric Thinking can arrange for you to be dealt two aces in the hole more often than not. If you will combine that with the dedication to master this business, you can become a consistent winner. **We believe this 100%.**
            '''))
                
            st.header(_('Why is this important?'))
            st.markdown(_('''
            Whether you care to believe this or not, dates such as the 12/17/2017 (20k top) or the 15/04/2021 (65k) BTC top were seen weeks in advance as a date for a possible top. The 3/12/2020 low was also forecasted as a possible low well more than a month in advance. **WE LITERALLY [TWEETED TO THE WORLD](https://twitter.com/jimfred1276/status/1462641460948267013), THAT THE NOV 2021 TOP WAS IN, A WEEK OR SO AFTER THE FACT, WHEN PRICE WAS STILL ~ 65000!** To the best of our knowledge, we are the only ones who did that.

            Whether you choose to believe this or not, We assure you it is true that at the very least, **several hundred geometric thinking traders know which dates to watch, and which prices, LONG before other traders do.** 
            
            **Does that seem important to you? Does that matter? Should you care? We think so.**

            You can join us in our [Telegram Channel](https://t.me/joinchat/FKSNuqrZpjhlZTJi)
            '''))

        with col00:
            spa = Image.open(r'images//space.png')
            st.image(spa, caption='The Solar System - "Spirals Everywhere" | A Little Book of Coincidence by John Martineau')
            astrotoologo = Image.open(r'images//astro.png')
            sva = Image.open(r'images//sva.png')
            st.image(sva, caption='Amir & Sachith logo')
            st.markdown(_('*About the developers...*'))
            st.markdown(_('''This fully implemented Web-App, ready to use in Python, was created as part of a **Memory Paper** for **[DU Data Analytics @ University Pantheon Sorbonne Paris](https://formations.pantheonsorbonne.fr/fr/catalogue-des-formations/diplome-d-universite-DU/diplome-d-universite-KBVXM363/diplome-d-universite-sorbonne-data-analytics-KPMK3V7Z.html)**. The two developers and students are **[Amir Lehmam](https://fr.linkedin.com/in/amirlehmam)** & **[Sachith Galbokka](https://fr.linkedin.com/in/sachith-galbokka-b22187204)**. Both being passionate about blockchain and programming since they met each others in 2016', they linked their passion with their interest to create this web-app. This was made possible only by our mentor **[Jim Fredrickson](https://geometricthinking.com/about-us/)** - *creator of GeometricThinking.com & AstroTool©* - who allowed us to translate "Astrotool©" into Python from his excel sheet which he has been working on since 1991'... We also want to thanks **[Marc Arthure DIAYE](http://marc-arthur.diaye.monsite-orange.fr/)** - *director of the DU Data Analytics at Pantheon Sorbonne* - for allowing us AstroTool© as a memory paper subject!

            The developers take no credit for the basic calculations and methods of the "Astrotool©" algorithm --- It is a complete property of our mentor Jim Fredrickson --- Our job was to translate the entire "Astrotool" algorithm into Python in order to make it competitive and up to date. The creation of the Web-App is a major asset for the ease of use of such an algorithm, it was a necessary step for the progress of such a project! A lot of work has been done (about 3 months of intense coding during the summer of 2022...), but the biggest part is still to come! The AstroTool Team has many upcoming ingenious ideas and we will bring astrotool to a level never seen before! Enjoy the Alpha...'''
            ))

    with help:
        
        ee1,ee2=st.tabs(["Intro", "User Guide"])

        with ee1:
            col1, col2, col3 = st.columns([2, 3, 2])

            with col1:
                st.write(' ')
                

            with col2:
                st.title(_("**AstroTool© Help Page**"))
                st.markdown(_('''GeometricThinking is of the opinion that it is FAR better to be **focus on time** as a factor in trading, than to first focus on price. However, forecasting time is much trickier than forecasting price. There are literally **hundreds of hidden variables** that we were never even taught to consider.'''))
                
                st.markdown(_('''AstroTool© was developed to solve a significant problem for forecasters who are employing natural law (astrology, arithmetic, geometry and universal principles of growth). There are so many factors to consider that it quickly becomes impossible for a serious forecaster to keep a handle on the hundreds of variables that are at work. We found ourselves missing market turns that we had ourselves forecasted in the past, because we got lost in the minutiae of forecasting, along with simply losing track of where we were in real-time. AstroTool has solved this problem.'''))
                
                st.markdown(_('''Following up on the success of AstroTool© v5.3 (*which was made available on this website to the public for free*), v6.0 has been completed. It offers several improvements over v5.3 and is now the tool of choice for those who have access to it.'''))
                
                st.markdown(_('''Our intention is to make v6.0 available to the public for a short window of time, as we move toward putting the key charts and output on our website. **AstroTool’s output will be put behind a paywall at some point in the future**. Those who have taken the time to research the accuracy of Astrotool v5.3 as a forecasting tool have found it to be on the order of **80% accurate in forecasting market turns**. These forecasts are often made months in advance. We invite others to do their own research to see if this statement is self-serving bluster, or is in fact the Truth. **We are confident in what you will find.**'''))
                
                st.markdown(_('''The key component of AstroTool is the chart of forecasted **Energy Points (eps)**. These are the days that have a higher-than-average likelihood of being dates of market turns. In some cases, those dates present themselves as eps immediately, with sharp turns (long green or red candles) on or about the day in question. But in many cases there is an extended period of time that elapses before it becomes clear that a major pivot has been formed. Here are two such examples:'''))
            
            with col3:
                st.write(' ')
    
            col1, col2, col3 = st.columns([0.2,5,0.2])

            with col1:
                st.write('')
                
            with col2:
                sp = Image.open(r'images//piv.png')
                st.image(sp)
            with col3:
                st.write('')


            col1, col2, col3 = st.columns([2, 3, 2])

            with col1:
                st.write(' ')

            with col2:
                st.title(_("Chart"))
                st.markdown(_('As mentioned above, the key component of Astrotool is the chart of forecasted EP dates in the months ahead. We use it with the understanding that it is accurate **+/- 1 day**. In other words, if a date like 4/10/2021 is forecasted, then we know to be alert from 4/9-4/11/2021. Here is an example of the chart:'))

            with col3:
                st.write(' ')
            
            col1, col2, col3 = st.columns([0.5,5,0.5])

            with col1:
                st.write('')
            with col2:
                figui = px.bar(m.head(36).iloc[5:,], x="Date", y="Magnitude", hover_data=['Date', 'Magnitude'], color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis,
                    height=700, width=1200).update_layout(xaxis={"rangeslider":{"visible":True}})
                st.plotly_chart(figui, use_container_width=True)
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])

            with col1:
                st.write(' ')

            with col2:
                st.title(_("Sq9"))
                st.markdown(_("As you can see, 10/3/2022 is being highlighted as a date to watch. There are many other visual aids as well. For example, here is a chart that shows the placement of each of the planets longitude, updated daily, superimposed upon the Gann Square of Nine chart (Sq9). **It was this visual that alerted us in advance to the likelihood of the 4/14/2021 high being a significant EP and turned out to be the 65k BTC Top we all aware of.**"))
                st.markdown(_("Below here's a plot of the **4/14/2021** Sq9 visualization.. We can clearly see **6 planets** ([Jup_G], [Ear_H], [Mer_G], [Ura_H], [Mer_H], [Mar_H]) that are in this 'yellow' area. This yellow zone is separated into 8 lines, all 45 degrees apart. **The more planets in this zone, the more important the date in question will be perceived as a pivot!**"))
            with col3:
                st.write(' ')

            col1, col2, col3 = st.columns([1,5,1])

            with col1:
                st.write('')
            with col2:
                sp = Image.open(r'images//sqhelp.png')
                st.image(sp)
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])

            with col1:
                st.write(' ')

            with col2:
                st.title(_("Main Page"))
                st.markdown(_("If you study the data on the Main page, you will gain insight into the things we search. At first sight it might looks difficult to understand, but it's not! **Let's unpack it!**"))
                st.markdown(_("The first two rows correspond to the actual transit of the planets. Their current degrees are displayed in the first row.  In the second row the name of the current house of the planet is given as well as its number of degrees in this house. This data is updated automatically every day by our algorithm."))
                st.markdown(_("The third and fourth rows correspond to the cumulative degrees since the date indicated. The third row contains the cumulative number of degrees, and the fourth row contains the number of revolutions followed by the number of degrees remaining before the next revolution."))
                st.markdown(_("Apart from the first 2 rows, the rest of the rows are based on the cumulative degrees since the major key date or pivot date... You can find the date and the related data information of '31/10/2008' which is the BTC White Paper or '01/03/2009', the genesis-block day also major TOPS such as '17/12/2017' (20k) or '11/10/2021' (69k) are also in the table..."))
                st.markdown(_("**The purpose of this 'Main' table was to have a record & calculation of all our important dates and key information in relation to our solar system planets.** It is very useful for advanced users in astro-trading! It is a must-have!"))
                def highlight_everyother(s):
                    return ['background-color: yellow; color:black' if x%2==1 else ''
                        for x in range(len(s))]
                st.dataframe(hm.head(6).style.apply(highlight_everyother))           

            with col3:
                st.write(' ')

        with ee2:
            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**AstroTool© User Guide**'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**Main**'))
                def highlight_everyother(s):
                    return ['background-color: yellow; color:black' if x%2==1 else ''
                        for x in range(len(s))]
                st.dataframe(hm.style.apply(highlight_everyother))   
                st.markdown(_('This section shows the current helio longitude of each planet on the 2nd line, which gives “Today date” on the far left. It is followed by “mod 30”. This line shows the current number of degrees into the current house. In the example above, the earth has moved into Aries…'))
                st.markdown(_('Each of the following lines beginning with “White Paper date”, shows how far each planet has moved since a key date in BTC history. Since the White Paper was published on 10/31/2008, the earth has moved 5002 degrees. '))
                st.markdown(_('The line following (mod360) shows us that the earth has moved 13 full cycles (13 earth years), and is 322 degrees into the 14th cycle, since WP date.'))
                st.markdown(_('Note that the Nep column has a highlighted ‘30’ on the Genesis block date. 30 degrees is a key degree so it is highlighted to stand out (of course Neptune moves very slowly, and may remain at 30 degrees for a month, so it is only useful when in tandem with other more immediate signals).'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**Chart**'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([0.5,5,0.5])

            with col1:
                st.write('')
            with col2:
                figui = px.bar(m.head(66).iloc[5:,], x="Date", y="Magnitude", hover_data=['Date', 'Magnitude'], color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis)
                st.plotly_chart(figui, use_container_width=True)
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write('')
            with col2:
                st.markdown(_('This is perhaps the most important visual in AstroTool. It shows at a glance the dates ahead in which there is a forecast of a likely change in trend. It is calculated by the aggregation of a large number of classical and esoteric timing signals employed by traders worldwide.'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**Longitudes on Square of 9**'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([1,5,1])    

            with col1:
                st.write('')
            with col2:
                sp = Image.open(r'images//sq9.png')
                st.image(sp)
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])       

            with col1:
                st.write('')
            with col2:
                original_titles = '**<p style="font-family:sans-serif; color:Red; font-size: 20px;">**Heliocentric (H)**</p>**'
                st.markdown(original_titles, unsafe_allow_html=True)
                for col in helio.columns[1:]:
                    helio = helio.astype({col: int})
                st.dataframe(helio)
                original_titles = '**<p style="font-family:sans-serif; color:Aqua; font-size: 20px;">**Geocentric (G)**</p>**'
                st.markdown(original_titles, unsafe_allow_html=True)
                for col in geo.columns[1:]:
                    geo = geo.astype({col: int})
                st.dataframe(geo)  
            with col3:
                st.write('')                  

            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write('')
            with col2:
                st.markdown(_('This visual shows the Helio longitude of each of the planets in red, and the Geo longitude in blue. The longitudes are overlaid on Gann’s Square of 9 chart.'))
                st.markdown(_('It has been our experience that on days when most planets, either in Helio or Geo, are on one of the 45 degrees lines, “the cross” (shown in yellow), a change in trend is likely. This tool alerted us to the 4/14/2021 high being a major pivot, in advance. '))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**Aspects**'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])    

            with col1:
                st.write('')
            with col2:
                st.markdown(_("**Transit Aspects**"))
                for col in mn1.columns[3:]:
                    mn1 = mn1.astype({col: int})
                st.dataframe(mn1.style.background_gradient(cmap='Blues'))
                st.markdown(_("**Natal Aspects**"))
                for col in mn2.columns[3:]:
                    mn2 = mn2.astype({col: int})
                st.dataframe(mn2.style.background_gradient(cmap='Blues'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write('')
            with col2:
                st.markdown(_('Here we see today’s planetary aspects. The key degrees to look for are highlighted in yellow. For example, in the example above, Earth & Mercury are in conjunction, and Pluto and Mercury are 60 degrees apart.'))
                st.markdown(_('The blue are is for those rare times when today’s planets are making an important aspect with BTC’s natal chart. For example, if today’s Saturn longitude was 60 degrees with where Jupiter was on the White Paper date, it would show up here.'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**Retrograde activity**'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])    

            with col1:
                st.write('')
            with col2:
                st.dataframe(mn6.style.background_gradient(cmap='Blues'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write('')
            with col2:
                st.markdown(_('This visual shows us the planet’s retrograde status over the next 10 days. Here we can see that 6 of the 8 planets are retrograde today.'))
                st.markdown(_('Importantly, we can see that Mercury will be no longer retrograde (will go direct) on 10/2/2022. You may see an “X” in one of the squares (occasionally not shown here). That would indicate that the planet had returned to its prior longitude from which it’s last retrograde has begun.'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])
            with col1:
                st.write('')
            with col2:
                st.title(_('**Progression from all Pivots**'))
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2,3,2])    

            with col1:
                st.write('')
            with col2:
                mn99 = helhelp.copy()
                st.dataframe(mn99)
            with col3:
                st.write('')

            col1, col2, col3 = st.columns([2, 3, 2])
            with col1:
                st.write('')
            with col2:
                st.markdown(_('This last section is rather like the very first section. It notes how many degrees each planet has moved since a key pivot date. Important degrees are highlighted in yellow for quick reference. Note that is TOTAL degrees moved, which can get to be pretty big number for fast-moving planets like Mercury. You will note that sometimes an odd-looking number like ‘1890’ will be highlighted. In such a case, the number is 90, 180 or 270 degrees from a full planetary cycle. It is not necessary to do the calculation. Astrotool has already done the calculation and highlighted the cell for you.'))
                st.markdown(_('***We wish you the best in your trading career and believe that this tool will be of tremendous help, once you learn how to use it on a daily basis. Happy trading!***'))
            with col3:
                st.write('')

        #figui = px.bar(mm, x="Date", y="Magnitude", hover_data=['Date', 'Magnitude'], color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis,
        #    height=550)
        #st.plotly_chart(figui, use_container_width=True)

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
                    st.markdown(_("**Transit Aspects**"))
                    for col in mn1.columns[3:]:
                        mn1 = mn1.astype({col: int})
                    st.dataframe(mn1.style.background_gradient(cmap='Blues'))
                    st.markdown(_("**Natal Aspects**"))
                    for col in mn2.columns[3:]:
                        mn2 = mn2.astype({col: int})
                    st.dataframe(mn2.style.background_gradient(cmap='Blues'))
                    st.markdown("7 = 7.5° & 22 = 22.5°")

        with h2:

            col0,col00 = st.columns([6.618,3])
            with col0:
                    def highlight_everyother(s):
                        return ['background-color: orange; color:black' if x%2==1 else ''
                            for x in range(len(s))]
                    st.dataframe(gm.style.apply(highlight_everyother))
            with col00:
                st.markdown(_("**Transit Aspects**"))
                for col in mn3.columns[3:]:
                    mn3 = mn3.astype({col: int})
                st.dataframe(mn3.style.background_gradient(cmap='Blues'))
                st.markdown(_("**Natal Aspects**"))
                for col in mn4.columns[3:]:
                    mn4 = mn4.astype({col: int})
                st.dataframe(mn4.style.background_gradient(cmap='Blues'))
                st.markdown("7 = 7.5° & 22 = 22.5°")
        
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
            sq1 = Image.open(r'images//sq9.png')
            sq2 = Image.open(r'images//SQ2.png')

            with col0:
                st.image(sq1)

            with col00:
                st.image(sq2)
                st.markdown(_("Here is an aerial view of the **Khufru pyramid in Egypt**, some claim that the ancient builders bequeathed these pyramids to us as an *astro-calculator*, which **W.D Gann** calls the ***Square of 9***. It has been discovered that each **45°** row of this pyramid (**8 sides**) has a **small inclination**, was this intentional to reveal the importance of the **45° degree**? Or as they call it, an architectural coincidence..."))
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
        st.title(_('**Energy Points Chart (next 3 months)**'))
        figui = px.bar(m.head(96).iloc[5:,], x="Date", y="Magnitude", hover_data=['Date', 'Magnitude'], color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis,
            height=618).update_layout(xaxis={"rangeslider":{"visible":True}})
        st.plotly_chart(figui, use_container_width=True)
        st.markdown(_('**Energy Points Hits on BTC @ last 2 years**'))
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
        ###### 
        col1, col2 = st.columns([1,3.33])

        with col1:
            dataframe_c = dataframe_c.copy()
            st.markdown(_("Total Major EP since last 2 years"))
            st.dataframe(dataframe_c.style.background_gradient(cmap='Blues'))
        with col2:
            fig1 = px.bar(dataframe_c, x='Date', y='Magnitude', color='Magnitude', color_continuous_scale=px.colors.sequential.Cividis,
                        title="EP hits since last 2 years")
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

    with Sentimental:

        e1,e2=st.tabs(["Dashboard", "Chart"])

        with e1:

            col1, col2, col3 = st.columns([5,3,5])
            with col1:
                st.title(_('**Twitter Sentimental Analysis on BTC**'))
                st.markdown(_('Cryptocurrencies are rising in importance as an investment option and alternative currency. Thus, investors are keen on finding timely market movement insights. One of such sources is Twitter due to its live feed of information on cryptocurrencies and emotional information from investors expressing their sentiments.'))
                st.markdown(_('This page will examine the extent to which Twitter sentiments can be used to correlate human mass-psychology and our major EP days date… This study was conducted using a snscrape for Twitter scrapping, a “pipeline_nlp” in order to clean our samples, and a lexicon-based approach through the VADER algorithm for sentiment analysis.'))
                st.markdown(_('This study has been made on 13 different MAJOR EP dates, we took for each of them, -1/+1 days from the given date (eg: our major EP is at 15/09/2022, we scrapped from Twitter 83k tweets from these 3 consecutive dates: 14/09 | 15/09 | 16/09). The total scrapped sample represent more than 850k tweets for those 13 major EP.'))
            with col2:
                
                #def highlight_everyother(s):
                #    return ['background-color: grey; color:black' if x%6 in range(3, 7) else ''
                #        for x in range(len(s))]
                #st.dataframe(gdeg.style.apply(highlight_everyother))
                gggg = ['Positive', 'Strongly Positive', "Weakly Positive"]
                def highlight(x):
                    return ['background-color:green' if x in gggg else 'background-color:darkred' for x in gdeg.Sentiment]

                st.dataframe(gdeg.style.apply(highlight))

            with col3:
                sss = Image.open(r'images//wc1.png')
                st.image(sss, width=500, caption='WordCloud of our scrapped Tweets (#bitcoin)')

            fig = px.line(gdeg, x="Date", y="Sentiment", color='Sentiment', title="Sentiments grouped by Dates", width=1618, height=500, symbol="Sentiment")
            fig.update_layout(xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False))
            st.plotly_chart(fig)

            col0,col00 = st.columns([3,3])
            with col0:
                fig = px.pie(gdeg, values='compound', names='Sentiment', width=600, height=500, title="Percentage distribution of each sentiment")
                st.plotly_chart(fig)

            with col00:
                fig1 = px.pie(gdeg, values='compound', names='Date', width=600, height=500, title="Percentage distribution of each sentiment by dates")
                st.plotly_chart(fig1)

        with e2:
            fig = px.bar(gdeg, x='Date', y='Sentiment', color="compound", title="Sentiment compound over time", color_continuous_scale=px.colors.sequential.Cividis, width=1618, height=618)
            st.plotly_chart(fig)

            df = btcusd_d.copy()

            fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close'])])
            fig.add_vline(x=1, x0="2020-12-17", x1="2020-12-19", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-01-20", x1="2021-01-22", line_width=4, line_color="firebrick")
            fig.add_vline(x=1, x0="2021-04-14", x1="2021-04-16", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-05-18", x1="2021-05-19", line_width=4, line_color="green")
            fig.add_vline(x=1, x0="2021-07-01", x1="2021-07-03", line_width=4, line_color="green")      
            fig.add_vline(x=1, x0="2021-07-17", x1="2021-07-19", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-07-31", x1="2021-08-02", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-08-31", x1="2021-09-02", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-09-23", x1="2021-09-25", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-10-09", x1="2021-10-11", line_width=4, line_color="lime")              
            fig.add_vline(x=1, x0="2021-11-09", x1="2021-11-11", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2021-12-09", x1="2021-12-11", line_width=4, line_color="lime")
            fig.add_vline(x=1, x0="2022-01-24", x1="2022-01-26", line_width=4, line_color="red")
            fig.add_vline(x=1, x0="2022-04-04", x1="2022-04-06", line_width=4, line_color="green")
            fig.add_vline(x=1, x0="2022-06-04", x1="2022-06-06", line_width=4, line_color="green")
            fig.add_vline(x=1, x0="2022-06-19", x1="2022-06-21", line_width=4, line_color="firebrick")
            fig.add_vline(x=1, x0="2022-07-03", x1="2022-07-05", line_width=4, line_color="green")
            fig.add_vline(x=1, x0="2022-07-12", x1="2022-07-15", line_width=4, line_color="firebrick")
            fig.add_vline(x=1, x0="2022-09-13", x1="2022-09-15", line_width=4, line_color="firebrick")

            fig.update_layout(
            autosize=False,
            width=1920,
            height=1080)

            fig.update_layout(plot_bgcolor="white")

            st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns([8, 7, 2])
    with col1:
        st.write(' ')
    with col2:
        authenticator.logout("Logout", "main")
    with col3:
        st.write(' ')