import os

from tokenators import password_db_clients as pas
import sqlalchemy as alch
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from dotenv import load_dotenv

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = alch.Column(alch.Integer, primary_key=True)
    name = alch.Column(alch.String(length=80), unique=True)

    book = relationship("Book", back_populates="publisher")

    def __str__(self):
        return f'id={self.id}\nname={self.name}'


class Book(Base):
    __tablename__ = "book"

    id = alch.Column(alch.Integer, primary_key=True)
    title = alch.Column(alch.String(length=255), unique=True)
    id_publisher = alch.Column(alch.Integer, alch.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship("Publisher", back_populates="book")
    stock = relationship("Stock", back_populates="book")

    def __str__(self):
        return f'id={self.id}\ntitle={self.title}\nid_publisher={self.id_publisher}'


class Shop(Base):
    __tablename__ = "shop"

    id = alch.Column(alch.Integer, primary_key=True)
    name = alch.Column(alch.String(length=80), unique=True)

    stock = relationship("Stock", back_populates="shop")

    def __str__(self):
        return f'id={self.id}\nname={self.name}'


class Stock(Base):
    __tablename__ = "stock"

    id = alch.Column(alch.Integer, primary_key=True)
    id_book = alch.Column(alch.Integer, alch.ForeignKey("book.id"), nullable=False)
    id_shop = alch.Column(alch.Integer, alch.ForeignKey("shop.id"), nullable=False)
    count = alch.Column(alch.Integer, nullable=False)

    shop = relationship("Shop", back_populates="stock")
    book = relationship("Book", back_populates="stock")
    sale = relationship("Sale", back_populates="stock")

    def __str__(self):
        return f'id={self.id}\nid_book={self.id_book}\nid_shop={self.id_shop}\ncount={self.count}'


class Sale(Base):
    __tablename__ = "sale"

    id = alch.Column(alch.Integer, primary_key=True)
    price = alch.Column(alch.Float, nullable=False)
    date_sale = alch.Column(alch.DateTime, nullable=False)
    id_stock = alch.Column(alch.Integer, alch.ForeignKey("stock.id"), nullable=False)
    count = alch.Column(alch.Integer, nullable=False)

    stock = relationship("Stock", back_populates="sale")

    def __str__(self):
        return f'id={self.id}\nprice={self.price}\ndate_sale={self.date_sale}\nid_stock={self.id_stock}\ncount={self.count}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


############################### Строка подключения и создание движка алхимии

load_dotenv()
data_source_name = f"postgresql://{os.getenv('USER')}:" \
                   f"{os.getenv('PASSWORD')}@" \
                   f"{os.getenv('HOST')}:" \
                   f"{os.getenv('PORT')}/" \
                   f"{os.getenv('DB')}"
engine = alch.create_engine(data_source_name)
create_tables(engine)

############################################# сессия

Session = sessionmaker(bind=engine)
my_session = Session()

