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

            col0,col00 = st.columns([6,4])
            with col0:
                from datetime import datetime
                today = datetime.strftime(datetime.now(), "%d/%m/%Y")

                cumulative_1 = helio_cum.copy()
                cumulative_2 = helio_cum.copy()
                cumulative_3 = helio_cum.copy()
                cumulative_4 = helio_cum.copy()
                cumulative_5 = helio_cum.copy()
                cumulative_6 = helio_cum.copy()
                cumulative_7 = helio_cum.copy()
                cumulative_8 = helio_cum.copy()
                cumulative_9 = helio_cum.copy()
                cumulative_10 = helio_cum.copy()
                cumulative_11 = helio_cum.copy()
                cumulative_12 = helio_cum.copy()
                cumulative_13 = helio_cum.copy()

                helio = helio.copy()
                test = helio_cum.copy()

                def cum_hel(df, date):
                    today = datetime.strftime(datetime.now(), "%d/%m/%Y")
                    return pd.DataFrame(
                        {
                            "Date": [date],
                            "Earth": df["Earth"][df.Date == today].values
                            - df["Earth"][df.Date == date].values,
                            "Mer": df["Mer"][df.Date == today].values
                            - df["Mer"][df.Date == date].values,
                            "Ven": df["Ven"][df.Date == today].values
                            - df["Ven"][df.Date == date].values,
                            "Mar": df["Mar"][df.Date == today].values
                            - df["Mar"][df.Date == date].values,
                            "Jup": df["Jup"][df.Date == today].values
                            - df["Jup"][df.Date == date].values,
                            "Sat": df["Sat"][df.Date == today].values
                            - df["Sat"][df.Date == date].values,
                            "Ura": df["Ura"][df.Date == today].values
                            - df["Ura"][df.Date == date].values,
                            "Nep": df["Nep"][df.Date == today].values
                            - df["Nep"][df.Date == date].values,
                            "Plu": df["Plu"][df.Date == today].values
                            - df["Plu"][df.Date == date].values,
                        }
                    )

                filtered_dfs = []

                data = [
                (cumulative_1, '31/10/2008'),
                (cumulative_2, '03/01/2009'),
                (cumulative_3, '22/05/2010'),
                (cumulative_4, '29/11/2013'),
                (cumulative_5, '17/12/2017'),
                (cumulative_6, '15/12/2018'),
                (cumulative_7, '26/06/2019'),
                (cumulative_8, '12/03/2020'),
                (cumulative_9, '25/04/2021'),
                (cumulative_10, '20/07/2021'),
                (cumulative_11, '20/10/2021'),
                (cumulative_12, '10/11/2021'),
                (cumulative_13, '18/06/2022'),
                ]

                for i, (df, date) in enumerate(data):
                    filtered_dfs.append(cum_hel(df, date))
                    
                result = helio[helio.Date == today]
                cumm_hel = pd.concat(filtered_dfs)
                hel = pd.concat([result, cumm_hel])
                hel = hel.round()

                # mod30 (donne qu'elle signe il est)

                mod = pd.DataFrame({'Date': [today],

                                                    'Earth': helio['Earth'][helio.Date == today].values
                                                    % 30,

                                                    'Mer': helio['Mer'][helio.Date == today].values
                                                    % 30,
                                                    
                                                    'Ven': helio['Ven'][helio.Date == today].values
                                                    % 30,

                                                    'Mar': helio['Mar'][helio.Date == today].values
                                                    % 30,

                                                    'Jup': helio['Jup'][helio.Date == today].values
                                                    % 30,
                                                    
                                                    'Sat': helio['Sat'][helio.Date == today].values
                                                    % 30,

                                                    'Ura': helio['Ura'][helio.Date == today].values
                                                    % 30,

                                                    'Nep': helio['Nep'][helio.Date == today].values
                                                    % 30,
                                                    
                                                    'Plu': helio['Plu'][helio.Date == today].values
                                                    % 30,

                                                    })


                mod = mod.round()


                mod0 = mod.round()

                # BON CUM MOD/REV

                hexx = hel.copy()

                hexx['Earth'] = hexx['Earth'] / 360
                hexx['Mer'] = hexx['Mer'] / 360
                hexx['Ven'] = hexx['Ven'] / 360
                hexx['Mar'] = hexx['Mar'] / 360
                hexx['Jup'] = hexx['Jup'] / 360
                hexx['Sat'] = hexx['Sat'] / 360
                hexx['Nep'] = hexx['Nep'] / 360
                hexx['Plu'] = hexx['Plu'] / 360

                hecc = hel.copy()

                hecc['Earth'] = hecc['Earth'] % 360
                hecc['Mer'] = hecc['Mer'] % 360
                hecc['Ven'] = hecc['Ven'] % 360
                hecc['Mar'] = hecc['Mar'] % 360
                hecc['Jup'] = hecc['Jup'] % 360
                hecc['Sat'] = hecc['Sat'] % 360
                hecc['Nep'] = hecc['Nep'] % 360
                hecc['Plu'] = hecc['Plu'] % 360

                hexx = hexx.iloc[1: , :]
                hecc = hecc.iloc[1:, :]

                # ROUNDDOWN

                hexx = hexx.iloc[::, hexx.columns !='Date'].apply(np.floor)
                hecc = hecc.iloc[::, hecc.columns !='Date'].apply(np.floor)

                # STR

                for col in hexx.columns[::]:
                    hexx = hexx.astype({col: str})

                for col in hecc.columns[::]:
                    hecc = hecc.astype({col: str})

                puant = pd.DataFrame({"Date": cumm_hel['Date']})

                # GROUPBY MANUALY

                for col in hexx.columns[::]:
                    puant[col] = hexx[col] + ' | ' + hecc[col] #.groupby('Date').agg('-'.join).reset_index()
                    
                helio_concat = pd.concat([cumm_hel, puant], axis=0)
                helio_concat.Date = pd.to_datetime(helio_concat.Date)
                helio_concat = helio_concat.sort_values("Date", ignore_index=True)
                helio_concat.Date = helio_concat.Date.dt.strftime("%d/%m/%Y")

                hcc = pd.concat([result, mod0, helio_concat])
                st.dataframe(hcc)
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
                NORTH, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0) # directions
                turn_left = {S: E, W: S, NORTH: W, E: NORTH} # old -> new direction
                MASTER_WIDTH    = 19
                MASTER_HEIGHT   = 19

                def spiral(width, height):
                    if width < 1 or height < 1:
                        raise ValueError
                    x, y = width // 2, height // 2 # start near the center
                    dx, dy = NORTH # initial direction
                    matrix = [[None] * width for _ in range(height)]
                    count = 0
                    while True:
                        count += 1
                        matrix[y][x] = count # visit
                        # try to turn right
                        new_dx, new_dy = turn_left[dx,dy]
                        new_x, new_y = x + new_dx, y + new_dy
                        if (0 <= new_x < width and 0 <= new_y < height and
                            matrix[new_y][new_x] is None): # can turn right
                            x, y = new_x, new_y
                            dx, dy = new_dx, new_dy
                        else: # try to move straight
                            x, y = x + dx, y + dy
                            if not (0 <= x < width and 0 <= y < height):
                                return matrix # nowhere to go

                def print_matrix(matrix):
                    width = len(str(max(el for row in matrix for el in row if el is not None)))
                    fmt = "{:0%dd}" % width
                    for row in matrix:
                        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))

                my_matrix = spiral(MASTER_WIDTH, MASTER_HEIGHT)

                # PLOT GANN SQUARE OF 9

                out_mat = my_matrix

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
                fig.set_size_inches(3.5, 3.5, forward=True)

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