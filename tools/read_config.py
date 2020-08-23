import os
import configparser

# os.path.realpath：获取当前执行脚本的绝对路径。
# os.path.split：如果给出的是一个目录和文件名，则输出路径和文件名
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "server.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_http(self, param):
        value = self.cf.get("HTTP", param)
        return value

    def get_db(self, param):
        value = self.cf.get("DATABASE", param)
        return value


if __name__ == '__main__':
    test = ReadConfig()
    LocalIp = test.get_http('')
    print(LocalIp)
    # print(configPath)
    # print(proDir)