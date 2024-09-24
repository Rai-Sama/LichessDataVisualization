import requests
import pandas as pd
import chess.pgn
from io import StringIO

def fetch_games(username, num_games = 500):
    """
    Fetches PGN games for a given Lichess username.

    Parameters:
    - username (str): Lichess username to fetch games for.
    - num_games (int): Maximum number of games to fetch (default is 500).

    Returns:
    - str: PGN formatted games or None if an error occurred.
    """
    url = f'https://lichess.org/api/games/user/{username}?max={num_games}'
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

def fetch_user_stats(username, game_format):
    """
    Fetches user statistics for a specific game format.

    Parameters:
    - username (str): Lichess username to fetch stats for.
    - game_format (str): The game format to fetch statistics for.

    Returns:
    - dict: Statistics JSON data or None if an error occurred.
    """
    url = f'https://lichess.org/api/user/{username}/perf/{game_format}'
    response = requests.get(url)
    return response.json().get("stat") if response.status_code == 200 else None

def fetch_rating_history(username):
    """
    Fetches rating history for a given Lichess username.

    Parameters:
    - username (str): Lichess username to fetch rating history for.

    Returns:
    - dict: Rating history JSON data or None if an error occurred.
    """
    url = f'https://lichess.org/api/user/{username}/rating-history'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def load_openings(file_path = 'chess_openings.csv'):
    """
    Loads chess openings from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file containing ECO mappings.

    Returns:
    - pd.DataFrame: DataFrame containing ECO and opening names.
    """
    openings = pd.read_csv(file_path)
    openings = openings[openings['ECO'] != openings['name']]
    return openings.drop_duplicates(subset='ECO', keep='first')
