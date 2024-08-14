# -*- coding: utf-8 -*-
# (в schemas.py)
from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str   # имя
    description: str   # описание
    price: int  # цена
    image_url: str     # ссылка на изображение
    stock: int  # остаток
    category: int      # № id - категории


class CreateCategory(BaseModel):
    name: str  # имя
    parent_id: int | None  # родитель