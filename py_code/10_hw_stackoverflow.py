import requests


link = 'https://api.stackexchange.com/2.3/questions'
params = {'fromdate': '1670284800', 'tagged': 'python', 'site': 'stackoverflow'}

response = requests.get(link, params=params)
my_dict = response.json()

for all_info in my_dict['items']:
    print(all_info['title'])
    print(all_info['tags'])
    print(all_info['link'])