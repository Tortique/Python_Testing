from flask import current_app, Flask
from tests.conftest import client


class TestRecap:

    def test_show_points_recap(self, client):
        response = client.get("/pointsRecap")
        data = response.data.decode()
        print(data)
        assert response.status_code == 200
        assert "Test1 : 20" in data
        assert "Test2 : 0" in data
        assert "Test3 : 1" in data
        assert "Test4 : 4" in data
        assert "Test5 : 3" in data
