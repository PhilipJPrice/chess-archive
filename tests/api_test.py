"""Api Test"""
import pytest

from chess_api.api import Api

@pytest.fixture
def api_fixture():
    """Pytest fixture returning Api object"""
    api = Api(username="test_username")
    return api

def test_get_player_profile(mocker, api_fixture):
    """Unittest for get_player_profile function in Api class."""
    mock_valid_response = mocker.MagicMock(status_code=200)
    mock_valid_response.json.return_value = {}
    mock_invalid_response = mocker.MagicMock(status_code=500)

    # test valid response
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = mock_valid_response
    assert api_fixture.get_player_profile() == {}

    # # test invalid response
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = mock_invalid_response
    assert api_fixture.get_player_profile() is None

def test_get_games_by_month(mocker, api_fixture):
    """Unittest for get_games_by_month function in Api class."""

    mock_valid_response = mocker.MagicMock(status_code=200, text="1. d4")
    mock_invalid_response = mocker.MagicMock(status_code=500)

    # test valid response
    requests_mock = mocker.patch('requests.get')
    requests_mock.return_value = mock_valid_response
    assert api_fixture.get_games_by_month() == "1. d4"

    # test invalid response
    requests_mock.return_value = mock_invalid_response
    assert api_fixture.get_games_by_month() is None
