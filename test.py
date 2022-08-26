# -*- coding:utf-8 -*-
import random
from hashlib import md5

import requests
class CJY(object):

    @staticmethod
    def cjy_handler(captcha_img: [str, bytes]):
        """
        :param captcha_img:
        :return:
        """
        cjy_client = CJY('interfacesystem', 'interfacesystem', '96001')
        if isinstance(captcha_img, str):
            with open(captcha_img, 'rb') as f:
                img = f.read()  # 将验证码图片读到内存
        else:
            img = captcha_img
        captcha_result = cjy_client.PostPic(img, 6001)  # 6001 验证码类型
        return captcha_result.get("pic_str")

    def __init__(self, username, password, soft_id):
        """
        :param username:
        :param password:
        :param soft_id:
        """
        self.username = username
        password = password.encode('utf8')

        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

    def get_captcha(self, captcha_img: [str, bytes]):
        if isinstance(captcha_img, str):
            with open(captcha_img, 'rb') as f:
                img = f.read()  # 将验证码图片读到内存
        else:
            img = captcha_img
        captcha_result = self.PostPic(img, 6001)  # 6001 验证码类型
        captcha = captcha_result.get("pic_str")
        return captcha


cjy_client = CJY('interfacesystem', 'interfacesystem', '96001')
numberslist = []
l = list()
for i in range(256):
    l.append(hex(i+256)[3:]) # 生成16进制的字符串并且进行切割
    # print(l)
def creatnumlist():
    import secrets # 区别于别的方法 console.log(window.crypto.getRandomValues(new Uint32Array(4)).join('')) 所产生 的数组进行二进制熵值计算
    randValue = [secrets.randbits(8) for i in range(16)]
    print(randValue)
    return randValue
def creatuuid(t,l):
    e = 0 # 偏移量
    i = (l[t[e + 0]] + l[t[e + 1]] + l[t[e + 2]] + l[t[e + 3]] + "-" + l[t[e + 4]] + l[t[e + 5]] + "-" + l[t[e + 6]] + l[
        t[e + 7]] + "-" + l[t[e + 8]] + l[t[e + 9]] + "-" + l[t[e + 10]] + l[t[e + 11]] + l[t[e + 12]] + l[t[e + 13]] +
     l[t[e + 14]] + l[t[e + 15]]).lower()
    return i
def maincode():
    n = creatnumlist()
    n[6] = 5 & (n[6]) | 64
    n[8] = 63 & n[8] | 128
    return(creatuuid(n,l))

def mainpassword(pwd):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("12345678"))
    print(m.hexdigest())

def reuqestlogin():
    import requests
    code = maincode()
    url = "https://v2.kp.newtimeai.com/login/getVerificationCode?code="+code
    yzm = cjy_client.get_captcha(requests.get(url).content)
    headers = {
        'authority': 'v2.kp.newtimeai.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,hu;q=0.5',
        'cache-control': 'no-cache',
        'origin': 'https://ep.newtimeai.com',
        # "Content-Type":"application/x-www-form-urlencoded",
        'pragma': 'no-cache',
        'referer': 'https://ep.newtimeai.com/',
        'request-end': 'web',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sybs': 'null',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
    }

    data = {
        'czydm': 'manchen',
        'yhkl': '25d55ad283aa400af464c76d713c07ad',
        'yzm': yzm,
        'code': code,
    }
    print(data)
    response = requests.post('https://v2.kp.newtimeai.com/login/userlogin', headers=headers, data=data)
    print(response.json())




if __name__ == '__main__':
    reuqestlogin()



