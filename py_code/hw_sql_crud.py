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

def create_tables(cursor: object):
    '''Создаёт таблицеу clients и phone_numbers.'''

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

    cursor.commit()


if __name__ == '__main__':

    my_con = psycopg2.connect(host='172.16.5.25',
                              port='5432',
                              database='clients',
                              user='postgres',
                              password='hanson')

    with my_con.cursor() as curs:
        create_tables(curs)

    my_con.close()
