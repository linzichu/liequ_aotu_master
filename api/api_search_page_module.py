import json
import pytest
import requests
from api.api_get_host import ApiGetHost


class ApiSearchPageModule(object):
    def __init__(self):
        self.host = ApiGetHost().api_get_host()

    def api_live_search(self, keyword):
        url = self.host + "/api/public/?service=Home.liveSearch"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "keyword": keyword
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    def api_live_search_data(self):
        url = self.host + "/api/public/?service=Home.liveSearch"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": "uid"
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    def api_get_anchor_rank(self):
        url = self.host + "/api/public/?service=Home.getAnchorRank"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "catid": "hotAnchor"
        }
        response = requests.post(url, headers=headers,params=data)
        return response


if __name__ == '__main__':
    r = ApiSearchPageModule().api_get_anchor_rank()
    print(r.json())
