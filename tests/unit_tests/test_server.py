from flask import current_app, Flask
from tests.conftest import client


class TestServer:

    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_home_page(self, client):
        response = client.get("/")
        expected = b"Welcome to the GUDLFT Registration Portal!"
        assert expected in response.data
