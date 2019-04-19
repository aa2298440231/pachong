import urllib.request
import json
import urllib.parse
import ssl
import pprint
ssl._create_default_https_context=ssl._create_unverified_context
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
def get_post(str):
    post={
        'i':str,
        'from':"en",
        'to':"zh - CHS",
        'smartresult':"dict",
        'client':"fanyideskweb",
        'salt':"15556871593500",#emmm
        'sign':"10c32e10790706905bec2fe52eb36902",#weizhi  978456eb55df87ee03fb408f816633f5
        'ts':"1555687135134",
        'bv':"db6b9693e24ea152843dd96fcd289f0f",
        'doctype':"json",
        'version':"2.1",
        'keyfrom':"fanyi.web",
        'action':"FY_BY_CLICKBUTTION",
    }
    return post
heades_data={
'Cookie':"OUTFOX_SEARCH_USER_ID_NCOO=1890657925.3184712; OUTFOX_SEARCH_USER_ID=-725726515@10.168.8.64; JSESSIONID=aaarcwjTZ1PuAhwfog2Ow; ___rl__test__cookies=1555685768764",
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
'Accept':"application / json, text / javascript, * / *; q = 0.01",
'Accept - Language':"zh - CN",
'Cache - Control':"no - cache",
'Connection':"Keep-Alive",
'Content-Length':"235",
'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
'Host':"fanyi.youdao.com",
'Origin':"http://fanyi.youdao.com",
'Referer':"http://fanyi.youdao.com/",
'X-Requested-With':"XMLHttpRequest",
}
str="Internal Server Error"
#str=input()
response=urllib.request.Request(url=url,headers=heades_data,data=urllib.parse.urlencode(get_post(str)).encode("utf-8"))
fanyi_data=json.loads(urllib.request.urlopen(response).read().decode('utf-8'))
pprint.pprint(fanyi_data)
#pprint.pprint(fanyi_data['smartResult']['entries'])
#pprint.pprint(fanyi_data['translateResult'][0][0]['tgt'])