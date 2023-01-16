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
import httpx
import base64
from functools import *
import time

base_url = "http://47.242.55.109:2023/"
base_url = "https://aitrad.in/"

def escape_url(url):
    #对url中的?、=、\、&执行转义
    url = url.replace('?', '%3F').replace('=', '%3D').replace('/', '%2F').replace('&', '%26')
    return url

def html_kline(symbol, interval, windowSize):
    symbol = symbol.upper()
    interval = interval.replace('分钟', 'm').replace('小时', 'h').replace('天', 'd')
    base_time = 0
    if '天' in windowSize:
        base_time = 86400000
    elif '月' in windowSize:
        base_time = 2592000000
    elif '年' in windowSize:
        base_time = 31536000000
    windowSize = int(windowSize.replace('天', '').replace('月', '').replace('年', '').replace('最近','')) * base_time
    current_time = int(time.time() * 1000)
    start_time = current_time - windowSize
    return base_url + 'kline/' + symbol + '?interval=' + interval + '&start_time=' + str(start_time) + '&end_time=' + str(current_time)
    
async def request_binance(url):
    #对url中的?、=、\、&执行转义
    #url = escape_url(url)
    #将url转为base64编码
    url = base64.b64encode(url.encode('utf-8')).decode('utf-8')
    #请求代理服务器
    #session = requests.session()
    agent_url = base_url + 'B?x=' + url
    print(agent_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(agent_url)
    print(response.status_code, response.text, response.headers, response.content)
    if response.status_code != 200:
        return None
    return json.loads(json.loads(response.text))

async def get_binance_ticker(usdt_on,interval="1d"):
    #获取最近x天的价格变化情况
    #top100_symbols = await get_top_symbols()
    #top_symbols = json.dumps(top100_symbols).replace(" ", "")
    #url = 'api/v3/ticker?symbols=' + top_symbols + '&windowSize='+interval
    #print(url)
    #resp = await request_binance(url)
    async with httpx.AsyncClient() as client:
        if usdt_on:
            url = base_url+'ticker_u/'+interval
        else:
            url = base_url+'ticker_b/'+interval
        print(url)
        response = await client.get(url)
    print(response.status_code)
    if response.status_code != 200:
        return None
    #print(response.text)
    return json.loads(response.text)

def get_all_symbols():
    #/fapi/v1/ticker/price
    url = 'fapi/v1/ticker/price'
    resp = request_binance(url)
    return resp

# def get_SYM_USDT():
#     return SYM_USDT[:100]

# def get_SYM_BTC():
#     return SYM_BTC[:100]
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(base_url+'symbols')
    # #print(response.status_code, response.text, response.headers, response.content)
    # if response.status_code != 200:
    #     return None
    # print(response.text)
    # return json.loads(response.text)
