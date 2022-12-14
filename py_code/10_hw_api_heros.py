import requests

base = 'https://akabab.github.io/superhero-api/api'
all = f'{base}/all.json'

def get_name_and_id(hero_name: str) -> tuple:
    resp = requests.get(all)
    hero_id = {hero_card['name']: hero_card['id'] for hero_card in resp.json()}
    for name, hero_id in hero_id.items():
        if name == hero_name:
            return (name, hero_id)


def get_power(hero_info: tuple) -> dict:
    power = f'{base}/powerstats/{hero_info[1]}.json'
    resp = requests.get(power)
    return resp.json()


def intelligence_selection(list_of_names: list):
    mind_list = []

    for name in list_of_names:
        hero_info = get_name_and_id(name)
        hero_power = get_power(hero_info)
        mind_list.append((hero_power['intelligence'], name))

    return max(mind_list)


print(intelligence_selection(['Hulk', 'Captain America', 'Thanos']))
print(intelligence_selection(['Alfred Pennyworth', 'Batman', 'Deadpool']))
