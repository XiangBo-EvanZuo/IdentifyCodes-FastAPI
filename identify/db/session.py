from typing import Generator

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from identify.core.config import settings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'pics'
    num = Column('num', String(32))
    code = Column('code', String(32))

    def __repr__(self):
        return '<Student(id:%s, name:%s, age:%s)>' % (self.id, self.name, self.age)


engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == '__main__':
    session = SessionLocal()
    d = session.query(Student).all()
    print(d)
