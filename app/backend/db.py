# -*- coding: utf-8 -*-
# Прописываем в orm\__init__.py
# № 17/2. Подключение к БД.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase  # New

engine = create_engine('sqlite:///ecommerce.db', echo=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):  # New
    pass