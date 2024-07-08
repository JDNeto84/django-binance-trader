import logging
from django.contrib.auth import authenticate, login, logout
from core.domain.cryptography import decrypt
from core.infrastructure.gateways import BinanceGateway
from core.domain.repositories import UserRepository
from core.domain.entities import User

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login_user(self, request, username: str, password: str) -> bool:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return True
        return False
    
    def logout_user(self, request):
        logout(request)
    
    def register_user(self, username: str, password: str, email: str) -> User:
        return self.user_repository.create_user(username, password, email)
    
    def update_user_keys(self, username: str, api_key: str, secret_key: str) -> bool:
        user = self.user_repository.update_api_key_and_secret(username, api_key, secret_key)
        return user is not None

class BinanceService:
    def __init__(self, user_repository: UserRepository, base_url=None):
        self.user_repository = user_repository
        self.base_url = base_url

    def get_user_balances(self, username: str):
        user = self.user_repository.get_user_by_username(username)
        if user:
            if not user._api_key or not user._secret_key:
                raise Exception("API key or secret key is missing for user.")
                
            api_key = decrypt(user._api_key)
            secret_key = decrypt(user._secret_key)
            if not api_key or not secret_key:
                raise Exception("Decryption failed. API key or secret key is None.")
                
            # logger.info(f'Decrypted API Key: {api_key}')
            # logger.info(f'Decrypted Secret Key: {secret_key}')
            binance_gateway = BinanceGateway(api_key, secret_key, base_url=self.base_url)
            return binance_gateway.get_account_balances()
        else:
            raise Exception("User not found")

    def create_market_order(self, username: str, symbol: str, side: str, quantity: float):
        user = self.user_repository.get_user_by_username(username)
        if user:
            if not user._api_key or not user._secret_key:
                raise Exception("API key or secret key is missing for user.")
                
            api_key = decrypt(user._api_key)
            secret_key = decrypt(user._secret_key)
            if not api_key or not secret_key:
                raise Exception("Decryption failed. API key or secret key is None.")
                
            # logger.info(f'Decrypted API Key: {api_key}')
            # logger.info(f'Decrypted Secret Key: {secret_key}')
            binance_gateway = BinanceGateway(api_key, secret_key, base_url=self.base_url)
            return binance_gateway.create_market_order(symbol, side, quantity)
        else:
            raise Exception("User not found")