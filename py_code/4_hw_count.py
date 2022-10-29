queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

three, two, one = 0, 0, 0

for substring in queries:
    list_words = substring.split()
    if len(list_words) == 3:
        three += 1
    elif len(list_words) == 2:
        two += 1
    elif len(list_words) == 2:
        one += 1

print(
    f'Поисковые запросы из:\n'
    f'трёх слов составляют -> {three * 100 / len(queries):.2f}%\n'
    f'двух слов составляют -> {two * 100 / len(queries):.2f}%\n'
    f'одного слова составляют -> {one * 100 / len(queries):.2f}%')
