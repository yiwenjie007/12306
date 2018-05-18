# coding=utf-8
import requests
session = requests.session()
#访问登录页面
login_url = 'https://kyfw.12306.cn/otn/login/init'
response = session.get(login_url)

#获取验证码图片
image_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4532935388585555'
image_response = session.get(image_url)
with open('image.jpg','wb') as f:
    f.write(image_response.content)

check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
code = input('>>>请输入验证码')
data = {
    'answer': code,
    'login_site': 'E',
    'rand': 'sjrand'
}
check_response = session.post(check_url, data)
if check_response.json().get('result_code') == '4':
    login = 'https://kyfw.12306.cn/passport/web/login'
    form_data = {
        'username': 'angushuochepiao',
        'password': 'XXXXXX',
        'appid': 'otn'
    }
    login_response = session.post(login, form_data)
    if login_response.json().get('result_code') == 0:
        uamtk = login_response.json().get('uamtk')
        print(uamtk)
        uamtk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
        uamtk_response = session.post(uamtk_url,data={'appid': 'otn'})
        print(uamtk_response.text)
        newapptk = uamtk_response.json().get('newapptk')
        uamauthclient_url = 'https://kyfw.12306.cn/otn/uamauthclient'
        uamauthclient_response = session.post(uamauthclient_url, data={
            'tk': newapptk
        })
        print(uamauthclient_response.text)
