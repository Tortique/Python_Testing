from flask import current_app, Flask
from tests.conftest import client


class TestConnection:

    def test_known_email(self, client):
        response = client.post("/showSummary", data={"email": "test1@test.com"}, follow_redirects=True)
        assert response.status_code == 200
        assert b'test1@test.com' in response.data

    def test_unknown_email(self, client):
        response = client.post("/showSummary", data={"email": "testunknown@test.com"}, follow_redirects=True)
        expected = b'<p>Sorry, that email wasn\'t found.</p>'
        assert expected in response.data
