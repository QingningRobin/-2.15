import requests
import execjs





with open('课/测1四川.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode)

for i in range(3):
    ana = ctx.call('data_en', i + 1)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://202.61.89.161:12021',
        'Pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'sign': ana["sign"],
        'source': ana["source"],
        'timestamp': ana["timestamp"],
        'urlprefix': '',
    }
                    
    json_data = {
        'parameter': ana["parameter"],
    }

    response = requests.post(
        'http://202.61.89.161:12021/api/api/loginSidePageEDE/getPurchaseOfAgriculturalMachinery',
        headers=headers,
        json=json_data,
        verify=False,
    )

    res = response.json()
    # print(res)
    print(ctx.call('data_de', res["data"]))



