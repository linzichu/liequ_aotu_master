from io import BytesIO

import zxing
import requests
from PIL.Image import Image


def qrcode_decode():
    url = "https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2879975435,3793478080&fm=26&gp=0.jpg"
    response = requests.get(url)

    with open("..\image\pic_name.png", "wb") as fp:
        for data in response.iter_content(128):
            # print(data)
            fp.write(data)

    file_name = "..\image\pic_name.png"
    reader = zxing.BarCodeReader()
    qrcode = reader.decode(file_name)
    return qrcode.parsed


if __name__ == '__main__':
    print(qrcode_decode())
