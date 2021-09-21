import flask 
from flask import request, jsonify
import ccxt
import config
from binance.client import Client

#from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS, cross_origin


binanceClient = Client(config.API_KEY, config.API_SECRET)#, tld='us')

#binanceClient.API_URL = 'https://api.binance.com/api/v3' 
#binanceClient.API_URL = 'https://api.binance.com/api/v3' 

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
#csrf = CSRFProtect(app)

dataTest = {
    'this':12,
    'that':'abc',
}


@app.route('/', methods=['GET'])
def home():
    return jsonify(dataTest)
    #return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/exchanges', methods=['GET'])
def exchanges():
    return jsonify(ccxt.exchanges)

@app.route('/exchange_info', methods=['GET'])
def exchangeInfo():
    info = binanceClient.get_exchange_info()   
    return jsonify(info)


@app.route('/prices', methods=['GET'])
def prices():
    prices = binanceClient.get_all_tickers()
    return jsonify(prices)

# @app.route('/symbol', methods=['GET'])
# def get_symbols(symbol):
#     info = binanceClient.get_symbol_info(symbol)
#     return jsonify(info)

@app.route('/symbol', methods=['GET'])
def get_symbols():
    info = binanceClient.get_symbol_info("")


@app.route('/symbol/<symbol>', methods=['GET'])
def get_symbol(symbol):
    #query_parameters = request.args

    #symbol = query_parameters.get('symbol')
    print("got sym:", symbol)
    #prices = binanceClient.get_all_tickers()
    #info = client.get_symbol_info('BNBBTC')
    # if(symbol == ""):
    #     info = binanceClient.get_symbol_info()
    # else:
    info = binanceClient.get_symbol_info(symbol)
    #info = binanceClient.get_all_coins_info()#timestamp=1632155002006)
    #info = binanceClient.get_all_tickers()
    return jsonify(info)

@app.route('/coins', methods=['GET', 'POST'])
#@csrf.exempt
def get_coins():
    #query_parameters = request.args

    #symbol = query_parameters.get('symbol')
    print("got coins req")
    #prices = binanceClient.get_all_tickers()
    #info = client.get_symbol_info('BNBBTC')
    #info = binanceClient.get_symbol_info(symbol)
    info = binanceClient.get_all_coins_info()#timestamp=1632155002006)
    #info = binanceClient.get_all_tickers()

    # response = flask.jsonify({'some': 'data'})
    # response.headers.add('Access-Control-Allow-Origin', '*')


    return jsonify(info)

@app.route('/pairs', methods=['GET'])
#@csrf.exempt
def get_pairs():

    margin_pairs = binanceClient.get_margin_all_pairs()#timestamp=1632155002006)
    return jsonify(margin_pairs)





app.run()