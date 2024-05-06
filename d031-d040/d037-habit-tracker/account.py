class Account:
    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token

    def as_dict(self) -> dict:
        return {
            'NAME': self.username,
            'TOKEN': self.token
        }
