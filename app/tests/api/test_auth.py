from fastapi.testclient import TestClient
from app.core.config import settings

def test_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Enterprise FastAPI"}

# This test requires a user to be in the database, 
# for a full enterprise setup we would use factory_boy or similar to setup data
# def test_login(client: TestClient) -> None:
#     login_data = {
#         "username": "test@example.com",
#         "password": "password",
#     }
#     r = client.post(f"{settings.API_V1_STR}/auth/login/access-token", data=login_data)
#     tokens = r.json()
#     assert r.status_code == 200
#     assert "access_token" in tokens
