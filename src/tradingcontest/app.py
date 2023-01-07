"""
Trading redefine.
"""
import toga

from toga.style.pack import CENTER, COLUMN, ROW, Pack, BOTTOM, TOP, LEFT, RIGHT
#import httpx

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
        style=Pack(padding=(0, 5),color="black",alignment=CENTER)
    )

def FlexInput(placeholder):
    return toga.TextInput(placeholder=placeholder,style=Pack(padding=(0, 5), flex=1))

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
    
    def on_market(self, widget):
        print("浏览市场")
        self.main_window.content = self.market_page()
    
    def on_search(self, widget):
        print("搜索")

    def market_page(self):
        self.search_input = FlexInput("输入币种名称")
        self.search_button = FixedButton("搜索",self.on_search,100)
        header = ['市场', '价格', '日涨跌', '周涨跌']
        data = [
            ('BTCUSDT', '10000', '10%', '20%'),
            ('ETHUSDT', '1000', '10%', '20%'),
            ('BNBUSDT', '100', '10%', '20%'),
            ('ADAUSDT', '10', '10%', '20%'),
            ('DOTUSDT', '1', '10%', '20%'),
            ('XRPUSDT', '0.1', '10%', '20%'),
            ('LTCUSDT', '100', '10%', '20%'),
            ('LINKUSDT', '10', '10%', '20%'),
            ('BCHUSDT', '100', '10%', '20%'),
            ('UNIUSDT', '10', '10%', '20%'),
            ('SOLUSDT', '1', '10%', '20%'),
            ('DOGEUSDT', '0.1', '10%', '20%'),
            ('XLMUSDT', '0.1', '10%', '20%'),
            ('THETAUSDT', '0.1', '10%', '20%'),
            ('VETUSDT', '0.1', '10%', '20%'),
            ('ETCUSDT', '10', '10%', '20%'),
            ('TRXUSDT', '0.1', '10%', '20%'),
            ('FILUSDT', '10', '10%', '20%'),
            ('EOSUSDT', '10', '10%', '20%'),
            ('ATOMUSDT', '10', '10%', '20%'),
            ('AVAXUSDT', '10', '10%', '20%'),
            ('ICPUSDT', '10', '10%', '20%'),
            ('ALGOUSDT', '10', '10%', '20%'),
            ('MKRUSDT', '10', '10%', '20%'),
            ('AAVEUSDT', '10', '10%', '20%'),
            ('COMPUSDT', '10', '10%', '20%'),
            ('YFIUSDT', '10', '10%', '20%'),
            ('SNXUSDT', '10', '10%', '20%'),
            #添加其它更多市场
            ('ZECUSDT', '10', '10%', '20%'),
            ('XTZUSDT', '10', '10%', '20%'),
            ('NEOUSDT', '10', '10%', '20%'),
            ('DASHUSDT', '10', '10%', '20%'),
            ('BATUSDT', '10', '10%', '20%'),
            ('OMGUSDT', '10', '10%', '20%'),
            ('KSMUSDT', '10', '10%', '20%'),
            ('ZILUSDT', '10', '10%', '20%'),
            ('ZRXUSDT', '10', '10%', '20%'),
            ('EGLDUSDT', '10', '10%', '20%'),
            ('KNCUSDT', '10', '10%', '20%'),
            ('BALUSDT', '10', '10%', '20%'),
            ('OXTUSDT', '10', '10%', '20%'),
            ('NMRUSDT', '10', '10%', '20%'),
            ('RUNEUSDT', '10', '10%', '20%'),
            ('UMAUSDT', '10', '10%', '20%'),
            ('SUSHIUSDT', '10', '10%', '20%'),
            ('YFIIUSDT', '10', '10%', '20%'),
            ('SXPUSDT', '10', '10%', '20%'),
            ('RENBTCUSDT', '10', '10%', '20%'),
            ('RENUSDT', '10', '10%', '20%'),
            ('CRVUSDT', '10', '10%', '20%'),
            ('SANDUSDT', '10', '10%', '20%'),
            ('OCEANUSDT', '10', '10%', '20%'),
            ('BANDUSDT', '10', '10%', '20%'),
            ('ANKRUSDT', '10', '10%', '20%'),
            ('SUNUSDT', '10', '10%', '20%'),
            ('SRMUSDT', '10', '10%', '20%'),
            ('NUUSDT', '10', '10%', '20%'),
            ('RSRUSDT', '10', '10%', '20%'),
            ('TRBUSDT', '10', '10%', '20%'),
            ('BZRXUSDT', '10', '10%', '20%'),
            ('WAVESUSDT', '10', '10%', '20%'),
            ('KAVAUSDT', '10', '10%', '20%'),
            ('PAXGUSDT', '10', '10%', '20%'),
            ('DGBUSDT', '10', '10%', '20%'),
            ('LRCUSDT', '10', '10%', '20%'),
            ('STORJUSDT', '10', '10%', '20%'),
            ('ENJUSDT', '10', '10%', '20%'),
            ('STMXUSDT', '10', '10%', '20%'),
        ]
        self.table = toga.Table(header, data=data, style=Pack(padding=10, flex=1, alignment=CENTER))
        return LayoutBox(
            [
                [FlexButton('返回主页',self.on_main_page),FlexButton('开始交易',self.on_trade)],
                [self.search_input,self.search_button],
                [self.table]
            ]
        )
    
    def on_main_page(self, widget):
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


    async def say_hello(self, widget):
        pass
        # if self.name_input.value:
        #     name = self.name_input.value
        # else:
        #     name = 'stranger'

        # async with httpx.AsyncClient() as client:
        #     response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        # payload = response.json()

        # self.main_window.info_dialog(
        #     "Hello, {}".format(name),
        #     payload["body"],
        # )


def main():
    return TradingContest("模拟交易竞赛")

'''
D:
cd BeeWare\tradingcontest
briefcase dev
briefcase run android -u
'''