month = input('Ввведите Ваш месяц рождения? (например Ноябрь)\n').lower()
day = int(input('Укажите день Вашего раждения? (например 28)\n'))

if month == 'январь':
    if day in range(1, 21):
        print('Ваш знак зодиака Козерог')
    elif day in range(21, 32):
        print('Ваш знак зодиака Водолей')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'февраль':
    if day in range(1, 19):
        print('Ваш знак зодиака Водолей')
    elif day in range(19, 29):
        print('Ваш знак зодиака Рыбы')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'март':
    if day in range(1, 21):
        print('Ваш знак зодиака Рыбы')
    elif day in range(21, 32):
        print('Ваш знак зодиака Овен')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'апрель':
    if day in range(1, 20):
        print('Ваш знак зодиака Овен')
    elif day in range(20, 31):
        print('Ваш знак зодиака Телец')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'май':
    if day in range(1, 21):
        print('Ваш знак зодиака Телец')
    elif day in range(21, 32):
        print('Ваш знак зодиака Близнецы')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'июнь':
    if day in range(1, 22):
        print('Ваш знак зодиака Близнецы')
    elif day in range(22, 31):
        print('Ваш знак зодиака Рак')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'июль':
    if day in range(1, 23):
        print('Ваш знак зодиака Рак')
    elif day in range(23, 32):
        print('Ваш знак зодиака Лев')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'август':
    if day in range(1, 23):
        print('Ваш знак зодиака Лев')
    elif day in range(23, 32):
        print('Ваш знак зодиака Дева')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'сентябрь':
    if day in range(1, 23):
        print('Ваш знак зодиака Дева')
    elif day in range(23, 31):
        print('Ваш знак зодиака Весы')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'октябрь':
    if day in range(1, 24):
        print('Ваш знак зодиака Весы')
    elif day in range(24, 32):
        print('Ваш знак зодиака Скорпион')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'ноябрь':
    if day in range(1, 23):
        print('Ваш знак зодиака Скорпион')
    elif day in range(23, 31):
        print('Ваш знак зодиака Стрелец')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

elif month == 'декабрь':
    if day in range(1, 22):
        print('Ваш знак зодиака Стрелец')
    elif day in range(22, 32):
        print('Ваш знак зодиака Козерог')
    else:
        print(f'Такой даты {day} в этом месяце нет.')

else:
    print(f'Такой месяца {month} несуществует.')
