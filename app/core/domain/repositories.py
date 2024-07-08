from core.models import CustomUser
from core.domain.entities import User
from core.domain.cryptography import encrypt

class UserRepository:
    def get_user_by_username(self, username: str) -> User:
        try:
            user_model = CustomUser.objects.get(username=username)
            return User(
                username=user_model.username,
                password=user_model.password,
                email=user_model.email,
                _api_key=user_model.api_key,
                _secret_key=user_model.secret_key,
                is_active=user_model.is_active
            )
        except CustomUser.DoesNotExist:
            return None
    
    def create_user(self, username: str, password: str, email: str) -> User:
        user_model = CustomUser.objects.create_user(
            username=username, password=password, email=email
        )
        return User(
            username=user_model.username,
            password=user_model.password,
            email=user_model.email,
            _api_key='',  # Inicialmente vazio
            _secret_key='',  # Inicialmente vazio
            is_active=user_model.is_active
        )

    def update_api_key_and_secret(self, username: str, api_key: str, secret_key: str) -> User:
        try:
            user_model = CustomUser.objects.get(username=username)
            user_model.api_key = encrypt(api_key)
            user_model.secret_key = encrypt(secret_key)
            user_model.save()
            return User(
                username=user_model.username,
                password=user_model.password,
                email=user_model.email,
                _api_key=user_model.api_key,
                _secret_key=user_model.secret_key,
                is_active=user_model.is_active
            )
        except CustomUser.DoesNotExist:
            return None
