import requests

def get_questions(tag: str) -> object:
    link = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': '1670284800', 'tagged': tag, 'site': 'stackoverflow'}
    response = requests.get(link, params=params)
    if response.status_code == 200:
        my_dict = response.json()
        questions_dict = {}
        for all_info in my_dict['items']:
            questions_dict[all_info['title']] = all_info['link'], all_info['tags']
        return questions_dict
    else:
        return response.status_code


if __name__ == '__main__':

    for k, v in get_questions('python').items():
        print(k, v)

    # TODO Подачу даты времени ввиде эпохи Unix из 1670284800 в Tue Dec  6 07:00:00 2022 print(time.ctime(1670284800))
