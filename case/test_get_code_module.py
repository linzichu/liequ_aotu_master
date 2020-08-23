import pytest
from api.api_get_code_module import ApiGetCode
import time


class TestGetCodeModule:
    @pytest.mark.parametrize('mobile', ['13928962030'])
    def test_get_login_code(self, mobile):
        result = ApiGetCode().api_get_login_code(mobile)[1]
        assert 200 == result.json()['ret']

    @pytest.mark.parametrize('mobile', ['13928962030'])
    def test_get_logon_code(self, mobile):
        time.sleep(1)
        result = ApiGetCode().api_get_logon_code(mobile)[1]
        assert 200 == result.json()['ret']

    @pytest.mark.parametrize('mobile', ['13928962030'])
    def test_get_forget_code(self, mobile):
        time.sleep(1)
        result = ApiGetCode().api_get_forget_code(mobile)[1]
        assert 200 == result.json()['ret']


if __name__ == '__main__':
    pytest.main(['-q', 'test_get_code_module.py'])
