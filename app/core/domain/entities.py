from dataclasses import dataclass, field
from core.domain.cryptography import encrypt, decrypt

@dataclass
class User:
    username: str
    password: str
    email: str
    _api_key: str = field(repr=False)
    _secret_key: str = field(repr=False)
    is_active: bool

    @property
    def api_key(self):
        return decrypt(self._api_key)

    @api_key.setter
    def api_key(self, value):
        self._api_key = encrypt(value)

    @property
    def secret_key(self):
        return decrypt(self._secret_key)

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = encrypt(value)
