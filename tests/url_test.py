import pytest
from chess_api.url import Url

def test_get_player_profile():
    """Unittest for get_player_profile function in Url class."""
    url = Url(username="test_username")
    assert url.get_player_profile_url() == f"{url.base_url}{url.get_player_profile}"

def test_get_games_by_month():
    """Unittest for get_games_by_month function in Url class."""
    url = Url(username="test_username")
    test_args = {'year':'2020', 'month': '02'}
    assert url.get_games_by_month() == f"{url.base_url}{url.get_games}/2000/01"
    assert url.get_games_by_month(**test_args) == f"{url.base_url}{url.get_games}/2020/02"
