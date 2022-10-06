from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register():
    response = client.post(
        "/v1/register", json={"email": "user@email.com", "password": "1qaz2wsx", "nickname": "usernew"})
    assert response.status_code == 201
    assert response.json() == {
        "email": "user@email.com", "nickname": "usernew"}


def test_register_invalid_email():
    response = client.post(
        "/v1/register", json={"email": "useremail.com", "password": "1qaz2wsx", "nickname": "usernew"})
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': [
        'body', 'email'], 'msg': 'value is not a valid email address', 'type': 'value_error.email'}]}

# def test_register_duplicated_user():
#     response = client.post(
#         "/v1/register", json={"email": "user2@email.com", "password": "1qaz2wsx", "nickname": "usernew"})
#     assert response.status_code == 400
#     assert response.json() == {"status":"duplicated-error","message":"The user already exist"}
