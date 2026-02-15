import requests
import execjs


with open('课/测4公共资源.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode)

for i in range(5):

    json_data = {
        'pageNo': i + 1,
        'pageSize': 10,
        'total': 728,
        'type': '11',
        'timeType': '0',  
    }
    ana = ctx.call('sign', json_data)

    json_data["ts"] = ana["ts"]

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://ggzyfw.fj.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://ggzyfw.fj.gov.cn/index/newList/?type=11',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'portal-sign': ana["portal-sign"],
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }



    response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList', headers=headers, json=json_data)

    res = response.json()
    # print(res["Data"])
    ana = ctx.call('data_de', res["Data"])
    print(ana)  




