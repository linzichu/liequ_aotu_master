import json
import requests
from api.api_get_host import ApiGetHost
import os


class ApiHomeModule(object):
    def __init__(self):
        self.host = "http://liequ.czhepeng.cn:8888/"

    # 验证配置文件
    def api_get_config(self):
        url = self.host + "/api/public/?service=Home.getConfig"
        headers = {"Content-type": "application/json/utf-8"}
        response = requests.get(url, headers)
        return response

    # 获取首页全部信息
    def api_get_all_data(self):
        url = self.host + "/api/public/?service=Home.GetAllData"
        # url = + "/api/public/?service=Home.GetAllData"
        headers = {"Content-type": "application/json/utf-8"}
        response = requests.get(url, headers)
        result = json.dumps(response.json())
        return result

    # 获取最新主播
    def api_get_new(self):
        url = self.host + "/api/public/?service=Home.GetNew"
        headers = {"Content-type": "application/json/utf-8"}
        response = requests.get(url, headers)
        return response

    # 获取热门主播
    def test_get_hot(self):
        url = self.host + "/api/public/?service=Home.getHot"
        headers = {"Content-type": "application/json/utf-8"}

        response = requests.get(url, headers=headers)
        return response

    # 获取新分类
    def api_get_class_live_new(self, liveclassid):
        url = self.host + "/api/public/?service=Home.getClassLiveNew"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "liveclassid": liveclassid
        }
        response = requests.post(url, headers=headers, params=data)
        return response


if __name__ == '__main__':
    # result = ApiHomeModule().api_get_all_data()
    # print(result)
    path = os.path.abspath(__file__)
    print(path)
