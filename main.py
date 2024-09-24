import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_fetching import fetch_games, fetch_user_stats, fetch_rating_history, load_openings
from data_processing import parse_openings_from_pgn

def main():
    # Load chess openings data
    openings_df = load_openings()

    # Streamlit App Title
    st.title("Lichess Player Analysis Dashboard")

    # User Input
    username = st.text_input("Enter Lichess Username:")

    if username:
        # Fetch player's PGN game data
        max_games = 60
        pgn_data = fetch_games(username, max_games)

        if pgn_data:
            st.header("Select Number of Games to analyze")
            num_games = st.slider("Number of games", 0, max_games, 50)

            # Parse openings from PGN data
            openings_count = parse_openings_from_pgn(pgn_data, openings_df)

            # Display most played openings
            st.header(f"Most Played Openings in the last {num_games} games")
            if openings_count:
                opening_df = pd.DataFrame(list(openings_count.items()), columns=['Opening', 'Count'])
                fig_openings = px.bar(opening_df.sort_values(by='Count', ascending=False), 
                                      x='Opening', y='Count', title="Most Played Openings")
                st.plotly_chart(fig_openings)
            else:
                st.write("No openings found.")

            # Fetch player rating history
            rating_history = fetch_rating_history(username)

            # Define game formats
            game_formats = ['bullet', 'blitz', 'rapid', 'classical', 'correspondence', 
                            'ultraBullet', 'crazyhouse', 'antichess', 
                            'horde', 'chess960', 'kingOfTheHill', 'threeCheck', 'racingKings']

            # Iterate over game formats to display stats
            for game_format in game_formats:
                st.header(f"{game_format.capitalize()} Games")
                stats = fetch_user_stats(username, game_format)

                if stats:
                    total_games = stats['count']['all']
                    wins = stats['count']['win']
                    losses = stats['count']['loss']
                    draws = stats['count']['draw']

                    win_loss_data = {'Win': wins, 'Loss': losses, 'Draw': draws}

                    # Pie chart for win/loss ratio
                    with st.expander(f"Win/Loss/Draw Ratio in {game_format.capitalize()}"):
                        fig_white = px.pie(values=win_loss_data.values(), names=win_loss_data.keys(), 
                                           title=f"Win/Loss/Draw Ratio in {game_format.capitalize()}", hole=0.4)
                        fig_white.update_traces(textinfo='percent+label')
                        st.plotly_chart(fig_white)

                    # Rating progression for the format/variant
                    # Rating progression for the format/variant
                    if rating_history:
                        for rating in rating_history:
                            if rating['name'] == game_format.capitalize() and rating['points']:
                                # Extract dates and ratings, ensuring dates are in proper date format
                                dates = [pd.to_datetime(f"{point[0]}-{point[1] + 1}-{point[2]}") for point in rating['points']]
                                ratings = [point[3] for point in rating['points']]
                                with st.expander(f"Rating Progression in {game_format.capitalize()}"):
                                    fig_rating = go.Figure(data=[go.Scatter(x=dates, y=ratings, mode='lines+markers')])
                                    fig_rating.update_layout(title=f"Rating Progression in {game_format.capitalize()}", 
                                                             xaxis_title='Date', yaxis_title='Rating')
                                    st.plotly_chart(fig_rating)
                    else:
                        st.write(f"No rating data available for {game_format.capitalize()}.")
                else:
                    st.write(f"Error fetching {game_format.capitalize()} statistics for {username}.")
        else:
            st.write(f"Error fetching games for {username}.")

if __name__ == "__main__":
    main()
