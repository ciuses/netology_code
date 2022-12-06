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

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)