boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Идеальные пары:')
    boys.sort()
    girls.sort()
    for row in zip(boys, girls):
        boy, girl = row
        print(f'{boy} и {girl}')

else:
    print(f'Количество мальчиков {len(boys)} и девочек {len(girls)} не совпадают!')
