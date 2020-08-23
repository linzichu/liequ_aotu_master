import json
import pytest
import requests
from api.api_home_module import ApiHomeModule


class TestHomeModule:
    # 验证配置文件
    def test_get_config(self):
        result = ApiHomeModule().api_get_config()
        assert 200 == result.json()['ret']

    # 获取首页全部信息
    def test_get_all_data(self):
        result = ApiHomeModule().api_get_all_data()
        assert 200 == result.json()['ret']

    # 获取最新主播
    def test_get_new(self):
        result = ApiHomeModule().api_get_new()
        assert 200 == result.json()['ret']

    # 获取热门主播
    def test_get_hot(self):
        result = ApiHomeModule().test_get_hot()
        assert 200 == result.json()['ret']

    # 获取新分类
    @pytest.mark.parametrize('liveclassid', ['13'])
    def test_get_class_live_new(self, liveclassid):
        result = ApiHomeModule().api_get_class_live_new(liveclassid)
        assert 200 == result.json()['ret']


if __name__ == '__main__':
    pytest.main(['-s', 'test_home_module.py'])
