stats = {'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
stats2 = {'zzzz': 56565, 'yandex': 120, 'vk': 115, 'email': 42, 'ok': 98}

# max_sales = [
#     my_key
#     for my_key, my_value in stats.items()
#     if my_value == max(stats.values())
# ]

# print(max_sales[0])

# альтернативное решение
# for company, any_digit in stats.items():
#     if any_digit == max(stats.values()):
#         print(company, any_digit)


print(max(stats2)) # берёт по ascii символам
print(max(stats2.values()))
