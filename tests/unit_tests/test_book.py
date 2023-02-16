from flask import current_app, Flask
from tests.conftest import client


class TestBook:

    def test_book_more_places_than_points(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Spring Festival",
                                                        "club": "Test3", "places": "3"}, follow_redirects=True)
        assert response.status_code == 200
        assert b'Sorry, you didn\'t have enough points' in response.data
        assert b'Points available: 2' in response.data
        assert b'Number of Places: 25' in response.data

    def test_book_less_places_than_points(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Spring Festival",
                                                        "club": "Test3", "places": "1"}, follow_redirects=True)
        expected = b'Great-booking complete!'
        assert b'Points available: 1' in response.data
        assert b'Number of Places: 24' in response.data
        assert expected in response.data

    def test_book_more_than_12_places(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Spring Festival",
                                                        "club": "Test1", "places": "15"}, follow_redirects=True)
        assert b'You can\'t book more than 12 places in competition' in response.data
        assert b'Points available: 20' in response.data
        assert b'Number of Places: 25' in response.data
