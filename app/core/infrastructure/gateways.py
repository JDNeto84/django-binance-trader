from binance.spot import Spot
from core.domain.cryptography import decrypt

class BinanceGateway:
    def __init__(self, api_key, secret_key):
        self.client = Spot(api_key=api_key, api_secret=secret_key, base_url="https://testnet.binance.vision")

    def get_account_balances(self):
        account_info = self.client.account()
        return account_info['balances']

    def create_market_order(self, symbol, side, quantity):
        order = self.client.new_order(
            symbol=symbol,
            side=side.upper(),
            type="MARKET",
            quantity=quantity
        )
        return order

