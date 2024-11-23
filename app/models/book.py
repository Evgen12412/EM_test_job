from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME

from app.config.config import Base


class Book(Base):
    #  указывает SQLAlchemy не пересоздавать таблицу, если она уже существует
    __tablename__ = "books"
    # используется для передачи дополнительных аргументов
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author  = Column(Integer, ForeignKey("books.id"), nullable=True)
    year = Column(DATETIME)
    status = Column(String)

from sqlalchemy.schema import CreateTable
print(CreateTable(Book.__table__))