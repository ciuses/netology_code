def my_quick_sort(my_list: list) -> list: # берём список
    if len(my_list) < 2: # если список меньше 2х, 1 и 0 не сортируется
        return my_list # возвращаем
    else:
        base_item = my_list[0] # берём самый первый элемент, рандомный элемент ускорит
        less = [num for num in my_list[1:] if num < base_item] # ищем все элементы меньше первого и делаем список малышей
        greater = [num for num in my_list[1:] if num > base_item] # ищем все элементы больше первого и делаем список старшаков
        return my_quick_sort(less) + [base_item] + my_quick_sort(greater) # посылаем оба списка по новой в рекурсию


print(my_quick_sort([15, 89, 3, 9, 10, 22, 2, 101]))

my_graf = {}
my_graf['you'] = ['alice', 'bob', 'mary']
my_graf['alice'] = ['Piter', 'Alex']
my_graf['bob'] = ['Tom']
my_graf['mary'] = ['Jane', 'Dan']
my_graf['Piter'] = []
my_graf['Tom'] = []
my_graf['Jane'] = []
my_graf['Dan'] = []

print(my_graf)