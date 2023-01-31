# Статистика портфеля
## _Проект для обмена данными с API Мосбиржи_

## Описание:
Проект статистика портфеля разработан для простоты учета финснсового 
результата инвестиционного портфеля, собранного у разных брокеров. 
Управление активами осуществляется через админку.

## Установка:
1. Клонируйте репозиторий, перейдите в него:
```sh
git clone git@github.com:gregoskol/deposits.git
cd deposits
```
2. Создайте и активируйте виртуальное окружение:
```sh
python -m venv venv
source venv/Scripts/activate
```
3. Установите зависимости:
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполните миграции, запустите проект:
```sh
python manage.py migrate
python manage.py runserver
```