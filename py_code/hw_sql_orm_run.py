import json
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

# # заполнение базы
# new_pub1 = Publisher(id=1, name='ДМК Пресс')
# new_pub2 = Publisher(id=2, name='ООО Издательство «Питер»')
#
# new_book1 = Book(id=1, title='Рогов Е. В. "PostgreSQL изнутри."', id_publisher=1)
# new_book2 = Book(id=2, title='Бизли Д., Джонс Б. К. "Python. Книга рецептов.', id_publisher=1)
# new_book3 = Book(id=3, title='Мэтиз Эрик "Изучаем Python. Программирование игр, визуализация данных, веб-приложения."',
#                  id_publisher=2)
#
# new_shop1 = Shop(id=1, name='Буказавр')
# new_shop2 = Shop(id=2, name='Книжбургер')
#
# new_stock1 = Stock(id=1, id_book=1, id_shop=1, count=100)
# new_stock2 = Stock(id=2, id_book=2, id_shop=1, count=500)
# new_stock3 = Stock(id=3, id_book=3, id_shop=2, count=305)

# my_session.add_all([new_pub1, new_pub2, new_book1, new_book2, new_book3, new_shop1, new_shop2, new_stock1, new_stock2, new_stock3])
# my_session.commit()


# search_term = input('Введите критерий для поиска "название" издательства или его "айди": ').lower()
#
# if search_term == 'название':
#     publishing_house = input('Введите название издательства c учетом регистра: ')
#     for re in my_session.query(Shop, Shop.name).join(Stock.shop, Stock.book, Book.publisher).filter(Publisher.name == publishing_house):
#         print(re[1])
#
# elif search_term == 'айди':
#     id_publishing_house = int(input('Введите айди издательства, цифрой: '))
#     for re in my_session.query(Shop, Shop.name).join(Stock.shop, Stock.book, Book.publisher).filter(Publisher.id == id_publishing_house):
#         print(re[1])
#
# else:
#     print('Введён некорретный критерий для поиска!')

def data_writer_for_db():
    with open('.\\other\\data_for_db_hw_orm.json', 'r', encoding='UTF-8') as filo:
        my_dict_data = json.load(filo)

        for data_string in my_dict_data:

            if data_string['model'] == 'publisher':
                # print(data_string)
                # print('No')
                data_for_db = Publisher(id=data_string['pk'], name=data_string['fields']['name'])
                my_session.add(data_for_db)
                my_session.commit()

            elif data_string['model'] == 'book':
                # print(data_string)
                # print('No')
                data_for_db = Book(id=data_string['pk'],
                                   title=data_string['fields']['title'],
                                   id_publisher=data_string['fields']['id_publisher'])
                my_session.add(data_for_db)
                my_session.commit()

            elif data_string['model'] == 'stock':
                # print(data_string)
                # print('No')
                data_for_db = Stock(id=data_string['pk'],
                                    id_book=data_string['fields']['id_book'],
                                    id_shop=data_string['fields']['id_shop'],
                                    count=data_string['fields']['count'])
                my_session.add(data_for_db)
                my_session.commit()

            elif data_string['model'] == 'shop':
                # print(data_string)
                # print('No')
                data_for_db = Shop(id=data_string['pk'], name=data_string['fields']['name'])
                my_session.add(data_for_db)
                my_session.commit()


data_writer_for_db()

my_session.close()
