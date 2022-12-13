# СЕРВИС УВЕДОМЛЕНИЙ

## Необходимые библиотеки для запуска

    pip install fastapi

    pip install apscheduler

    pip install requests

    pip install sqlalchemy

## Команда для запуска

    uvicorn main:app --reload

## Документация

По локальному адресу: http://127.0.0.1:8000/docs#/

### Команды

По локальному адресу http://127.0.0.1:8000/ или вашему серверу.
Далее указанный адрес, для лаконичности, будет отмечаться точкой.

#### POST-запросы

Добавление клиента в базу:

    ./client/

Создание рассылки:

    ./mailing
#### GET-запросы
Получить рассылку по id:

    ./mailing/{mailing_id}
Получить все сообщения по id рассылки:
    ./message/{mailing_id}
#### DELETE-запросы
Удалить клиента из базы данных:

    ./client/{client_id}
Удалить рассылку:

    ./mailing/{mailing_id}

#### PATCH-запросы
Обновить любые данные клиента:

    ./client/{client_id}

Обновить атрибуты рассылки:

    ./mailing/{mailing_id}

    
