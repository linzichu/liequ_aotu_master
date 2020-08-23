import json
import pytest
import requests
from api.api_get_host import ApiGetHost
from tools.read_image import read_image


class ApiUserPageModule(object):
    def __init__(self):
        self.host = ApiGetHost().api_get_host()

    # 获取用户信息
    def api_get_base_info(self, uid, token):
        url = self.host + "/api/public/?service=User.getBaseInfo"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 获取用户昵称
    def api_get_user_information(self, uid, token):
        url = self.host + "/api/public/?service=User.getUserInformation"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 我的关注列表
    def api_get_my_concern_list(self, uid, token):
        url = self.host + "/api/public/?service=User.getMyConcernList"
        headers = {"Content-type": "application/json/utf-8"}

        data = {
            "uid": uid,
            "token": token
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 头像上传
    def api_update_fields(self, uid, token):
        url = self.host + "/api/public/?service=User.updateFields"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "fields": {'fields': ("pic_name.png", open("F:\liequ_aotu_master/image/pic_name.png", 'rb'), 'image/png')}
        }

        response = requests.post(url, headers=headers, params=data)
        return response

    # 修改用户密码
    def api_update_pass(self, uid, token, oldpass, pass1, pass2):
        url = self.host + "/api/public/?service=User.updatePass"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "oldpass": oldpass,
            "pass": pass1,
            "pass2": pass2
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 添加用户提现账户
    def api_set_user_account(self, uid, token, account, type):  # , account_bank, type, wx_mobile):
        url = self.host + "/api/public/?service=User.SetUserAccount"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "account": account,
            # "name": name,
            # "account_bank": account_bank,
            "type": type
            # "wx_mobile": wx_mobile
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 我的收益
    def api_get_profit(self, uid, token):
        url = self.host + "/api/public/?service=User.getProfit"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 获取用户提款账号
    def api_get_user_account_list(self, uid, token):
        url = self.host + "/api/public/?service=User.GetUserAccountList"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 设置提现密码
    def api_set_cash_password(self, uid, token):
        url = self.host + "/api/public/?service=User.setCashPassword"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "pass": '8888',
            "pass2": '8888'
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 会员找回提现密码
    def api_user_find_cash_pass(self, uid, token):
        url = self.host + "/api/public/?service=User.userFindCashPass"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "user_login": '13928962020',
            "user_pass": 'lin33158044',
            "user_pass2": 'lin33158044',
            "code": '123456'
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 用户提现
    def api_set_cash(self, uid, token):
        url = self.host + "/api/public/?service=User.setCash"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "accountid": '323',
            "cash_amount": '13928962020',
            "user_pass": '8888'
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 删除提现账户
    def api_del_user_account(self, uid, token):
        url = self.host + "/api/public/?service=User.delUserAccount"
        headers = {"Content-type": "application/json/utf-8"}
        response = ApiUserPageModule().api_get_user_account_list(uid, token)
        r_id = response.json()['data']['info'][0]['id']
        data = {
            "uid": uid,
            "token": token,
            "id": r_id,
            "user_pass": '8888',
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 充值记录
    def api_recharge_record(self, uid, token):
        url = self.host + "/api/public/?service=User.rechargeRecord"
        headers = {"Content-type": "application/json/utf-8"}

        data = {
            "uid": uid,
            "token": token
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 提现记录
    def api_with_drawals_record(self, uid, token):
        url = self.host + "/api/public/?service=User.withdrawalsRecord"
        headers = {"Content-type": "application/json/utf-8"}

        data = {
            "uid": uid,
            "token": token
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 粉丝列表
    def api_get_fans_list(self, uid, token):
        url = self.host + "/api/public/?service=User.getFansList"
        headers = {"Content-type": "application/json/utf-8"}

        data = {
            "uid": uid,
            "token": token,
            "touid": uid
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 直播明细
    def api_live_broad_cast_details(self, uid, token):
        url = self.host + "/api/public/?service=User.LiveBroadcastDetails"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 礼物明细
    def api_gift_details(self, uid, token):
        url = self.host + "/api/public/?service=User.giftDetails"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "showid": '1'
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 关注主播
    def api_set_attent(self, uid, token):
        url = self.host + "/api/public/?service=User.setAttent"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
            "touid": uid
        }
        response = requests.post(url, headers=headers, params=data)
        return response

    # 我的趣豆
    def api_get_balance(self, uid, token):
        url = self.host + "/api/public/?service=User.getBalance"
        headers = {"Content-type": "application/json/utf-8"}
        data = {
            "uid": uid,
            "token": token,
        }
        response = requests.post(url, headers=headers, params=data)
        return response


if __name__ == '__main__':
    r = ApiUserPageModule().api_update_fields('208', '04ad1a58898e12ab7c7e07c338a6e717')
    # r1 = ApiUserPageModule().api_get_user_account_list('208', '04ad1a58898e12ab7c7e07c338a6e717')
    print(r.json())
    # print(r1.json())
