import json


def read_json():
    with open('../data/datas.json', 'r') as json_file:
        result = json.load(json_file)
        return result


if __name__ == '__main__':
    print(read_json())
