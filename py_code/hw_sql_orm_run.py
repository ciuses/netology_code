from py_code.hw_sql_orm_upload_data import data_writer_for_db
from hw_sql_orm_models import my_session, Shop, Stock, Book, Publisher

data_writer_for_db()

if __name__ == '__main__':

############################################### Задание № 2 Найти магаз по издателю

    search_term = input('Введите критерий для поиска "название" издательства или его "айди": ').lower()

    if search_term == 'название':
        publishing_house = input('Введите название издательства c учетом регистра: ')
        for re in my_session.query(Shop, Shop.name)\
                .join(Stock, Stock.id_shop == Shop.id)\
                .join(Book, Book.id == Stock.id_book)\
                .join(Publisher, Publisher.id == Book.id_publisher)\
                .filter(Publisher.name == publishing_house):
            print(re[1])

    elif search_term == 'айди':
        id_publishing_house = int(input('Введите айди издательства, цифрой: '))
        for re in my_session.query(Shop, Shop.name)\
                .join(Stock, Stock.id_shop == Shop.id)\
                .join(Book, Book.id == Stock.id_book)\
                .join(Publisher, Publisher.id == Book.id_publisher)\
                .filter(Publisher.id == id_publishing_house):
            print(re[1])

    else:
        print('Введён некорретный критерий для поиска!')



    my_session.close()
