import requests
from api.api_get_host import ApiGetHost
from tools.read_image import read_image


class ApiShortClipModule(object):
    def __init__(self):
        self.host = ApiGetHost().api_get_host()

    def api_get_video_list(self, uid, token):
        url = self.host + "/api/public/?service=User.GetVideoList"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token
        }
        response = requests.post(url, headers=headers, params=data)
        return response


if __name__ == '__main__':
    r = ApiShortClipModule().api_get_video_list('208', '04ad1a58898e12ab7c7e07c338a6e717')
    print(r.json())
