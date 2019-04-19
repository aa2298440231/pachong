import urllib.request
import json
import urllib.parse
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
url="https://fanyi.baidu.com/v2transapi"
def get_post(str):
    post={
        'from':"en",
        'to':"zh",
        'query':str,
        'transtype':"realtime",
        'simple_means_flag':"3",
        'sign':"503011.217042",
        'token':"80945ac459c14886663cf8fc53617096",
    }
    return post
heades_data={
'Cookie':"BAIDUID=B652BA03057135AC00BA9ABCFEA1A995:FG=1; BIDUPSID=B652BA03057135AC00BA9ABCFEA1A995; PSTM=1554443175; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=HBFQngzdGF1NXV3VVZBTXI4Zk1BUy05T3FxSEJGTDE5M0UyQ2JsS3hnYzdnTlZjRVFBQUFBJCQAAAAAAAAAAAEAAAC1WWvzZmx3bnh1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADvzrVw7861cV; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; locale=zh; delPer=0; H_PS_PSSID=28884_1434_21121_28774_28722_28557_28834_28585_28604; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1555505635,1555661776,1555681721,1555681901; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1555681901; from_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
}
str="yes"
response=urllib.request.Request(url=url,headers=heades_data,data=urllib.parse.urlencode(get_post(str)).encode("gzip"))
fanyi_data=urllib.request.urlopen(response)
print(fanyi_data)