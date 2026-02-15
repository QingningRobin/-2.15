import requests
import execjs


cookies = {
    'mobile_iindex_uuid': '8f4a181d-4dad-5c4b-bc85-b31215a0f6cc',
    'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f': '1771069591,1771128351',
    'Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f': '1771128351',
    'HMACCOUNT': 'BD94F09D1D87D798',
}


with open('课/测5艾曼指数.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode)

for i in range(5):

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.chinaindex.net/search',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'UUID': '8f4a181d-4dad-5c4b-bc85-b31215a0f6cc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'funcID': '2614',
        'incognitoMode': '0',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'mobile_iindex_uuid=8f4a181d-4dad-5c4b-bc85-b31215a0f6cc; Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f=1771069591,1771128351; Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f=1771128351; HMACCOUNT=BD94F09D1D87D798',
    }


    params = {
        'keyWord': '仙',
        'page_no': str(i + 1),
        'tab': 'artistTab',

    }
    ana = ctx.call('sign', params)
    params["sign"] = ana

    response = requests.get(
        'https://www.chinaindex.net/iIndexMobileServer/mobile/comm/getSearchResult',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    res = response.json()
    ana = ctx.call('data_de', res)
    print(ana)





