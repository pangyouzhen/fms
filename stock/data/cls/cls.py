cls_headers = {
    'Host': 'www.cls.cn',
    'Connection': 'keep-alive',
    'Content-Length': '112',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.cls.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
cls_payload = "{\"type\":\"telegram\",\"keyword\":\"%s\",\"page\":0,\"rn\":20,\"os\":\"web\",\"sv\":\"7.2.2\",\"app\":\"CailianpressWeb\"}"
cls_url = "https://www.cls.cn/api/sw?app=CailianpressWeb&os=web"
