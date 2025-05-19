from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_and_hello():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Welcome to the API"}

    res = client.get("/hello")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello World"}

def test_register_and_duplicate_user():
    res = client.post("/auth/register", json={"username": "charlie", "password": "pass123"})
    assert res.status_code == 200
    assert "id" in res.json()

    res = client.post("/auth/register", json={"username": "charlie", "password": "pass123"})
    assert res.status_code == 400
    assert res.json()["detail"] == "Username already registered"

def test_login_with_correct_and_wrong_credentials():
    res = client.post("/auth/token", data={"username": "charlie", "password": "pass123"})
    assert res.status_code == 200
    token = res.json()["access_token"]
    assert token is not None

    res = client.post("/auth/token", data={"username": "charlie", "password": "wrongpass"})
    assert res.status_code == 400
    assert res.json()["detail"] == "Incorrect username or password"

def test_protected_endpoints_with_token():
    # Login
    res = client.post("/auth/token", data={"username": "charlie", "password": "pass123"})
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Crear item
    item = {"name": "Monitor", "price": 189.99, "in_stock": True}
    res = client.post("/items/", json=item, headers=headers)
    assert res.status_code == 200
    created = res.json()
    assert created["name"] == "Monitor"
    assert created["price"] == 189.99
    assert created["in_stock"] is True

    # Listar items
    res = client.get("/items/", headers=headers)
    assert res.status_code == 200
    items = res.json()
    assert isinstance(items, list)
    assert any(i["name"] == "Monitor" for i in items)

def test_protected_endpoints_without_token():
    item = {"name": "ShouldFail", "price": 0.0, "in_stock": False}
    res = client.post("/items/", json=item)
    assert res.status_code == 401

    res = client.get("/items/")
    assert res.status_code == 401
