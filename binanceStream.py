
import websocket, json, pprint, numpy #, talib
import config
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05

closes = []
in_position = False

client = Client(config.API_KEY, config.API_SECRET, tld='us')

# def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
#     try:
#         print("sending order")
#         order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
#         print(order)
#     except Exception as e:
#         print("an exception occured - {}".format(e))
#         return False

#     return True

    
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    global closes, in_position
    
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)
    return

    # candle = json_message['k']

    # is_candle_closed = candle['x']
    # close = candle['c']

    # if is_candle_closed:
    #     print("candle closed at {}".format(close))
    #     closes.append(float(close))
    #     print("closes")
    #     print(closes)

    #     if len(closes) > RSI_PERIOD:
    #         np_closes = numpy.array(closes)
    #         rsi = talib.RSI(np_closes, RSI_PERIOD)
    #         print("all rsis calculated so far")
    #         print(rsi)
    #         last_rsi = rsi[-1]
    #         print("the current rsi is {}".format(last_rsi))

    #         if last_rsi > RSI_OVERBOUGHT:
    #             if in_position:
    #                 print("Overbought! Sell! Sell! Sell!")
    #                 # put binance sell logic here
    #                 order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
    #                 if order_succeeded:
    #                     in_position = False
    #             else:
    #                 print("It is overbought, but we don't own any. Nothing to do.")
            
    #         if last_rsi < RSI_OVERSOLD:
    #             if in_position:
    #                 print("It is oversold, but you already own it, nothing to do.")
    #             else:
    #                 print("Oversold! Buy! Buy! Buy!")
    #                 # put binance buy order logic here
    #                 order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
    #                 if order_succeeded:
    #                     in_position = True

                
# ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
# ws.run_forever()


for kline in client.get_historical_klines_generator("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"):
    print(kline)
    # do something with the kline

#SCHEMA:

kline =   [
    1499040000000,      # Open time
    "0.01634790",       # Open
    "0.80000000",       # High
    "0.01575800",       # Low
    "0.01577100",       # Close
    "148976.11427815",  # Volume
    1499644799999,      # Close time
    "2434.19055334",    # Quote asset volume
    308,                # Number of trades
    "1756.87402397",    # Taker buy base asset volume
    "28.46694368",      # Taker buy quote asset volume
    "17928899.62484339" # Ignore.
]

socketData = {'E': 1632150306372,
 'e': 'kline',
 'k': {'B': '0',
       'L': 606452010,
       'Q': '54395.49794500',
       'T': 1632150359999,
       'V': '17.82520000',
       'c': '3052.73000000',
       'f': 606451910,
       'h': '3053.17000000',
       'i': '1m',
       'l': '3049.78000000',
       'n': 101,
       'o': '3049.78000000',
       'q': '81361.20858900',
       's': 'ETHUSDT',
       't': 1632150300000,
       'v': '26.66220000',
       'x': False},
 's': 'ETHUSDT'}