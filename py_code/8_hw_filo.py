def recipe_from_file(path: str) -> dict:

    filo = open(path, 'rt', encoding='utf8')

    cook_book = {}
    list_of_dishes = []

    while True:

        string = filo.readline()

        if not string:
            break

        elif string[0].isalpha() and '|' not in string:
            string_without_n = string.replace('\n', '')
            list_of_dishes.append(string_without_n)
            cook_book[string_without_n] = []

        elif '|' in string:
            string_without_n = string[:-1]
            ingredient, quantity, measure = string_without_n.split('|')
            ingredient_without_space = ingredient.strip()
            quantity_without_space = quantity.strip()
            measure_without_space = measure.strip()
            dish = list_of_dishes[-1]
            cook_book[dish].append({'ingredient_name': ingredient_without_space,
                                    'quantity': quantity_without_space,
                                    'measure': measure_without_space})


    return cook_book

        # elif string[0].isdigit():
        #     # print(string)
        #     pass



print(recipe_from_file('other\\recipes.txt'))
