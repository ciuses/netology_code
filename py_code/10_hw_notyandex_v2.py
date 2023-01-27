import requests
from tokenators import ya_api_disk_token as token

# link_for_upload = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'

# head = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}


def upload_link(file_path: str) -> dict:
    head = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}
    param = {'path': file_path, 'overwrite': 'true'}
    resp = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload', headers=head, params=param,)
    print(resp)
    resp_dict = resp.json()
    return resp_dict



def upload_filo(file_path: str):
    href = upload_link(file_path).get('href')
    with open(file_path, 'rb') as filo:
        resp = requests.put(href, data=filo)
        print(resp.text, resp.status_code)


def all_in_one(filo, ya_name):
    head = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}
    param = {'path': f'disk:/Netology/{ya_name}', 'overwrite': 'true'} # нужен полный путь к файлу с его названием
    resp = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload', headers=head, params=param)
    # print(resp, resp.text)
    resp_dict = resp.json()
    special_link = resp_dict.get('href')
    with open(filo, 'rb') as filo:
        resp = requests.put(special_link, data=filo)
        print(resp.text, resp.status_code)



def new_dir(dir_name):

    head = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}
    param = {'path': dir_name}
    resp = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources', headers=head, params=param)
    print(resp)



if __name__ == '__main__':
    # dict_with_info = upload_link('неселф.png')
    # # print(dict_with_info)
    # link = dict_with_info['href']
    # print(link)
    # upload_filo('recipes.txt')
    all_in_one('неселф.png')
    # new_dir('new_dir')


    # link2 = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    # head = {'Authorization': f'OAuth {token}', 'Content-Type': 'application/json'}
    # par = {'path': 'netology'}
    # resp = requests.get(link2, headers=head, params=par)
    # di = resp.json()
    # print(resp, di)
    # print(token)





