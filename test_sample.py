import pytest

class TestClass:
    def test_login(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_home(self, client):
        response = client.get("/home")
        assert response.status_code == 200

    def test_registration(self, client):
        response = client.get("/registration")
        assert response.status_code == 200

    def test_newpost(self, client):
        response = client.get("/newpost")
        assert response.status_code == 200
