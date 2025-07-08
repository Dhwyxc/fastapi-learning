import jwt
from decouple import config
import time

JWT_SECRET_KEY = config('JWT_SECRET_KEY')
JWT_ALGORITHM = config('JWT_ALGORITHM')


class AuthHandler(object):
    @staticmethod
    def sign_jwt(user_id: str) -> str:
        """Sign a JWT token with user ID."""
        payload = {
            'user_id': user_id,
            'exp': time.time() + 3600*24  # Token expires in 24 hour
        }
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    
    @staticmethod
    def decode_jwt(token: str) -> dict:
        """Decode a JWT token and return the payload if valid, or None if expired."""
        try:
            decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            return decoded if decoded["exp"] >= time.time() else None
        except:
            print("Invalid token")
            return None
        
