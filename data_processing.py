import pandas as pd
import chess.pgn
from io import StringIO

def parse_openings_from_pgn(pgn_data, openings_df):
    """
    Parses openings from PGN game data.

    Parameters:
    - pgn_data (str): PGN formatted game data.
    - openings_df (pd.DataFrame): DataFrame containing ECO to opening mappings.

    Returns:
    - dict: A dictionary with opening names as keys and counts as values.
    """
    openings_count = {}
    pgn_io = StringIO(pgn_data)

    while True:
        game = chess.pgn.read_game(pgn_io)
        if game is None:
            break

        opening_eco = game.headers.get("ECO", "")
        opening_name = openings_df[openings_df['ECO'] == opening_eco]['name'].values
        
        if opening_name.size > 0:
            opening_name = opening_name[0]
            openings_count[opening_name] = openings_count.get(opening_name, 0) + 1
                
    return openings_count
