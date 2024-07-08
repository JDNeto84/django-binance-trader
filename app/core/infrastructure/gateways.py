from binance.spot import Spot
from binance.error import ClientError, ServerError
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class BinanceGateway:
    def __init__(self, api_key, secret_key, base_url=None):
        if base_url:
            self.client = Spot(api_key=api_key, api_secret=secret_key, base_url=base_url)
        else:
            self.client = Spot(api_key=api_key, api_secret=secret_key)
        logger.info('Binance client initialized')

    def get_account_balances(self):
        try:
            account_info = self.client.account()
            logger.info('Account info retrieved successfully')
            return account_info['balances']
        except ClientError as e:
            logger.error(f"Client Error: {e}")
            raise Exception(f"Client Error: {e}")
        except ServerError as e:
            logger.error(f"Server Error: {e}")
            raise Exception(f"Server Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise Exception(f"Unexpected Error: {e}")

    def create_market_order(self, symbol, side, quantity):
        try:
            order = self.client.new_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            logger.info('Market order created successfully')
            return order
        except ClientError as e:
            logger.error(f"Client Error: {e}")
            raise Exception(f"Client Error: {e}")
        except ServerError as e:
            logger.error(f"Server Error: {e}")
            raise Exception(f"Server Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise Exception(f"Unexpected Error: {e}")
