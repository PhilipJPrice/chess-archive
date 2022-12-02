"""
app.py
"""
import os, os.path
import datetime
from pathlib import Path
from config import Config
from chess_api.api import Api

def generate_archive():
    """generates an archive folder containing pgn files of player game history by year and month"""
    api = Api(username=Config.USERNAME)

    player_profile_obj = api.get_player_profile()
    joined_timestamp = player_profile_obj['joined']
    joined_datetime = datetime.datetime.utcfromtimestamp(joined_timestamp)
    year_start = joined_datetime.year
    year_end = datetime.datetime.today().year

    for year in range(year_start, year_end+1):
        data_folder = Path(Config.OUTPUT_PATH + str(year))
        for i in range(1, 13):
            month = str(i).zfill(2)
            games = api.get_games_by_month(year=year, month=month)
            file_path = data_folder / f'/{month}.pgn'
            with open(file_path, 'w+', encoding='utf-8') as f:
                f.write(games)
                f.close()

if __name__ == '__main__':
    generate_archive()
