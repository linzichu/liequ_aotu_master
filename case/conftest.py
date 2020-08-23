import json
import pytest
from api import api_login_module


@pytest.fixture()
def action():
    user_datas = api_login_module.ApiLogin().api_user_login("13928962020", "lin33158044")
    user_id = user_datas.json()['data']['info'][0]["id"]
    user_token = user_datas.json()['data']['info'][0]["token"]
    user_data = [user_id, user_token]
    return user_data

    # """with open('F:\liequ_aotu_master/data/datas.json', 'r', encoding="utf-8") as json_file:
    #     result = json.load(json_file)
    #     return result"""


def test_user_data(action):
    print(action)


if __name__ == '__main__':
    pytest.main(['-s', 'conftest.py'])
