from api.api_get_host import ApiGetHost
from api.api_get_code_module import ApiGetCode
import json
import requests


class ApiLogin(object):
    def __init__(self):
        self.host = ApiGetHost().api_get_host()
        self.session = ApiGetCode().session

    def api_user_login(self, user_login, user_pass):
        url = self.host + "/api/public/?service=Login.userLogin"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "user_login": user_login,
            "user_pass": user_pass,
        }
        response = self.session.post(url, headers=headers, params=data)
        # 将登陆信息保存到本地文件/data/datas.json
        with open('F:\liequ_aotu_master/data/datas.json', 'w') as fp:
            fp.write(json.dumps(response.json(), indent=4))
            fp.close()
        return response

    def api_code_login(self, mobile):
        url = self.host + "/api/public/?service=Login.userLoginBySms"
        get_session = ApiGetCode().api_get_login_code(mobile)
        code = input('请输入验证码: ')
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "user_login": mobile,
            "code": code,
        }
        response = requests.post(url, headers=headers, params=data, cookies=get_session)
        print(response.json())


if __name__ == '__main__':
    print(ApiLogin().api_user_login('13928962020', 'lin33158044'))
