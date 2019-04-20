import urllib.request
import urllib.parse
import dama
import threading
import 代理ip
class tingyun(threading.Thread):
    yzm_url='http://member.tingyun.com/member/user/getImage?date=Sat%20Apr%2020%202019%2017:05:05%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
    dx_url='http://member.tingyun.com/member/regist/sendMoblieCode'
    head_data={
    'Cookie':"JSESSIONID=6D066A0ADD605A33918A89920F60A877; ty_member_uid=adcde6b43ddd3710d4e0b3cf95bfd918; SERVER_ID=279fc1c9-d3eeddd7",
    'Host':"member.tingyun.com",
    'Referer':"http://member.tingyun.com/member/regist",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    }
    def get_post(yzm,iphon):
        post_data={
            'mobileNum':iphon,#13125183836
            'codeCaptcha':yzm,
            'type':"1",
        }
        return post_data
    def __init__(self,iphon):
        threading.Thread.__init__(self)
        self.iphon=iphon
    def run(self):
        yzm_response=urllib.request.Request(url=tingyun.yzm_url,headers=tingyun.head_data)
        with open("yzm.png","wb") as f:
            f.write(urllib.request.urlopen(yzm_response).read())
        yzm=dama.get_code_text(file_name='yzm')
        dx_respones=urllib.request.Request(url=tingyun.dx_url,headers=tingyun.head_data,data=urllib.parse.urlencode(tingyun.get_post(yzm=yzm,iphon=self.iphon)).encode('utf-8'))
        print(urllib.request.urlopen(dx_respones).read().decode("utf-8"))

代理ip.dailiip()
t=tingyun('13343509055')#13125183836
t.start()