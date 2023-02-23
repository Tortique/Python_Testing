import pytest

import server
from server import app, clubs, competitions


@pytest.fixture
def client():
    app.config.from_object({"TESTING": True})
    with app.test_client() as client:
        yield client


server.clubs = [
    {"name": "Test1", "email": "test1@test.com", "points": "20"},
    {"name": "Test2", "email": "test2@test.com", "points": "0"},
    {"name": "Test3", "email": "test3@test.com", "points": "2"},
    {"name": "Test4", "email": "test4@test.com", "points": "4"},
    {"name": "Test5", "email": "test5@test.com", "points": "3"},
]

server.competitions = [
    {
        "name": "Spring Festival",
        "date": "2023-03-27 10:00:00",
        "numberOfPlaces": "25"
    },
    {
        "name": "Fall Classic",
        "date": "2020-10-22 13:30:00",
        "numberOfPlaces": "13"
    }
]

server.booking = {
    "Test1": {"Spring Festival": 0, "Fall Classic": 0},
    "Test2": {"Spring Festival": 0, "Fall Classic": 0},
    "Test3": {"Spring Festival": 0, "Fall Classic": 0},
    "Test4": {"Spring Festival": 0, "Fall Classic": 0},
    "Test5": {"Spring Festival": 0, "Fall Classic": 0}
}
