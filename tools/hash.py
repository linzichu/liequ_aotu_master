import time
import hashlib


def api_sign(mobile):
    now_time = int(time.time())
    # 拼接签名所需参数
    splice_sign = ("mobile=%s" + "&15776956207194e966c8836a06" + "%s") % (mobile, now_time)
    # 对字符串进行转码
    md5 = hashlib.md5()
    md5.update(splice_sign.encode(encoding="utf-8"))
    sign = md5.hexdigest()
    return sign


if __name__ == '__main__':
    sign = api_sign("13928962030")
    print(sign)
