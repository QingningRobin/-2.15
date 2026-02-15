import requests
import execjs


cookies = {
    'webapp': '1',
    'siteCode': 'sxzfcg',
    'siteGuid': '6883226032309207040',
    'regioncode': '140001000',
    'regionguid': '140001',
    'theme': 'default',
    'regionpguid': '232',
    'rootregionguid': '232',
    'isOpenArea': 'true',
    'regionname': '%E7%9C%81%E6%9C%AC%E7%BA%A7',
}


with open('课/测2电子卖场.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode)

for i in range(3):
    ana = ctx.call('ans', i + 1)

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'form-token': '9d0205c4201bf15687b089d84ba727d1',
        'nsssjss': ana["nsssjss"],
        'origin': 'https://shanxisheng-zfcgdzmcgov.cn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://shanxisheng-zfcgdzmcgov.cn/gpmall-main-web/basic/sxNotice',
        'regioncode': '140001000',
        'regionguid': '140001',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sign': ana["sign"],
        'sitecode': 'sxzfcg',
        'siteguid': '6883226032309207040',
        'time': str(ana["time"]),
        'timestamp': ana["timestamp"],
        'url': '/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'webapp': '1',
        # 'cookie': 'webapp=1; siteCode=sxzfcg; siteGuid=6883226032309207040; regioncode=140001000; regionguid=140001; theme=default; regionpguid=232; rootregionguid=232; isOpenArea=true; regionname=%E7%9C%81%E6%9C%AC%E7%BA%A7',
    }
                    
    json_data = {
        'regionGuid': '232',
        'regionCode': '140000000',
        'webApp': '1',
        'pageSize': 10,
        'pageNum': i + 1,
        'noticeType': '0',
    }

    response = requests.post(
        'https://shanxisheng-zfcgdzmcgov.cn/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList',
        # cookies=cookies,
        headers=headers,
        json=json_data,
    )

    res = response.text
    print(res)




