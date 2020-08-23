import requests
import base64


def read_image():
    url = "https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2879975435,3793478080&fm=26&gp=0.jpg"
    response = requests.get(url)
    for i in response.iter_content(128):
        return i


if __name__ == '__main__':
    print(read_image())
