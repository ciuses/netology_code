import json

import requests

base = 'https://akabab.github.io/superhero-api/api'
all = f'{base}/all.json'
first = f'{base}/id/17.json'
power = f'{base}/powerstats/17.json'
appearance = f'{base}/appearance/17.json'
bio = f'{base}/biography/17.json'
connections = f'{base}/connections/17.json'
work = f'{base}/work/17.json'

r2 = requests.get(all)
# print(r2.text)


with open('other\\heros.json', 'w', encoding='utf8') as filo:
    json.dump(r2.json(), filo, indent=4, ensure_ascii=False)
