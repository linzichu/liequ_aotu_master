import requests
import json


class ApiGetHost(object):
    def __init__(self):
        self.session = requests.session()

    def api_get_host(self):
        url = "https://liequ.tv/api/public/?service=Home.getDomainName"
        response = self.session.get(url)
        r_host = response.json()["data"]['info']['domain_name']
        r_host_t = response.text
        return r_host

    # @property
    # def read_datas(self):
    #     with open('../data/datas.json', 'r', encoding="utf-8") as json_file:
    #         result = json.load(json_file)
    #         return result


if __name__ == '__main__':
    r = ApiGetHost().api_get_host()
    print(r)
