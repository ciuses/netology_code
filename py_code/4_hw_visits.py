geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# russian_list = [
#     {my_key: my_value} for row in geo_logs
#     for my_key, my_value in row.items()
#     if my_value[1] == 'Россия'
# ]

russian_list = []

for st in geo_logs:
    el = st.values()
    print(type(el), el['one'])

    # for k, v in st.items():
    #     # print(k, v[1])
    #     if 'Россия' in v[-1]:
    #         russian_list.append(st)

for element in russian_list:
    print(element)
