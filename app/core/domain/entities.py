from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str
    email: str
    is_active: bool