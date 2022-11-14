class Income:
    def __init__(self, id_):
        self.id_ = id_
        id_ = 100

in_1 = Income(1000)
print(in_1.id_)

class Pers:
    def __init__(self, id):
        self.id = id

some_pers = Pers(100)
# some_pers.id = 100
some_pers.__dict__['age'] = 30
print(some_pers.age + len(some_pers.__dict__))

class Income:
    def __init__(self, id_):
        self.id_ = id_

    def test(self, word):
        print(f'My word is {word}')

    def test(self, int):
        print(f'My ineger is {int}')


my_income = Income(45)
print(my_income.test(555))
print(my_income.test('test'))

# print(my_income.isinstans(Income))
# print(Income.isinstans(my_income))
print(isinstance(my_income, Income))