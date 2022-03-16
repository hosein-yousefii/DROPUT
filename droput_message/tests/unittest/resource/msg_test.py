import pytest
import json, requests
from droput_msg.config import Config


@pytest.mark.parametrize(
    ("status", "code"),
    [
        (200, 100)
    ]
)
def test_get_msgs(client, status, code):
    result = client.get("/api/v1/msgs")
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code

@pytest.mark.parametrize(
    ("user_id", "status", "code"),
    [
        ("notfound", 404, 103)
    ]
)
def test_get_msg(client, user_id, status, code):
    result = client.get(f"/api/v1/msgs/{user_id}")
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code

@pytest.mark.parametrize(
    ("status", "code"),
    [
        (201, 100)
    ]
)
def test_add_msg(client,status,code):
    global msg_id
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype
    }

    data = {
        "sender":Config.TEST_USER,
        "receiver":Config.TEST_USER,
        "content":"content test"
    }

    result = client.post("/api/v1/msgs", data=json.dumps(data), headers=headers)
    response_data = result.get_json()
    msg_id = response_data["msg"]["id"]
    assert result.content_type == mimetype
    assert result.status_code == status
    assert response_data["code"] == code

@pytest.mark.parametrize(
    ("status", "code"),
    [
        (201, 100)
    ]
)
def test_del_msg(client,status,code):
    result = client.delete(f"/api/v1/msgs/{msg_id}")
    response_data = result.get_json()
    assert result.status_code == status
    assert response_data["code"] == code


def test_get_test_user_id():
    global user_id
    url = Config.USER_AUTH_URL + "/api/v1/users"
    response = requests.get(url=url)
    data = response.json()

    for i in range(0, len(data["users"])):
        if Config.TEST_USER == data["users"][i]["username"]:
            user_id = data["users"][i]["id"]
            break



@pytest.mark.parametrize(
    ("status", "code"),
    [
        (201, 100)
    ]
)
def test_del_test_user(client,status,code):

    url = Config.USER_AUTH_URL + f"/api/v1/users/{user_id}"
    result = requests.delete(url=url)
    response_data = result.json()
    assert result.status_code == status
    assert response_data["code"] == code















