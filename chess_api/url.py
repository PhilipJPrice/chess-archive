"""Url"""
class Url:
    """Returns chess.com API urls"""
    def __init__(self, username=""):
        self.base_url = "https://api.chess.com/pub/"
        self.get_player_profile = f"player/{username}"
        self.get_games = f"player/{username}/games"

    def get_player_profile_url(self):
        """Returns player profile url"""
        return self.base_url + self.get_player_profile

    def get_games_by_month(self, year="2000", month="01"):
        """Returns player games by month and year"""
        if year in (None, ""):
            print("Url.get_games_by_month(): The 'year' parameter is mising or undefined.")
        if month in (None, ""):
            print("Url.get_games_by_month(): The 'month' parameter is mising or undefined.")

        return f"{self.base_url}{self.get_games}/{year}/{month}"
