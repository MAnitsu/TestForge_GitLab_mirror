# constants/credentials.py

class LoginConfig:
    __USERS = {
        "valid_credentials": {"username": "tomsmith", "password": "SuperSecretPassword!"},
        "invalid_credentials": {"username": "wronguser", "password": "wrongpassword"}
    }

    @classmethod
    def get_user(cls, role):
        return cls.__USERS.get(role)
