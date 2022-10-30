from collections import defaultdict

row_list = ['2018-01-01', 'yandex', 'cpc', 100]

# new_dict = {}
# for el in row_list:
#     new_dict[el] = el
# print(new_dict)


# super_dict = {item: item for item in row_list}
# print(super_dict)

# super_dict = {item: {item: {item: item}} for item in row_list}
# print(super_dict)


# new_dict = {}
#
# for element in row_list:
#     new_dict[element] = element
#
# print(new_dict)

# new_dict = {}
# while row_list:
#     item = row_list.pop()
#     new_dict[item] = {}
#     print(new_dict.get())
#
#
# print(new_dict)

# new_dict = {}
# new_dict['пыса'] = {'жопа': {'мандарин': {'ицо': 'тухлое'}}}
# print(new_dict)
#
# print(new_dict['пыса']['жопа']['мандарин'])

# a_di = {}
# a_di = {'пыса': 'пыса'}
# a_di['пыса'] = {'жопа': 'жопа'}
# a_di['пыса']['жопа'] = {'мандарин': 'мандарин'}
# a_di['пыса']['жопа']['мандарин'] = {'ицо': 'тухлое'}
#
# print(a_di)

# почти рабочий вариант
# sup_di = {}
# for element in row_list:
#     sup_di = {element: sup_di}
#
#
# print(sup_di)

sup_di = {}
for element in row_list[::-1]:
    sup_di = {element: sup_di}


print(sup_di)