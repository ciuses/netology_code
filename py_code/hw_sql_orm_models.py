import sqlalchemy as alch
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = alch.Column(alch.Integer, primary_key=True)
    name = alch.Column(alch.String(length=40), unique=True)

    book = relationship("book", back_populates="publisher")


class Book(Base):
    __tablename__ = "book"

    id = alch.Column(alch.Integer, primary_key=True)
    title = alch.Column(alch.String(length=40), unique=True)
    id_publisher = alch.Column(alch.Integer, alch.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")


class Shop(Base):
    __tablename__ = "shop"

    id = alch.Column(alch.Integer, primary_key=True)
    name = alch.Column(alch.String(length=40), unique=True)

    stock = relationship("stock", back_populates="shop")


class Stock(Base):
    __tablename__ = "stock"

    id = alch.Column(alch.Integer, primary_key=True)
    id_book = alch.Column(alch.Integer, alch.ForeignKey("book.id"), nullable=False)
    id_shop = alch.Column(alch.Integer, alch.ForeignKey("shop.id"), nullable=False)
    count = alch.Column(alch.Integer, nullable=False)

    # TODO проверить правильные ли связи
    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")


class Sale(Base):
    __tablename__ = "sale"

    id = alch.Column(alch.Integer, primary_key=True)
    price = alch.Column(alch.Integer, nullable=False)  # TODO Проверить тип данных
    date_sale = alch.Column(alch.Integer, nullable=False)  # TODO Проверить тип данных
    id_stock = alch.Column(alch.Integer, alch.ForeignKey("stock.id"), nullable=False)
    count = alch.Column(alch.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
