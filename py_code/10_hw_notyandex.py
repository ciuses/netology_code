import requests
import json
from tokenators import ya_api_disk_token as token


# link = 'https://cloud-api.yandex.net:443/v1/disk'
# link2 = 'https://cloud-api.yandex.net:443/v1/disk/resources'
#
# head = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}
# par = {'path': 'netology'}
# resp = requests.get(link2, headers=head, params=par)
# di = resp.json()
# print(resp, di)
# # print(token)

# with open('other\\heros.json', 'w', encoding='utf8') as filo:
#     json.dump(r2.json(), filo, indent=4, ensure_ascii=False)

class YaUploader:
    link_for_fails = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
    link_for_upload = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    @property
    def head(self) -> dict:
        return {'Authorization': f'OAuth {self.token}', 'Content-Type': 'application/json'}

    def upload_link(self, file_path: str) -> dict:
        param = {'path': file_path, 'overwrite': 'true'}
        resp = requests.get(self.link_for_upload, params=param, headers=self.head)
        resp_dict = resp.json()
        print(resp_dict)
        return resp_dict

    def upload_filo(self, file_path: str):
        href = self.upload_link(file_path).get('href')
        if not href:
            return
        with open(file_path, 'rb') as filo:
            resp = requests.put(href, data=filo)
            if resp.status_code == 201:
                print('Загружено')
                return True
            print(f'Неудача при загрузке {resp.status_code}')
            return False


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'other\\final_filo.txt'
    another_path = 'неселф.png'
    # token = ...
    # uploader = YaUploader(token)
    # result = uploader.upload(path_to_file)

    client = YaUploader(token)
    # client.upload_link(path_to_file)
    # client.upload_filo(path_to_file)
    client.upload_filo(another_path)
