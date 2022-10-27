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
    if len(boys) > len(girls):
        print(f'Нехватает {len(boys) - len(girls)} девочек!')
    else:
        print(f'Нехватает {len(girls) - len(boys)} мальчиков!')
