base_rate = 10

far_east = ['анадырь', 'благовещенск', 'биробиджан', 'владивосток', 'комсомольск-на-амуре', 'магадан',
            'петропавловск-камчатский', 'хабаровск', 'южно-сахалинск', 'якутск']

city = input('Ввведите Ваш город регистрации:(например Хабаровск)\n').lower()
amount_of_children = int(input('Укажите количество детей? (например 2)\n'))
salary_project = input('Являетесь ли Вы нашим клиентом по зарплатному проекту? (да\нет)\n').lower()
insurance = input('Нужна ли Вам страховка? (да\нет)\n').lower()

if city in far_east:
    base_rate = 2
    print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

else:

    if amount_of_children > 3:
        base_rate -= 1

        if salary_project == 'да':
            base_rate -= 0.5

            if insurance == 'да':
                base_rate -= 1.5
                print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

            else:
                print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

        else:
            print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')


    else:

        if salary_project == 'да':
            base_rate -= 0.5

            if insurance == 'да':
                base_rate -= 1.5
                print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

            else:
                print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

        else:

            if insurance == 'да':
                base_rate -= 1.5
                print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')

            else:
                print(f'Ваша базовая ставка по ипотеке будет {base_rate}%')
