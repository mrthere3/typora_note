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
