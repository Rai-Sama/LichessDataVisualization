import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO

# Streamlit App
st.title("Lichess Player Analysis Dashboard")

username = st.text_input("Enter Lichess Username:")

if username:
    # Fetch player's games data and display slider to select number of games
    max_games = 60
    pgn_data = 5 # Lichess PGN games response
    if pgn_data:
        st.header("Select Number of Games to analyze")
        num_games = st.slider("Number of games", 0, max_games, 50)  # Default to 50 games

        # Display most played openings as a bar chart
        st.header(f"Most Played Openings in the last {num_games} games")
        st.write("<<Openings bar chart>>")
        
        # Game formats and variants to display -- standard lichess formats based on the docs
        game_formats = ['bullet', 'blitz', 'rapid', 'classical', 'correspondence', 
        'ultraBullet', 'crazyhouse', 'antichess', 
        'horde', 'chess960', 'kingOfTheHill', 'threeCheck', 'racingKings'
        ]

        for game_format in game_formats:
            st.header(f"{game_format.capitalize()} Games")
            st.write(f"<< Win/Loss ratio for {game_format.capitalize()} games. >>")
            st.write(f"<<Rating progression for {game_format.capitalize()} games >>")
