import time
import requests
from api.api_get_host import ApiGetHost
from tools.hash import api_sign


class ApiGetCode(object):
    def __init__(self):
        self.host = ApiGetHost().api_get_host()
        self.now_time = int(time.time())
        self.session = requests.session()

    # 登录验证码
    def api_get_login_code(self, mobile):
        # 实例化加密函数
        sign = api_sign(mobile)
        url = self.host + "/api/public/?service=Login.getLoginCode"
        # 获取验证码参数
        data = {
            "mobile": mobile,
            "sign": sign,
            "time": self.now_time
        }
        response = self.session.post(url=url, params=data)
        # print(response.json())
        return [response.cookies.get_dict(), response]

    # 忘记密码验证码
    def api_get_forget_code(self, mobile):
        # 实例化加密函数
        sign = api_sign(mobile)
        url = self.host + "/api/public/?service=Login.getForgetCode"
        # 获取验证码参数
        data = {
            "mobile": mobile,
            "sign": sign,
            "time": self.now_time
        }
        response = self.session.post(url=url, params=data)
        return [response.cookies.get_dict(), response]

    # 注册验证码
    def api_get_logon_code(self, mobile):
        # 实例化加密函数
        sign = api_sign(mobile)
        url = self.host + "/api/public/?service=Login.getCode"
        # 获取验证码参数
        data = {
            "mobile": mobile,
            "sign": sign,
            "time": self.now_time
        }
        response = self.session.post(url=url, params=data)
        return [response.cookies.get_dict(), response]

    # 获取重置密码验证码
    def api_get_cash_password_code(self, uid, token, mobile):
        sign = api_sign(mobile)
        url = self.host + "/api/public/?service=User.getCashPasswordCode"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "mobile": mobile,
            "sign": sign,
            "time": self.now_time
        }
        response = requests.post(url, headers=headers, params=data)
        return [response.cookies.get_dict(), response]


if __name__ == '__main__':
    r = ApiGetCode().api_get_login_code('13928962020')
    print(r[1])
