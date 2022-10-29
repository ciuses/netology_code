stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max_sales = [
    my_key
    for my_key, my_value in stats.items()
    if my_value == max(stats.values())
]

print(max_sales[0])