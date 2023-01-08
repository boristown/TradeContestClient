"""
Trading redefine.
"""
import toga

from toga.style.pack import CENTER, COLUMN, ROW, Pack, BOTTOM, TOP, LEFT, RIGHT
#import httpx
from tradingcontest.binanceAPI import *
from collections import defaultdict
import time
import threading
import asyncio

user_token = None

def HCenterElem(element):
    return toga.Box(
        children=[
            element
        ],
        style=Pack(
            direction=ROW,
            alignment=CENTER,
            padding=5
        )
    )

def ColumnBox(children):
    return toga.Box(
        children=[HCenterElem(c) for c in children],
        style=Pack(
            direction=COLUMN,
            alignment=CENTER,
            padding=10
        )
    )

def BlackLabel(text):
    return toga.Label(
        text,
        #style=Pack(padding=(0, 5),color="black",alignment=CENTER,flex=1)
        style=Pack(padding=(0, 5),color="black",alignment=CENTER)
    )

def FlexInput(placeholder,on_change=None):
    return toga.TextInput(placeholder=placeholder,
        style=Pack(padding=(0, 5), flex=1),
        on_change=on_change
    )

def FlexButton(text,handler):
    return toga.Button(
        text,
        on_press=handler,
        style=Pack(padding=(0, 5),flex=1)
    )

def FixedButton(label, on_press, width):
    return toga.Button(
        label,
        on_press=on_press,
        style=Pack(padding=(0, 5),width=width)
    )

def FlexNumber():
    return toga.NumberInput(
        style=Pack(padding_left = 5, flex=1),
    )

def LayoutBox(children):
    children = [
        toga.Box(
            children=child, 
            style=Pack(
                flex=1,
                direction=ROW,
                alignment=CENTER,
                padding=5
            )) for child in children
        ]
    return toga.Box(
        children=children,
        style=Pack(
            direction=COLUMN,
            alignment=CENTER,
            padding=5,
            flex = 1
            )
    )

class TradingContest(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        global user_token

        if user_token is None:
            first_page = self.login_page()
        else:
            first_page = self.main_page()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = first_page
        self.main_window.show()

    def login_page(self):
        #用toga创建一个登录页面
        #布局如下：
        #手机号Label：国家区号选择下拉框（默认中国+86）+手机号输入框
        #验证码Label：验证码输入框+获取验证码按钮（回调函数：self.on_valnum）
        #登录/注册按钮（回调函数：self.on_login）
        #用toga.box布局
        #水平拉伸元素，垂直居中元素
        
        #手机号Label
        self.phone_label = BlackLabel('【手机号】')
        #国家区号选择下拉框
        self.country_code = toga.Selection(
            items=['中国+86', '美国+1', '英国+44', '日本+81', '韩国+82', '法国+33', '德国+49', '意大利+39', '西班牙+34', '俄罗斯+7', '加拿大+1', '澳大利亚+61', '新西兰+64', '印度+91', '巴西+55', '阿根廷+54', '墨西哥+52', '南非+27', '马来西亚+60', '泰国+66', '菲律宾+63', '印尼+62', '越南+84', '新加坡+65', '马尔代夫+960', '伊朗+98', '土耳其+90', '以色列+972', '阿联酋+971', '沙特阿拉伯+966', '卡塔尔+974', '科威特+965', '巴林+973', '阿曼+968', '约旦+962', '黎巴嫩+961', '伊拉克+964', '叙利亚+963', '巴勒斯坦+970', '也门+967', '科特迪瓦+225', '尼日利亚+234', '埃及+20', '南苏丹+211', '利比亚+218', '苏丹+249', '摩洛哥+212', '阿尔及利亚+213', '突尼斯+216', '埃塞俄比亚+251', '肯尼亚+254', '乌干达+256', '坦桑尼亚+255', '塞舌尔+248', '毛里求斯+230', '马达加斯加+261', '留尼汪+262', '津巴布韦+263', '莫桑比克+258'],
            on_select=self.on_select,
            style=Pack(width=150),
        )

        #手机号输入框
        self.phone_input = FlexNumber()

        #验证码Label
        self.valnum_label = BlackLabel('【验证码】')

        #验证码输入框
        self.valnum_input = FlexNumber()

        #获取验证码按钮
        self.valnum_button = FixedButton('获取验证码',self.on_valnum,150)

        #登录/注册按钮
        self.login_button = FlexButton('登录/注册',self.on_login)

        #登录页面布局
        login_box = LayoutBox(
            [
                [self.phone_label],
                [self.country_code, self.phone_input],
                [self.valnum_label],
                [self.valnum_input, self.valnum_button],
                [self.login_button]
            ]
        )

        return login_box
    
    def on_select(self, widget):
        print("选中的国家区号：", widget.value)

    def on_valnum(self, widget):
        print("获取验证码")

    def on_login(self, widget):
        print("登录/注册")
        self.main_window.content = self.main_page()
    
    def main_page(self):
        #用toga创建一个主页面
        #显示：
        #第三轮模拟交易竞赛
        #2023年1月2日~2023年1月8日”
        #余额：1000000 USDT
        #当前排名：第3名
        #之后是按钮：
        #查看排行榜
        #查看我的交易
        #查看我的订单
        #查看我的持仓
        #用toga.box从上往下布局
        
        #第三轮模拟交易竞赛（水平居中）
        self.round_label = BlackLabel('第三轮模拟交易竞赛')
        #2023年1月2日~2023年1月8日”
        self.date_label = BlackLabel('2023年1月2日~2023年1月8日')
        #余额：1000000 USDT
        self.balance_label = BlackLabel('余额：1000000 USDT')
        #当前排名：第3名
        self.rank_label = BlackLabel('当前排名：第3名')
        #查看排行榜
        self.rank_button = FlexButton('查看排行榜',self.on_rank)
        #浏览市场
        self.view_markets = FlexButton('浏览市场',self.on_market)
        #开始交易
        self.start_trade = FlexButton('开始交易',self.on_trade)
        #查看我的交易
        self.trade_log_button = FlexButton('交易日志',self.on_trade_log)
        #查看我的订单
        self.order_button = FlexButton('我的订单',self.on_order)
        #查看我的持仓
        self.position_button = FlexButton('查看我的持仓',self.on_position)
        #退出登录
        self.logout_button = FlexButton('退出登录',self.on_logout)
        #布局
        main_box = ColumnBox([self.round_label,self.date_label,self.balance_label,self.rank_label,self.view_markets,self.start_trade,self.trade_log_button,self.order_button,self.position_button,self.rank_button,self.logout_button])
        return main_box

    def on_logout(self, widget):
        print("退出登录")
        self.main_window.content = self.login_page()
    
    async def on_market(self, widget):
        self.loading_market = True
        self.main_window.content = LayoutBox([
            [BlackLabel("载入中……")],
            [FlexButton('返回主页',self.on_main_page)]
            ])
        self.view_markets.text = "浏览市场(载入中……)"
        await self.show_market_page()
        self.view_markets.text = "浏览市场"
    
    async def show_market_page(self):
        content = await self.market_page()
        if self.loading_market:
            self.main_window.content = content
            self.main_window.content.refresh()

    #实现异步方法get_market_data
    async def get_market_data(self):
        #获取数据
        if not self.loading_market: return
        data1d = await get_binance_ticker("1d")
        #print(data1d)
        if not self.loading_market: return
        await asyncio.sleep(0.8)
        if not self.loading_market: return
        data7d = await get_binance_ticker("7d")
        if not self.loading_market: return
        #print(data7d)
        #print(data1d)
        #print(data7d)
        symbolinfo = defaultdict(dict)
        for d1d in data1d:
            symbol = d1d["symbol"]
            symbolinfo[symbol]["price"] = d1d["lastPrice"]
            symbolinfo[symbol]["Change1d"] = d1d["priceChangePercent"]
            symbolinfo[symbol]["Volume1d"] = d1d["quoteVolume"]
        for d7d in data7d:
            symbol = d7d["symbol"]
            symbolinfo[symbol]["Change7d"] = d7d["priceChangePercent"]
            symbolinfo[symbol]["Volume7d"] = d7d["quoteVolume"]
        data = []
        top100_symbols = get_top_symbols()
        for symbol in top100_symbols:
            info = symbolinfo[symbol]
            data.append([symbol,float(info["price"]),float(info["Change1d"]),float(info["Change7d"]),info["Volume1d"],info["Volume7d"]])
        #data.sort(key=lambda x:x[2],reverse=True)
        data = [[d[0],d[1],d[2],d[3]] for d in data]
        return data

    def on_search(self, widget):
        print("搜索")
        txt = self.search_input.value.upper()
        self.realtabledata = self.tabledata[:]
        self.realtabledata = [itm for itm in self.realtabledata if txt in itm[0]]
        self.market_table.data = self.realtabledata
        #self.market_table.refresh()


    async def market_page(self):
        self.search_input = FlexInput("输入币种名称执行搜索",self.on_search)
        self.search_button = FixedButton("搜索",self.on_search,100)
        header = ['市场', '价格', '日涨幅%', '周涨幅%']
        self.tabledata = await self.get_market_data()
        self.realtabledata = self.tabledata[:]
        self.market_table = toga.Table(header, data=self.realtabledata, style=Pack(padding=10, flex=1, alignment=CENTER))
        self.refresh_button = FlexButton('刷新',self.refresh_table)
        return LayoutBox(
            [
                [FlexButton('返回主页',self.on_main_page),FlexButton('开始交易',self.on_trade)],
                [self.refresh_button,FlexButton('默认排序',self.on_sort_by_default)],
                [FlexButton('按日涨幅升序',self.on_sort_by_change1d),FlexButton('按日涨幅降序',self.on_sort_by_change1d_desc)],
                [FlexButton('按周涨幅升序',self.on_sort_by_change7d),FlexButton('按周涨幅降序',self.on_sort_by_change7d_desc)],
                [self.search_input],
                [self.market_table]
            ]
        )
    
    def on_sort_by_default(self, widget):
        print("默认排序")
        #self.tabledata.sort(key=lambda x:x[0])
        self.realtabledata = self.tabledata[:]
        self.market_table.data = self.realtabledata
        print(self.realtabledata)
        #self.on_search(widget)
        #self.market_table.refresh()
    
    def on_sort_by_change7d(self, widget):
        print("按周涨幅升序")
        self.realtabledata = self.tabledata[:]
        self.realtabledata.sort(key=lambda x:x[3])
        self.market_table.data = self.realtabledata
        print(self.realtabledata)
        #self.on_search(widget)
        #self.market_table.refresh()
    
    def on_sort_by_change1d(self, widget):
        print("按日涨幅升序")
        self.realtabledata = self.tabledata[:]
        self.realtabledata.sort(key=lambda x:x[2])
        self.market_table.data = self.realtabledata
        print(self.realtabledata)
        #self.on_search(widget)
        #self.market_table.refresh()
    
    def on_sort_by_change7d_desc(self, widget):
        print("按周涨幅降序")
        self.realtabledata = self.tabledata[:]
        self.realtabledata.sort(key=lambda x:x[3],reverse=True)
        self.market_table.data = self.realtabledata
        print(self.realtabledata)
        #self.on_search(widget)
        #self.market_table.refresh()

    def on_sort_by_change1d_desc(self, widget):
        print("按日涨幅降序")
        self.realtabledata = self.tabledata[:]
        self.realtabledata.sort(key=lambda x:x[2],reverse=True)
        self.market_table.data = self.realtabledata
        print(self.realtabledata)
        #self.on_search(widget)
        #self.market_table.refresh()
    
    async def refresh_table(self, widget):
        print("刷新")
        self.refresh_button.enabled = False
        self.refresh_button.text = "刷新中..."
        self.loading_market = True
        self.tabledata = await self.get_market_data()
        self.market_table.data = self.tabledata[:]
        self.refresh_button.text = "刷新"
        self.refresh_button.enabled = True
        self.loading_market = False
    
    def on_main_page(self, widget):
        self.loading_market = False
        print("返回主页")
        self.main_window.content = self.main_page()
    
    def on_trade_log(self, widget):
        print("查看交易日志")
        self.main_window.content = self.trade_log_page()

    def on_rank(self, widget):
        print("查看排行榜")
        self.main_window.content = self.rank_page()

    def rank_page(self):
        pass

    def on_trade(self, widget):
        print("查看我的交易")
        self.main_window.content = self.trade_page()
    
    def trade_page(self):
        pass

    def on_order(self, widget):
        print("查看我的订单")
        self.main_window.content = self.order_page()
    
    def order_page(self):
        pass

    def on_position(self, widget):
        print("查看我的持仓")
        self.main_window.content = self.position_page()
    
    def position_page(self):
        pass

def main():
    return TradingContest("模拟交易竞赛")

'''
D:
cd BeeWare\tradingcontest
briefcase dev
briefcase update android -d
briefcase run android -u
'''