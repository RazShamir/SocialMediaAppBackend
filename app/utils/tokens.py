

from typing import Any
import jwt
import os

class Tokens:
    
    def encode(self, data: Any) -> str:
        secret = os.getenv("JWT_SECRET")
        return jwt.encode(data, secret, algorithm="HS256")

    def decode(self, token: str) -> Any:
        secret = os.getenv("JWT_SECRET")
        return jwt.decode(token, secret, algorithms=["HS256"]) 