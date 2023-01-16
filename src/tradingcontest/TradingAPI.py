import requests
import json
import httpx
import base64
from functools import *
import time

base_url = "https://aitrad.in/"

def escape_url(url):
    #对url中的?、=、\、&执行转义
    url = url.replace('?', '%3F').replace('=', '%3D').replace('/', '%2F').replace('&', '%26')
    return url

async def request_json(url):
    #请求代理服务器
    agent_url = base_url + url
    print(agent_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(agent_url)
    print(response.status_code)
    if response.status_code != 200:
        print(response)
        return None
    return json.loads(response.text)

async def request_txt(url):
    #请求代理服务器
    agent_url = base_url + url
    print(agent_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(agent_url)
    print(response.status_code)
    if response.status_code != 200:
        print(response)
        return None
    return response.text

async def request_file(url):
    #请求代理服务器
    agent_url = base_url + url
    print(agent_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(agent_url)
    print(response.status_code)
    if response.status_code != 200:
        print(response)
        return None
    return response.content

async def get_last_version():
    #获取最新版本号
    url = 'version/'
    resp = await request_json(url)
    return resp

async def download_last_version():
    #下载最新版本
    url = 'download_last/'
    resp = await request_json(url)
    return resp

def get_start_up_code():
    #获取启动代码
    url = 'start_up_code/'
    resp = requests.get(base_url+url)
    print(resp.text)
    return resp.text