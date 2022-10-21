base_rate = 10

far_east = ['анадырь', 'благовещенск', 'биробиджан', 'владивосток', 'комсомольск-на-амуре', 'магадан',
            'петропавловск-камчатский', 'хабаровск', 'южно-сахалинск', 'якутск']

children_bonus = 0
salary_bonus = 0
insurance_bonus = 0

city = input('Ввведите Ваш город регистрации:(например Хабаровск)\n').lower()
amount_of_children = int(input('Укажите количество детей? (например 2)\n'))
salary_project = input('Являетесь ли Вы нашим клиентом по зарплатному проекту? (да\нет)\n').lower()
insurance = input('Нужна ли Вам страховка? (да\нет)\n').lower()

if city in far_east:
    base_rate = 2
    print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

else:

    if amount_of_children > 3 and salary_project == 'да' and insurance == 'да':
        children_bonus = 1
        salary_bonus = 0.5
        insurance_bonus = 1.5

    elif salary_project == 'да' and insurance == 'да':
        salary_bonus = 0.5
        insurance_bonus = 1.5

    elif amount_of_children > 3:
        children_bonus = 1

    elif salary_project == 'да':
        salary_bonus = 0.5

    elif insurance == 'да':
        insurance_bonus = 1.5

    print(f'Ваша базовая ставка по ипотеке будет {base_rate - children_bonus - salary_bonus - insurance_bonus}%')
