filo = open('other\\recipes.txt', 'rt', encoding='utf8')

cook_book = {}
list_of_dishes = []

while True:

    string = filo.readline()
    # string.rstrip('\\n')

    if not string:
        break

    elif string[0].isalpha() and '|' not in string:
        print(string)
        # string.replace("\\n", "")
        list_of_dishes.append(string)
        cook_book[string] = []



    elif string[0].isdigit():
        # print(string)
        pass

    elif '|' in string:
        ingredient, quantity, measure = string.split('|')
        dish = list_of_dishes[-1]
        cook_book[dish].append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})



# print(cook_book)

for d, ing in cook_book.items():
    print(d, ing)
