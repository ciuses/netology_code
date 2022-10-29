ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

#ленивый вариант
# my_list = []
# for my_value in ids.values():
#        my_list += my_value
# print(list(set(my_list)))

unic_id = set([
       geo_id
       for my_value in ids.values()
       for geo_id in my_value
])
print(list(unic_id))