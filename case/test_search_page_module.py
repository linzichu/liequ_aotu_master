import json
import pytest
import requests
from api.api_search_page_module import ApiSearchPageModule


class TestSearchModule:
    @pytest.mark.parametrize('keyword', ['阿'])
    def test_live_search(self, keyword):
        result = ApiSearchPageModule().api_live_search(keyword)
        assert 200 == result.json()['ret']

    def test_live_search_data(self):
        result = ApiSearchPageModule().api_live_search_data()
        assert 200 == result.json()['ret']

    def test_get_anchor_rank(self):
        result = ApiSearchPageModule().api_get_anchor_rank()
        assert 200 == result.json()['ret']


if __name__ == '__main__':
    pytest.main(['-s', 'test_search_page_module.py'])
