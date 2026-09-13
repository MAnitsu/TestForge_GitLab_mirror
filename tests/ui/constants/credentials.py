# constants/credentials.py
import os
from dotenv import load_dotenv

load_dotenv()


class LoginConfig:
    _USERS = {
        "valid_credentials": {
            "username": os.getenv("VALID_USER", "tomsmith"),
            "password": os.getenv("VALID_PASS", "SuperSecretPassword!"),
        },
        "invalid_credentials": {
            "username": os.getenv("INVALID_USER", "wronguser"),
            "password": os.getenv("INVALID_PASS", "wrongpassword"),
        },
    }

    @classmethod
    def get_user(cls, role):
        return cls._USERS.get(role)
