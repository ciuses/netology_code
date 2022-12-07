import requests
from tokenators import ya_api_disk_token as token

class YaUploader:
    link_for_fails = 'https://cloud-api.yandex.net:443/v1/disk/resources/files' # для чего эта ссылка?
    link_for_upload = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    @property
    def head(self) -> dict:
        return {'Authorization': f'OAuth {self.token}', 'Content-Type': 'application/json'}

    def upload_link(self, file_path: str) -> dict:
        param = {'path': file_path, 'overwrite': 'true'}
        resp = requests.get(self.link_for_upload, params=param, headers=self.head)
        if resp.status_code == 200:
            resp_dict = resp.json()
            return resp_dict

        return False

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

    # client = YaUploader(token)
    # client.upload_link(path_to_file)
    # client.upload_filo(path_to_file)
    # client.upload_filo(another_path)

    cli = YaUploader(token)
    cli.upload_filo(another_path)

    #todo сделать загрузку в нужную папку
