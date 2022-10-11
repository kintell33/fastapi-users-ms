from fastapi.testclient import TestClient
from main import app
from src.exceptions.duplicated_exception import DuplicatedException

client = TestClient(app)


def test_register():
    response = client.post(
        "/v1/register", json={"email": "user@email.com", "password": "1qaz2wsx", "nickname": "usernew"})
    assert response.status_code == 201
    assert response.json() == {
        "email": "user@email.com", "nickname": "usernew"}


def test_register_invalid_parameters():
    response = client.post(
        "/v1/register", json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "email"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": [
                    "body",
                    "password"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            },
            {
                "loc": [
                    "body",
                    "nickname"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_register_invalid_email():
    response = client.post(
        "/v1/register", json={"email": "useremail.com", "password": "1qaz2wsx", "nickname": "usernew"})
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': [
        'body', 'email'], 'msg': 'value is not a valid email address', 'type': 'value_error.email'}]}


def test_register_duplicated_user(mocker):
    mocker.patch("src.services.register_service.RegisterService.register", side_effect = DuplicatedException("duplicated user"))
    response = client.post(
        "/v1/register", json={"email": "user2@email.com", "password": "1qaz2wsx", "nickname": "usernew"})
    assert response.status_code == 400
    assert response.json() == {"status":"duplicated-error","message":"Resource not found"}

