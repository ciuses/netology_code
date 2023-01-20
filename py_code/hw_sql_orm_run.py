import sqlalchemy as alch
from sqlalchemy.orm import sessionmaker
from tokenators import password_db_clients as pas
from hw_sql_orm_models import *

data_source_name = f"postgresql://postgres:{pas}@172.16.5.24:5432/test_hw"
engine = alch.create_engine(data_source_name)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
my_session = Session()

# заполнение базы
new_pub1 = Publisher(id=1, name='ДМК Пресс')
new_pub2 = Publisher(id=2, name='ООО Издательство «Питер»')

new_book1 = Book(id=1, title='Рогов Е. В. "PostgreSQL изнутри."', id_publisher=1)
new_book2 = Book(id=2, title='Бизли Д., Джонс Б. К. "Python. Книга рецептов.', id_publisher=1)
new_book3 = Book(id=3, title='Мэтиз Эрик "Изучаем Python. Программирование игр, визуализация данных, веб-приложения."',
                 id_publisher=2)

new_shop1 = Shop(id=1, name='Буказавр')
new_shop2 = Shop(id=2, name='Книжбургер')

new_stock1 = Stock(id=1, id_book=1, id_shop=1, count=100)
new_stock2 = Stock(id=2, id_book=2, id_shop=1, count=500)
new_stock3 = Stock(id=3, id_book=3, id_shop=2, count=305)

# my_session.add_all([new_pub1, new_pub2, new_book1, new_book2, new_book3, new_shop1, new_shop2, new_stock1, new_stock2, new_stock3])
# my_session.commit()

# вывести данные
# print(new_pub1)
# print(new_book2)

# for boo in my_session.query(Book).all():
#     print(boo)
# for re in my_session.query(Book).join(Publisher.book).filter(Book.title == 'Бизли Д., Джонс Б. К. "Python. Книга рецептов.'):
#     print(re)
# работает
# for re in my_session.query(Book, Book.title).join(Publisher.book).filter(Publisher.id == 1):
#     print(re[1])
# for re in my_session.query(Book, Book.title).join(Publisher.book).filter(Publisher.name == 'ДМК Пресс'):
#     print(re[1])

for re in my_session.query(Shop, Shop.name).join(Stock.shop, Stock.book, Book.publisher).filter(Publisher.name == 'ДМК Пресс'):
    print(re[1])


my_session.close()
