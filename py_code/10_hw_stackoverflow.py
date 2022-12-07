import json
import requests


link = 'https://api.stackexchange.com/2.3/questions'
params = {'fromdate': '1670284800', 'tagged': 'python', 'site': 'stackoverflow'}

response = requests.get(link, params=params)
my_dict = response.json()
questions_dict = {}
for all_info in my_dict['items']:
    questions_dict[all_info['title']] = all_info['link'], all_info['tags']


for k, v in questions_dict.items():
    print(k, v)