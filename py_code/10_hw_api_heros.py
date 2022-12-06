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

# r2 = requests.get(all)
# print(r2.text)

# with open('other\\heros.json', 'w', encoding='utf8') as filo:
#     json.dump(r2.json(), filo, indent=4, ensure_ascii=False)


def get_name_and_id(hero_name:str) -> tuple:
    resp = requests.get(all)
    hero_id = {hero_card['name']: hero_card['id'] for hero_card in resp.json()}
    for name, hero_id in hero_id.items():
        if name == hero_name:
            return (name, hero_id)


print(get_name_and_id('Thanos'))

def get_power(hero_info:tuple) -> dict:
    power = f'{base}/powerstats/{hero_info[1]}.json'
    resp = requests.get(power)
    return resp.json()

print(get_power(get_name_and_id('Thanos')))


def intelligence_selection(list_of_names: list):

    mind_list = []

    for name in list_of_names:
        hero_info = get_name_and_id(name)
        hero_power = get_power(hero_info)
        mind_list.append(hero_power['intelligence'])
        print(hero_power['intelligence'])


    print(mind_list)
    return max(mind_list)


intelligence_selection(['Hulk', 'Captain America', 'Thanos'])
print(intelligence_selection(['Hulk', 'Captain America', 'Thanos']))