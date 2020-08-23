import pytest
import os

if __name__ == '__main__':
    args = ['-q', '-s', '--alluredir', 'F:/liequ_aotu_master/raw_files']
    pytest.main(args)
    os.system("allure generate raw_files -o report --clean")

