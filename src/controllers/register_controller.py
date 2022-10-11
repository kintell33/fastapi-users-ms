from main import app
from src.models.user.user_register_model import UserRegister
from src.services.register_service import RegisterService
from fastapi import Response, status
from src.decorators.api_base import Api as api

API_VERSION='v1'

@app.post("/{}/register".format(API_VERSION), status_code=201)
@api.exception
async def register(user_register: UserRegister, response: Response):
    service = RegisterService()
    service_response = service.register()
    return {"email": "user@email.com", "nickname": "usernew"}