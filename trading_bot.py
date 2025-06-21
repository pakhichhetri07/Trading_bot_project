from binance import Client
import logging
import argparse

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='trading_bot.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def validate_symbol(self, symbol):
        try:
            exchange_info = self.client.futures_exchange_info()
            symbols = [s['symbol'] for s in exchange_info['symbols']]
            if symbol not in symbols:
                raise ValueError(f"Invalid trading pair: {symbol}")
        except Exception as e:
            logging.error(f"Error validating symbol: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            print(f"Placing order: {order_type} {side} {quantity} at price {price} with stop price {stop_price}")

            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce='GTC'
                )
            elif order_type == 'STOP_MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP_MARKET',
                    quantity=quantity,
                    stopPrice=stop_price
                )
            elif order_type == 'STOP_LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='STOP_LIMIT',
                    quantity=quantity,
                    price=price,
                    stopPrice=stop_price,
                    timeInForce='GTC'
                )

            print(f"Order placed: {order}")  
            logging.info(f"Order placed: {order}")
            return order
        except Exception as e:
            print(f"Error placing order: {e}")  
            logging.error(f"Error placing order: {e}")
            return None

    def get_order_status(self, symbol, order_id):
        try:
            order = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            return order
        except Exception as e:
            logging.error(f"Error getting order status: {e}")
            return None

def main():
    parser = argparse.ArgumentParser(description='Trading Bot for Binance Futures Testnet')
    parser.add_argument('--api_key', required=True, help='API Key')
    parser.add_argument('--api_secret', required=True, help='API Secret')
    parser.add_argument('--symbol', required=True, help='Trading Pair (e.g., BTCUSDT)')
    parser.add_argument('--side', choices=['BUY', 'SELL'], help='Order Side')
    parser.add_argument('--type', choices=['MARKET', 'LIMIT', 'STOP_MARKET', 'STOP_LIMIT'], help='Order Type')
    parser.add_argument('--quantity', type=float, help='Order Quantity')
    parser.add_argument('--price', type=float, help='Order Price (for LIMIT and STOP_LIMIT orders)')
    parser.add_argument('--stop_price', type=float, help='Stop Price (for STOP_MARKET and STOP_LIMIT orders)')
    parser.add_argument('--check_order', type=int, help='Order ID to check status')

    args = parser.parse_args()

    bot = BasicBot(args.api_key, args.api_secret)

    # Validate the trading pair
    try:
        bot.validate_symbol(args.symbol)
    except ValueError as e:
        print(e)
        return

    if args.check_order is not None:
        order_status = bot.get_order_status(args.symbol, args.check_order)
        if order_status:
            print(f"Order status: {order_status}")
        return

    if args.type in ['STOP_LIMIT', 'STOP_MARKET'] and (args.stop_price is None):
        print("Stop price must be specified for STOP_LIMIT and STOP_MARKET orders.")
        return

    if args.type == 'LIMIT' and (args.price is None):
        print("Price must be specified for LIMIT orders.")
        return

    order = bot.place_order(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)
    if order:
        print(f"Order placed: {order}")

if __name__ == "__main__":
    main()
