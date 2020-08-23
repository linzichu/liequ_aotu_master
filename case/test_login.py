import pytest
from api.api_login_module import ApiLogin


class TestLogin:
    @pytest.mark.parametrize("user_login,password", [['13928962030', '12345x']])
    def test_user_login(self, user_login, password):
        result = ApiLogin().api_user_login(user_login, password)
        assert 200 == result.json()['ret']


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py', '--html=../report/test.html'])
