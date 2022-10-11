from functools import wraps
from fastapi.responses import JSONResponse
from fastapi import status
from src.exceptions.duplicated_exception import DuplicatedException


class Api():
    def exception(f):
        @wraps(f)
        async def decorated_function(*args, **kwargs):
            try:
                return await f(*args, **kwargs)
            except DuplicatedException as error:
                return JSONResponse(content={"status": "duplicated-error", "message": "Resource not found"}, status_code=status.HTTP_400_BAD_REQUEST)
        return decorated_function