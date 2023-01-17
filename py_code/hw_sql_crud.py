import psycopg2


# def create_db(conn):
#     pass
#
# def add_client(conn, first_name, last_name, email, phones=None):
#     pass
#
# def add_phone(conn, client_id, phone):
#     pass
#
# def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
#     pass
#
# def delete_phone(conn, client_id, phone):
#     pass
#
# def delete_client(conn, client_id):
#     pass
#
# def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
#     pass
#
#
# with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
#     pass  # вызывайте функции здесь
#
# conn.close()

def drop_tables(connect: object, table_name: str):
    '''Удаляет таблицы перданные в аргумете table_name.'''
    with connect.cursor() as cursor:
        cursor.execute(f"""DROP TABLE {table_name};""")
    connect.commit()

def create_tables(connect: object):
    '''Создаёт таблицеу clients и phone_numbers.'''

    with connect.cursor() as cursor:

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(60) NOT NULL,
                    last_name VARCHAR(80) NOT NULL,
                    email VARCHAR(255) NOT NULL);
                    """)

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS phone_numbers (
                    phone_id INTEGER REFERENCES clients(id),
                    phone_number VARCHAR(20));
                    """)

    connect.commit() # TODO дописать какие нить принты


def add_new_client(connect: object, f_name: str, l_name: str, email: str, phone: str=None):
    '''Добавляет клиента, можно без телефона.'''

    if phone == None:

        with connect.cursor() as cursor:

            cursor.execute("""
                        INSERT INTO clients(first_name, last_name, email)
                        VALUES (%s, %s, %s);""", (f_name, l_name, email))

    else:

        with connect.cursor() as cursor:

            cursor.execute("""
                        INSERT INTO clients(first_name, last_name, email)
                        VALUES (%s, %s, %s) RETURNING id;""", (f_name, l_name, email))

            id_for_link_phone = cursor.fetchone()[0]

            cursor.execute("""
                        INSERT INTO phone_numbers
                        VALUES (%s, %s);""", (id_for_link_phone, phone))

    connect.commit()


def add_phone(connect: object, client_id: int, phone: str):
    '''Создаёт запись в табле телефонов с айди существющего клиента.'''

    with connect.cursor() as cursor:

        cursor.execute("""
                    INSERT INTO phone_numbers
                    VALUES (%s, %s);""", (client_id, phone))

    connect.commit()

def change_client_data(connect: object, client_id: int, f_name: str=None, l_name: str=None, email: str=None, phone: str=None):

    if f_name:

        with connect.cursor() as cursor:

            cursor.execute("""UPDATE clients SET first_name=%s WHERE id=%s;""", (f_name, client_id))

    if l_name:

        with connect.cursor() as cursor:

            cursor.execute("""UPDATE clients SET last_name=%s WHERE id=%s;""", (l_name, client_id))

    if email:

        with connect.cursor() as cursor:

            cursor.execute("""UPDATE clients SET email=%s WHERE id=%s;""", (email, client_id))

    if phone:

        with connect.cursor() as cursor:

            cursor.execute("""UPDATE phone_numbers SET phone_number=%s WHERE phone_id=%s;""", (phone, client_id))


    connect.commit()



if __name__ == '__main__':

    my_con = psycopg2.connect(host='172.16.5.25',
                              port='5432',
                              database='clients',
                              user='postgres',
                              password='hanson')


    # drop_tables(my_con, 'phone_numbers')
    # drop_tables(my_con, 'clients')

    # create_tables(my_con)

    # add_new_client(my_con, 'Фёдор', 'Дядя', 'fedor@df_city.com')
    # add_new_client(my_con, 'Матроскин', 'Кот', 'matroskin@df_city.com', '79029017776')
    # add_new_client(my_con, 'Шарик', 'Пёс', 'sharick@df_city.com', '79039014862')
    # add_new_client(my_con, 'Галчёнок', 'Кто Там','jackdaw@village.com', '79049019559')
    # add_new_client(my_con, 'Игорь Иванович', 'Печкин', 'pechkin@village.com', '79049019559')

    # add_phone(my_con, 16, '79019011111')
    # add_phone(my_con, 16, '79019013333')

    change_client_data(my_con, 18,
                       f_name='Шароид',
                       l_name='Пёсинатор',
                       email='kill_them_all@destroy.com',
                       phone='22222222222')



    my_con.close()


