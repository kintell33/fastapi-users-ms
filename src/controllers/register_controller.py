from main import app
from src.models.user.user_register_model import UserRegister

API_VERSION='v1'

@app.post("/{}/register".format(API_VERSION), status_code=201)
async def register(user_register: UserRegister):
    return {"email": "user@email.com", "nickname": "usernew"}