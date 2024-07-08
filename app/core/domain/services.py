from django.contrib.auth import authenticate, login, logout
from core.domain.cryptography import decrypt
from core.infrastructure.gateways import BinanceGateway
from core.domain.repositories import UserRepository
from core.domain.entities import User

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
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_balances(self, username: str):
        user = self.user_repository.get_user_by_username(username)
        if user:
            api_key = decrypt(user._api_key)
            secret_key = decrypt(user._secret_key)
            binance_gateway = BinanceGateway(api_key, secret_key, base_url="https://testnet.binance.vision")
            return binance_gateway.get_account_balances()
        else:
            raise Exception("User not found")

    def create_market_order(self, username: str, symbol: str, side: str, quantity: float):
        user = self.user_repository.get_user_by_username(username)
        if user:
            api_key = decrypt(user._api_key)
            secret_key = decrypt(user._secret_key)
            binance_gateway = BinanceGateway(api_key, secret_key, base_url="https://testnet.binance.vision")
            return binance_gateway.create_market_order(symbol, side, quantity)
        else:
            raise Exception("User not found")