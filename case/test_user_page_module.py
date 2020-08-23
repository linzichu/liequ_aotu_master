import json
import pytest
import requests
from api.api_get_host import ApiGetHost
from tools.read_image import read_image
from api.api_user_page_module import ApiUserPageModule


class TestUserPageModule(object):
    # 获取用户信息
    def test_get_base_info(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_base_info(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 获取用户昵称
    def test_get_user_information(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_user_information(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 我的关注列表
    def test_get_my_concern_list(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_my_concern_list(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 头像上传
    def test_update_fields(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_update_fields(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 修改用户密码
    @pytest.mark.parametrize('oldpass, pass1, pass2', [['lin33158044', 'lin33158044', 'lin33158044']])
    def test_update_pass(self, oldpass, pass1, pass2, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_update_pass(uid, token, oldpass, pass1, pass2)
        print(result.json())
        assert 200 == result.json()['ret']

    # 添加用户提现账户
    @pytest.mark.parametrize('account, type', [['13928962030', '1']])
    def test_set_user_account(self, action, account, type):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_set_user_account(uid, token, account, type)
        print(result.json())
        assert 200 == result.json()['ret']

    # 我的收益
    def test_get_profit(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_profit(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 获取用户提款账号
    def test_get_user_account_list(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_user_account_list(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 设置提现密码
    def test_set_cash_password(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_set_cash_password(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 会员找回提现密码
    def test_user_find_cash_pass(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_user_find_cash_pass(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 用户提现
    def test_set_cash(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_set_cash(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 删除提现账户
    def test_del_user_account(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_del_user_account(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 充值记录
    def test_recharge_record(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_recharge_record(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 提现记录
    def test_with_drawals_record(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_with_drawals_record(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 粉丝列表
    def test_get_fans_list(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_fans_list(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 直播明细
    def test_live_broad_cast_details(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_live_broad_cast_details(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 礼物明细
    def test_gift_details(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_gift_details(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 关注主播
    def test_set_attent(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_set_attent(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']

    # 我的趣豆
    def test_get_balance(self, action):
        uid = action[0]
        token = action[1]
        result = ApiUserPageModule().api_get_balance(uid, token)
        print(result.json())
        assert 200 == result.json()['ret']


if __name__ == '__main__':
    pytest.main(['-s', 'test_user_page_module.py'])
