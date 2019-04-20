import urllib.request
import json
import urllib.parse
import ssl
import pprint
ssl._create_default_https_context=ssl._create_unverified_context
url="http://fy.iciba.com/ajax.php?a=fy"
def get_post(str):
    post={
        'f':"auto",
        't':"auto",
        'w':str,
    }
    return post
heades_data={
'Cookie':"iciba_u_rand=6d8ba9bcfa60c4298123f4fafe8313ef%4027.155.93.79; iciba_u_rand_t=1555728876; UM_distinctid=16a38aabe2249b-058c9ab0f78e4e-3d644601-1fa400-16a38aabe23748; CNZZDATA1256573702=920922850-1555728091-http%253A%252F%252Fwww.iciba.com%252F%7C1555728091; __gads=ID=2d57dd182e5dfb12:T=1555728887:S=ALNI_MbwX44FipcaZfdsJuy_DjaOZFfb2A",
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
# 'Accept':"application / json, text / javascript, * / *; q = 0.01",
# 'Accept - Language':"zh - CN",
# 'Cache - Control':"no - cache",
# 'Connection':"Keep-Alive",
# 'Content-Length':"235",
# 'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
# 'Host':"fanyi.youdao.com",
# 'Origin':"http://fanyi.youdao.com",
# 'Referer':"http://fanyi.youdao.com/",
# 'X-Requested-With':"XMLHttpRequest",
}

str="yes"#"Internal Server Error"
str=input()
response=urllib.request.Request(url=url,headers=heades_data,data=urllib.parse.urlencode(get_post(str)).encode("utf-8"))
fanyi_data=json.loads(urllib.request.urlopen(response).read().decode('utf-8'))
pprint.pprint(fanyi_data)
#pprint.pprint(fanyi_data['smartResult']['entries'])
#pprint.pprint(fanyi_data['translateResult'][0][0]['tgt'])