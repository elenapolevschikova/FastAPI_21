# -*- coding: utf-8 -*-
# № 17/1. Структура проекта( в main.py)

from fastapi import FastAPI
from app.routers import category, products


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(category.router)
app.include_router(products.router)


def main():
    pass


if __name__ == '__main__':
    main()



##################################
# Запуск :

# 1.Для запуска и автоматической перезагрузки сервера:
# uvicorn main:app --reload   (только при тестировании--reload )

# pip install fastapi
# pip install sqlalchemy
# pip install slugify
# pip install pydantic
# pip install alembic

# alembic init app/migrations
# alembic revision --autogenerate -m "Initial migration"

######################################################
# Попробуйте новую кроссплатформленную оболочку Powershell(https://aka.ms//pscore6)
# pip install fastapi[all]

# python.exe -m pip install upgrade pip


