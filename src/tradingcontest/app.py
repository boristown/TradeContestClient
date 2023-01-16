"""
Trading redefine.
"""
import toga

from toga.style.pack import CENTER, COLUMN, ROW, Pack, BOTTOM, TOP, LEFT, RIGHT
#import httpx
from tradingcontest.binanceAPI import *
from tradingcontest.TradingAPI import *
from collections import defaultdict
import time
import threading
import asyncio

class TradingContest(toga.App):

    def startup(self):
        #下载最新的Python代码
        #然后动态执行
        start_up_code = get_start_up_code()

        if start_up_code is not None:
            exec(start_up_code)
        else:
            #弹出提示框，显示：加载初始界面失败，无法连接到服务器
            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = toga.Label('加载初始界面失败，无法连接到服务器')
            self.main_window.show()

def main():
    return TradingContest("模拟交易竞赛")

'''
D:
cd BeeWare\tradingcontest
briefcase dev
briefcase update android -d
briefcase run android -u
'''