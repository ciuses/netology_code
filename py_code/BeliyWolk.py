# a = 10 + 20
# b = a * 30
# c = a / b
# print('Ответ:', c)

# c = x+y
# print(c)

# x=20

# print(2>1)

# print(3<5)

# print(5!=5)

# print(3<=4)

# print(8.0==8)

# print(8>=6)

# print(5!=8)

# print(3 < 5 > 8)
# print(3 < 5 and 5 < 8)

# my_comp = 8 >= 6
# print(my_comp)

# print(ord(' '),'AAAK' < 'cda')
# print(len('AAAK'))

# print(True and True)
# print(True and False)

# print(True or False)
# print(False or False)

# print(not False)

# print((5<7) and (3>8))
# print(4 > 2 and (6 > 5 or 4 < 3))
# print((((not(9 > 7)) or (4 < 2 and 6 > 5)) or 4 >3))
# print(not(9 > 7))
# print(4 < 2 and 6 > 5)
print(4 < 2)
print(6 > 5)
print(0 * 1)
# print(((not(9 > 7)) or (4 < 2 and 6 > 5)))
# print(((not(9 > 7) or 4 < 2 and 6 > 5) or 4 >3))

# print((not(9 > 7) or 4 < 2) and (6 > 5 or 4 >3))
# print(bool(123456789))

bogatyr_health = input('Введите здоров или болен богатырь: ')
if bogatyr_health =='здоров':
	print('Соловей-разбойник побежден!')


bogatyr_health = input('Введите здоров или болен богатырь: ')
if bogatyr_health =='здоров':
  print('Соловей-разбойник побежден!')
else:
	print('Соловей-разбойник может победить!')

bogatyr_health = input('Введите здоров или болен богатырь: ')
if bogatyr_health == 'здоров':
    print('Соловей-разбойник побежден!')
    experience = 'вырос'
else:
    # print('Соловей-разбойник может победить!')
    experience = 'снизился'

chance_to_win = 0
bogatyr_health = int(input('Введите процент здоровья богатыря от 0 до 100: '))
if bogatyr_health >= 100:
    chance_to_win = 100
else:
    sword_length = int(input('Вес меча богатыря: '))
    presence_tooth = input('Есть у Соловья-разбойника зуб(да/нет) ').lower()
    weapon = int(input('Вес брони: '))

    if 5 <= sword_length < 8:
        chance_to_win += 40
        # chance_to_win = chance_to_win + 40
    elif presence_tooth == 'да':
        chance_to_win -= 50
    elif 10 < weapon < 30:
        chance_to_win += 70

print('Вероятность победы богатыря:', chance_to_win, 'процентов')

##################################################################
age = int(input('Введите возраст богатыря: '))
town = input('Введите город проживания: ').capitalize()
if age < 18:
    print('Отправьте ребенка домой!')
else:
    if (town == 'Муром' and age <= 33) or (town == 'Киев' and age > 33):
        print(town, 'Илья Муромец')
    elif town == 'Новгород' and 20 <= age <= 30:
        print(town, 'Никита Кожемяка')
    elif town == 'Ростов' and 18 <= age <= 25:
        print(town, 'Алеша Попович')
    else:
        print('Такого богатыря не существовало!')

a = 33
c = 18
b = 16
if a == 33:
    b = 34
    if c > b:
        c = b
    else:
        c = 35
print(a, b, c)
result = 31
print(result * '#')
