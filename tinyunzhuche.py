import urllib.request
import urllib.parse
import dama
import 代理ip
yzm_url='http://member.tingyun.com/member/user/getImage?date=Sat%20Apr%2020%202019%2017:05:05%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
dx_url='http://member.tingyun.com/member/regist/sendMoblieCode'
head_data={
'Cookie':"JSESSIONID=6400BD139A08671A5023D901A1553842; ty_member_uid=352c4a7e52bcae3bdad58ea9cfdb356d; SERVER_ID=279fc1c9-d3eeddd7",
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
def main(iphon):
    yzm_response=urllib.request.Request(url=yzm_url,headers=head_data)
    with open("yzm.png","wb") as f:
        f.write(urllib.request.urlopen(yzm_response).read())
    yzm=dama.get_code_text(file_name='yzm')
    dx_respones=urllib.request.Request(url=dx_url,headers=head_data,data=urllib.parse.urlencode(get_post(yzm=yzm,iphon=iphon)).encode('utf-8'))
    print(urllib.request.urlopen(dx_respones).read().decode("utf-8"))

代理ip.dailiip()
main('13125183836')