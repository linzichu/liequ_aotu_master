import pytest
from api.api_get_host import ApiGetHost


class TestGetHost:
    def test_get_host(self):
        response_host = ApiGetHost().api_get_host()
        assert "https://" in response_host


if __name__ == '__main__':
    pytest.main(['-s', 'test_get_host.py'])
