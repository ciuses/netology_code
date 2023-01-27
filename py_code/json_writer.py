import json


def json_writer(info: dict, path: str):
    with open(path, 'w', encoding='utf8') as filo:
        json.dump(info, filo, indent=4, ensure_ascii=False)
        print('Записал')
