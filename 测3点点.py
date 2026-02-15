import requests
import execjs
import re


cookies = {
    'i18n_redirected': 'zh',
    'deviceid': '7cdb3c64a73ab937865c4e554f374fd',
    'Qs_lvt_404253': '1771063656',
    '_ga': 'GA1.1.2090363413.1771063660',
    'mediav': "%7B%22eid%22%3A%221089729%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Xf'%2FSif%23%5DD9%3CdgG%3DZa%3Eu%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22Xf'%2FSif%23%5DD9%3CdgG%3DZa%3Eu%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A1%7D",
    'Hm_lvt_beac6fc75c36ba113cbffa9a59b1b18d': '1771063657,1771069486',
    'HMACCOUNT': 'BD94F09D1D87D798',
    'Hm_lvt_8a5bd6e095cd118016489cab0443c2d7': '1771063657,1771069486',
    'Hm_lvt_d185b2974609101d8f9340b5f861ca70': '1771063657,1771069486',
    'showMajorDialog': 'true',
    'Qs_pv_404253': '4458258357777739000%2C2201494892241580000%2C2721410789238322700%2C1205913864957818600%2C4522550657357011000',
    'Hm_lpvt_beac6fc75c36ba113cbffa9a59b1b18d': '1771077124',
    'Hm_lpvt_8a5bd6e095cd118016489cab0443c2d7': '1771077124',
    'Hm_lpvt_d185b2974609101d8f9340b5f861ca70': '1771077124',
    '_uetsid': 'fdf1d770098c11f1a6effd2aed9adfab|1ek89uk|2|g3k|0|2236',
    '_ga_GVCWL6PNZ2': 'GS2.1.s1771072785$o3$g1$t1771077125$j60$l0$h0',
    '_uetvid': 'fdf1ff10098c11f1ac74c71477b7945d|b429nc|1771077126385|14|1|bat.bing.com/p/conversions/c/h',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': "i18n_redirected=zh; deviceid=7cdb3c64a73ab937865c4e554f374fd; Qs_lvt_404253=1771063656; _ga=GA1.1.2090363413.1771063660; mediav=%7B%22eid%22%3A%221089729%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Xf'%2FSif%23%5DD9%3CdgG%3DZa%3Eu%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22Xf'%2FSif%23%5DD9%3CdgG%3DZa%3Eu%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A1%7D; Hm_lvt_beac6fc75c36ba113cbffa9a59b1b18d=1771063657,1771069486; HMACCOUNT=BD94F09D1D87D798; Hm_lvt_8a5bd6e095cd118016489cab0443c2d7=1771063657,1771069486; Hm_lvt_d185b2974609101d8f9340b5f861ca70=1771063657,1771069486; showMajorDialog=true; Qs_pv_404253=4458258357777739000%2C2201494892241580000%2C2721410789238322700%2C1205913864957818600%2C4522550657357011000; Hm_lpvt_beac6fc75c36ba113cbffa9a59b1b18d=1771077124; Hm_lpvt_8a5bd6e095cd118016489cab0443c2d7=1771077124; Hm_lpvt_d185b2974609101d8f9340b5f861ca70=1771077124; _uetsid=fdf1d770098c11f1a6effd2aed9adfab|1ek89uk|2|g3k|0|2236; _ga_GVCWL6PNZ2=GS2.1.s1771072785$o3$g1$t1771077125$j60$l0$h0; _uetvid=fdf1ff10098c11f1ac74c71477b7945d|b429nc|1771077126385|14|1|bat.bing.com/p/conversions/c/h",
}

response = requests.get('https://app.diandian.com/', cookies=cookies, headers=headers)

pattern = r'u:\s*\{([^}]+)\}'
u_match = re.search(pattern, response.text, re.DOTALL)  
if u_match:
    inner = u_match.group(1)  
    # print(inner)
    kv_pattern = r'([skl]):\s*"([^"]*)"'
    matches = re.findall(kv_pattern, inner)
    value_dict = dict(matches)
    
    s_val = value_dict.get('s')
    k_val = value_dict.get('k')
    l_val = value_dict.get('l')
    d_val = value_dict.get('d')
# print(s_val, k_val, l_val, d_val)


cookies = {
    'deviceid': '7cdb3c64a73ab937865c4e554f374fd',
    'Qs_lvt_404253': '1771063656',
    '_ga': 'GA1.1.2090363413.1771063660',
    'Qs_pv_404253': '2390038020803379700%2C1458693686157335600%2C4400383428677953000',
    '_uetsid': 'fdf1d770098c11f1a6effd2aed9adfab|1ek89uk|2|g3k|0|2236',
    '_uetvid': 'fdf1ff10098c11f1ac74c71477b7945d|pyxzm6|1771066633984|1|1|bat.bing.com/p/conversions/c/h',
    '_ga_GVCWL6PNZ2': 'GS2.1.s1771066639$o2$g1$t1771066642$j57$l0$h0',
}


with open('课/测3点点.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode)

for i in range(1):
    ana = ctx.call('data_en', s_val, k_val, l_val, d_val)

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://app.diandian.com',
        'Pragma': 'no-cache',
        'Referer': 'https://app.diandian.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'language': 'zh',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'deviceid=7cdb3c64a73ab937865c4e554f374fd; Qs_lvt_404253=1771063656; _ga=GA1.1.2090363413.1771063660; Qs_pv_404253=2390038020803379700%2C1458693686157335600%2C4400383428677953000; _uetsid=fdf1d770098c11f1a6effd2aed9adfab|1ek89uk|2|g3k|0|2236; _uetvid=fdf1ff10098c11f1ac74c71477b7945d|pyxzm6|1771066633984|1|1|bat.bing.com/p/conversions/c/h; _ga_GVCWL6PNZ2=GS2.1.s1771066639$o2$g1$t1771066642$j57$l0$h0',
    }

    params = {
        'market_id': '',
        'sub_type': '1',
        'is_detail': '0',
        'is_go_sea': '0',
        'country_id': '',
        'k': ana,
    }

    response = requests.get('https://api.diandian.com/pc/app/v2/user/favorite', params=params, cookies=cookies, headers=headers)

    res = response.text
    print(res)




