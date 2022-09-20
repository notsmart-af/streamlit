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

    geo = geo.copy()
    geo = geo.iloc[::, geo.columns !='Date'].apply(np.floor)

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

    main,chart,Method = st.tabs(["Main", "Chart","Method"])

    with main:

        h1,h2,h3,h4=st.tabs(["Helio", "Geo", "Tools", "Sq9"])

        with h1:

            col0,col00 = st.columns([4,3])
            with col0:
                    st.dataframe(hm)
            with col00:
                    st.markdown("**Transit Aspects**")
                    st.dataframe(mn1.style.background_gradient(cmap='Blues'))
                    st.markdown("**Natal Aspects**")
                    st.dataframe(mn2.style.background_gradient(cmap='Blues'))

        with h2:

            col0,col00 = st.columns([6.618,3])
            with col0:
                st.dataframe(gm.style.background_gradient(cmap='Blues'))
            with col00:
                st.markdown("**Transit Aspects**")
                st.dataframe(mn3.style.background_gradient(cmap='Blues'))
                st.markdown("**Natal Aspects**")
                st.dataframe(mn4.style.background_gradient(cmap='Blues'))
        
        with h3:

            col5, col9 = st.columns([6,4])
            with col5:
                st.markdown("**Retro**")
                st.dataframe(mn6.style.background_gradient(cmap='Blues'))
            with col9:
                st.markdown("**Declination/Latitude**")
                st.dataframe(mn5.style.background_gradient(cmap='Blues'))

            st.markdown("**Moon/Node/Dec/Lat**")
            col7, col8 = st.columns([12,0.2])
            with col7:
                st.dataframe(mn7.style.background_gradient(cmap='Blues'))

        with h4:

            col0,col00 = st.columns([1,1])
            sq2 = Image.open(r'SQ2.png')

            with col0:
                #############################################################################

                # SPIRAL MATRIX ALGORITHM FOR SQUARE OF 9

                NORTH, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0) # directions
                turn_left = {S: E, W: S, NORTH: W, E: NORTH} # old -> new direction
                MASTER_WIDTH    = 19
                MASTER_HEIGHT   = 19

                #############################################################################

                # PLOT GANN SQUARE OF 9

                degrees = helio[helio.Date == today].values.tolist()[0]
                degrees.pop(0)
                planets = ["Ear", "Mer", "Ven", "Mar", "Jup", "Sat", "Ura", "Nep", "Plu"]
                planet_hash = dict(zip(degrees, planets))

                matrix = [[307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325],[306,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,326],
                [305,240,183,184,185,186,187,188,189,190,191,192,193,194,195,196, 197,258,327],[304,239,182,133,134,135,136,137,138,139,140,141,142,143,144,145,198,259,328],[303,238,181,132,91,92,93,94,95,96,97,98,99,100,101,146,199,260,329],
                [302,237,180,131,90,57,58,59,60,61,62,63,64,65,102,147,200,261,330],[301,236,179,130,89,56,31,32,33,34,35,36,37,66,103,148,201,262,331],[300,235,178,129,88,55,30,13,14,15,16,17,38,67,104,149,202,263,332],
                [299,234,177,128,87,54,29,12,3,4,5,18,39,68,105,150,203,264,333],[298,233,176,127,86,53,28,11,2,1,6,19,40,69,106,151,204,265,334],[297,232,175,126,85,52,27,10,9,8,7,20,41,70,107,152,205,266,335],
                [296,231,174,125,84,51,26,25,24,23,22,21,42,71,108,153,206,267,336],[295,230,173,124,83,50,49,48,47,46,45,44,43,72,109,154,207,268,337],[294,229,172,123,82,81,80,79,78,77,76,75,74,73,110,155,208,269,338],
                [293,228,171,122,121,120,119,118,117,116,115,114,113,112,111,156,209,270,339],[292,227,170,169,168,167,166,165,164,163,162,161,160,159,158,157,210,271,340],[291,226,225,224,223,222,221,220,219,218,217,216,215,214,213,212,211,272,341],
                [290,289,288,287,286,285,284,283,282,281,280,279,278,277,276,275,274,273,342],[361,360,359,358,357,356,355,354,353,352,351,350,349,348,347,346,345,344,343]]
                new_matrix = []

                for row in matrix:
                    x = []
                    for i, degree in enumerate(row):
                        if i < len(row):
                            x.append(planet_hash[degree]) if degree in planet_hash.keys() else x.append(degree)
                    return new_matrix.append(x)

                out_mat = new_matrix

                cell_text = []
                cell_colours = []
                for i in range(MASTER_HEIGHT):
                    cell_text.append([])
                    cell_colours.append([])
                    for j in range(MASTER_WIDTH):
                        cell_text[i].append(str(out_mat[i][j]))
                        if  i == j \
                            or i == (18-j) \
                            or j == (MASTER_WIDTH // 2) \
                            or i == (MASTER_HEIGHT // 2):
                            cell_colours[i].append("yellow")
                        else:
                            cell_colours[i].append("none")

                fig, ax = plt.subplots()
                fig.set_size_inches(12, 12, forward=True)

                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axes.spines["left"].set_color(None)
                ax.axes.spines["right"].set_color(None)
                ax.axes.spines["top"].set_color(None)
                ax.axes.spines["bottom"].set_color(None)
                ax.set_aspect("equal")

                table = plt.table(cellText=cell_text, cellColours=cell_colours, cellLoc="center", bbox=[0, 0, 1, 1])

                for k, v in table._cells.items():
                    v.set_edgecolor((0.7, 0.7, 0.7))

                for i in range(10):
                    ax.add_patch(Rect((2-0.1*i, 2-0.1*i), 0.2*i, 0.2*i, facecolor="none", edgecolor="black", lw=1.5))
                st.pyplot(fig)               

            with col00:
                st.image(sq2)
                st.markdown("Here is an aerial view of the **Khufru pyramid in Egypt**, some claim that the ancient builders bequeathed these pyramids to us as an *astro-calculator*, which **W.D Gann** calls the ***Square of 9***. It has been discovered that each **45°** row of this pyramid (**8 sides**) has a **small inclination**, was this intentional to reveal the importance of the **45° degree**? Or as they call it, an architectural coincidence...")
                st.markdown("**Helio** in Purple")
                st.dataframe(helio)
                st.markdown("**Geo** in Blue")
                st.dataframe(geo) 

    with chart:
        figui = px.bar(m, x="Date", y="EP", hover_data=['Date', 'EP'], color='EP', color_continuous_scale=px.colors.sequential.Cividis,
             height=618).update_layout(xaxis={"rangeslider":{"visible":True}})
        st.plotly_chart(figui, use_container_width=True)
        st.markdown("**Energy Points (EP) Hits on BTC chart last 2 years**")        
        st.image(epp)

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