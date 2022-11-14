# Наследование
# Наследование — это свойство системы, позволяющее описать
# новый класс на основе уже существующего.


class Primate:
    # Базовый, или же родительский класс.
    def __init__(self):
        self.number_of_legs = 2
        self.can_walk = True

    def display_info(self):
        print("Я примат.")


class Man(Primate):
    # Дочерний класс, наследующий от Primate
    def __init__(self, name, surname):
        # Эта строчка инициализирует объект родительского класса.
        # Если вы переопределяете метод __init__,
        # то она здесь обязательно должна быть!
        super().__init__()
        # Атрибуты, которые есть только у объектов класса Man, но не Primate.
        self.name = name
        self.surname = surname

    def display_info(self):
        print("Я человек.")


tom = Man("Том", "Смит")

# Атрибуты базового класса
print(tom.number_of_legs)
print(tom.can_walk)
# Атрибуты дочернего класса
print(tom.name)
print(tom.surname)


# В дочернем классе мы можем присвоить атрибутам базового класса новое значение


class Insect:
    def __init__(self):
        self.number_of_legs = 6
        self.can_crawl = True

    def display_info(self):
        print("Я насекомое.")


class Spider(Insect):
    def __init__(self):
        super().__init__()
        self.number_of_legs += 2

    def display_info(self):
        print("Я паук.")


spider = Spider()
print(spider.number_of_legs)


# Один класс может наследовать от нескольких классов. В этом случае у него
# будут атрибуты и методы всех родительских классов.


class SpiderMan(Man, Spider):
    def __init__(self, name, surname):
        # В случае множественного наследования мы должны инициализировать
        # все родительские классы. super().__init() здесь не подойдёт,
        # потому что он инициализирует только один родительский класс.
        Man.__init__(self, name, surname)
        Spider.__init__(self)

    def display_info(self):
        print("Я Человек-Паук!")


peter_parker = SpiderMan("Питер", "Паркер")
print(peter_parker.name)
print(peter_parker.surname)
print(peter_parker.can_walk)
print(peter_parker.can_crawl)


# Method Resolution Order

# Метод display_info() есть у всех классов выше, при этом для каждого класса
# этот метод делает разное. Как вы думаете, что выведется, если вызвать этот
# метод у объекта класса SpiderMan?

# peter_parker.display_info()

# А если убрать этот метод из каких-то классов?

# Method Resolution Order (MRO) —
# порядок, в котором Python ищет метод в иерархии классов.
# Посмотреть этот порядок можно так:

print(SpiderMan.mro())
