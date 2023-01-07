# 请求：
#获取最近7天的价格变化情况：
# http://47.242.55.109:2023/agent/?url=https://www.binance.com/api/v3/ticker%3Fsymbols%3D[%22BTCUSDT%22,%22ETHUSDT%22,%22ETHBTC%22]%26windowSize%3D7d
#获取最近1天的价格变化情况：
# http://47.242.55.109:2023/agent/?url=https://www.binance.com/api/v3/ticker%3Fsymbols%3D[%22BTCUSDT%22,%22ETHUSDT%22,%22ETHBTC%22]%26windowSize%3D1d

# 以上两个接口的响应格式相同：
# "[{\"symbol\":\"ETHBTC\",\"priceChange\":\"0.00250700\",\"priceChangePercent\":\"3.474\",\"weightedAvgPrice\":\"0.07361632\",\"openPrice\":\"0.07217000\",\"highPrice\":\"0.07542900\",\"lowPrice\":\"0.07199500\",\"lastPrice\":\"0.07467700\",\"volume\":\"389006.09210000\",\"quoteVolume\":\"28637.19682309\",\"openTime\":1672467900000,\"closeTime\":1673072744904,\"firstId\":395706414,\"lastId\":396358174,\"count\":651761},{\"symbol\":\"BTCUSDT\",\"priceChange\":\"383.21000000\",\"priceChangePercent\":\"2.316\",\"weightedAvgPrice\":\"16752.09198491\",\"openPrice\":\"16547.97000000\",\"highPrice\":\"17041.00000000\",\"lowPrice\":\"16470.00000000\",\"lastPrice\":\"16931.18000000\",\"volume\":\"1086134.99203000\",\"quoteVolume\":\"18195033294.51799530\",\"openTime\":1672467900000,\"closeTime\":1673072744904,\"firstId\":2405655771,\"lastId\":2437969453,\"count\":32313683},{\"symbol\":\"ETHUSDT\",\"priceChange\":\"70.09000000\",\"priceChangePercent\":\"5.869\",\"weightedAvgPrice\":\"1235.29591865\",\"openPrice\":\"1194.20000000\",\"highPrice\":\"1276.70000000\",\"lowPrice\":\"1190.57000000\",\"lastPrice\":\"1264.29000000\",\"volume\":\"1796737.22010000\",\"quoteVolume\":\"2219502154.88380700\",\"openTime\":1672467900000,\"closeTime\":1673072744904,\"firstId\":1049368581,\"lastId\":1051805387,\"count\":2436807}]"

# 说明：
# 该接口返回的是一个数组，数组中的每个元素是一个对象，
# 对象中的symbol属性是交易对，priceChange属性是价格变化，
# priceChangePercent属性是价格变化百分比，
# weightedAvgPrice属性是加权平均价格，
# openPrice属性是开盘价，highPrice属性是最高价，
# lowPrice属性是最低价，lastPrice属性是最新价，volume属性是成交量，
# quoteVolume属性是成交额，openTime属性是开盘时间，closeTime属性是收盘时间，
# firstId属性是第一笔成交ID，lastId属性是最后一笔成交ID，count属性是成交笔数。

import requests
import json

top100_symbols = [
"BTCUSDT",
"BTCBUSD",
"BUSDUSDT",
"ETHUSDT",
"ETHBUSD",
"XRPUSDT",
"ETHBTC",
"GALAUSDT",
"TRXUSDT",
"BNBBUSD",
"SOLUSDT",
"DOGEUSDT",
"BNBUSDT",
"ETCUSDT",
"LTCUSDT",
"GALABUSD",
"SOLBUSD",
"USDTTRY",
"MATICUSDT",
"ADAUSDT",
"SANDUSDT",
"XRPBUSD",
"OPUSDT",
"SHIBUSDT",
"LDOUSDT",
"LUNCBUSD",
"APTUSDT",
"DOGEBUSD",
"BTCEUR",
"NEARUSDT",
"FETUSDT",
"GALATRY",
"TRXBUSD",
"LTCBUSD",
"LINKUSDT",
"ATOMUSDT",
"BUSDTRY",
"FTMUSDT",
"LDOBUSD",
"ETCBUSD",
"ADABUSD",
"JASMYUSDT",
"FETBUSD",
"ETHEUR",
"SHIBBUSD",
"MATICBUSD",
"AVAXUSDT",
"DOTUSDT",
"APTBUSD",
"XMRUSDT",
"MASKUSDT",
"BTCTRY",
"BTCAUD",
"FILUSDT",
"BTCGBP",
"OPBUSD",
"LUNCUSDT",
"AGIXBUSD",
"APEUSDT",
"USDTBRL",
"MANAUSDT",
"AXSUSDT",
"SUSHIUSDT",
"JASMYBUSD",
"OCEANUSDT",
"DYDXUSDT",
"TWTUSDT",
"CHZUSDT",
"NEARBUSD",
"BNXUSDT",
"HOOKUSDT",
"CTXCUSDT",
"JASMYTRY",
"FIDABUSD",
"BNBBTC",
"SANDBUSD",
"ALGOUSDT",
"LINKBUSD",
"GMTUSDT",
"BCHUSDT",
"SOLBTC",
"VIDTBUSD",
"BTCBRL",
"VIDTUSDT",
"HOOKBUSD",
"RLCUSDT",
"AVAXBUSD",
"SOLTRY",
"LTCBTC",
"FIDAUSDT",
"SRMBUSD",
"USDTBIDR",
"UNIUSDT",
"WBTCBTC",
"DASHUSDT",
"AUDIOUSDT",
"TWTBUSD",
"OCEANBUSD",
"APEBUSD",
"ICPUSDT"
]

def escape_url(url):
    #对url中的?、=、\、&执行转义
    url = url.replace('?', '%3F').replace('=', '%3D').replace('/', '%2F').replace('&', '%26')
    return url

def request_binance(url):
    #对url中的?、=、\、&执行转义
    url = escape_url(url)
    #请求代理服务器
    agent_url = 'http://47.242.55.109:2023/agent/?url=' + url
    resp = requests.get(agent_url)
    if resp.status_code != 200:
        return None
    return json.loads(json.loads(resp.text))

def get_binance_ticker(interval="1d"):
    #获取最近x天的价格变化情况
    top_symbols = json.dumps(get_top_symbols()).replace(" ", "")
    url = 'https://www.binance.com/api/v3/ticker?symbols=' + top_symbols + '&windowSize='+interval
    print(url)
    resp = request_binance(url)
    return resp

def get_all_symbols():
    #/fapi/v1/ticker/price
    url = 'https://fapi.binance.com/fapi/v1/ticker/price'
    resp = request_binance(url)
    return resp

def get_top_symbols():
    return top100_symbols
    symbols = get_all_symbols()[:100]
    print(symbols)
    top_symbols = []
    for symbol in symbols:
        print(symbol)
        top_symbols.append(symbol['symbol'])
    #top_symbols = [symbol['symbol'] for symbol in symbols]
    return top_symbols
