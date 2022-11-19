"""API"""
import requests

from .url import Url

class Api:
    """API wrapper class"""
    def __init__(self, username):
        self.url = Url(username=username)

    def get_player_profile(self):
        """Returns player profile json object"""
        response = requests.get(self.url.get_player_profile_url(), timeout=60)
        if response.status_code != 200:
            print("get_player_profile(): Response failed. Returning None.")
            return None
        return response.json()

    def get_games_by_month(self, year="", month=""):
        """Returns a pgn string for passed in year/month"""
        response = requests.get(self.url.get_games_by_month(year=year, month=month), timeout=60)
        if response.status_code != 200:
            print("get_games_by_month(): Response failed. Returning None.")
            return None
        return response.text
