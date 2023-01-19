import sqlalchemy as alch
from sqlalchemy.orm import sessionmaker
from tokenators import password_db_clients as pas
from hw_sql_orm_models import create_tables

data_source_name = f"postgresql://postgres:{pas}@172.16.5.24:5432/test_hw"
engine = alch.create_engine(data_source_name)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
my_session = Session()


my_session.close()

