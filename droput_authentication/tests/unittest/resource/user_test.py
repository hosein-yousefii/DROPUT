import pytest
import json
from droput_auth.config import Config

@pytest.mark.parametrize(
    ("status", "code"),
    [
        (200, 100)
    ]
)
def test_get_users(client, status, code):
    result = client.get("/api/v1/users")
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code

@pytest.mark.parametrize(
    ("user_id", "status", "code"),
    [
        ("not found", 404, 103)
    ]
)
def test_get_user(client, user_id, status, code):
    result = client.get(f"/api/v1/users/{user_id}")
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code

@pytest.mark.parametrize(
    ("status", "code"),
    [
        (201, 100)
    ]
)
def test_add_user(client,status,code):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }

    data = {
        "username":Config.TEST_USER,
        "password":"test"
    }

    result = client.post("/api/v1/users", data=json.dumps(data), headers=headers)
    response_data = result.get_json()
    assert result.content_type == mimetype
    assert result.status_code == status
    assert response_data["code"] == code




