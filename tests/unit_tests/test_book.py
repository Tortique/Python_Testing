from flask import current_app, Flask
from tests.conftest import client


class TestBook:

    def test_book_more_places_than_points(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Spring Festival",
                                                        "club": "Test3", "places": "3"}, follow_redirects=True)
        data = response.data.decode()
        assert response.status_code == 200
        assert "Sorry, you didn&#39;t have enough points" in data
        assert "Points available: 2" in data
        assert "Number of Places: 25" in data

    def test_book_less_places_than_points(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Spring Festival",
                                                        "club": "Test3", "places": "1"}, follow_redirects=True)
        data = response.data.decode()
        assert "Points available: 1" in data
        assert "Number of Places: 24" in data
        assert "Great-booking complete!" in data

    def test_book_more_than_12_places(self, client):
        response = client.post("/purchasePlaces", data={"competition": "Spring Festival",
                                                        "club": "Test1", "places": "15"}, follow_redirects=True)
        data = response.data.decode()
        assert "You can&#39;t book more than 12 places in competition" in data
        assert "Points available: 20" in data
        assert "Number of Places: 24" in data

    def test_book_past_dated_competition(self, client):
        response = client.get("/book/Fall%20Classic/Test1")
        data = response.data.decode()
        assert "This competition is past-dated" in data
