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

        # elif string[0].isdigit():
        #     # print(string)
        #     pass

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int, path_to_recipe: str) -> dict:
    shop_list = {}

    for dishe in dishes:
        all_dishes = recipe_from_file(path_to_recipe)
        my_dishe = all_dishes[dishe]
        for ingredients_for_dishe in my_dishe:
            shop_list[ingredients_for_dishe['ingredient_name']] = {'measure': ingredients_for_dishe['measure'],
                                                                   'quantity': int(ingredients_for_dishe[
                                                                                       'quantity']) * person_count}

    return shop_list


if __name__ == '__main__':
    print(recipe_from_file('other\\recipes.txt'))
    di = get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 10, 'other\\recipes.txt')
    for k, v in di.items():
        print(k, v)
