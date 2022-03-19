# API для мегафона

либо локально через

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

либо через 

    docker-compose up

api доступно по следующим урлам:

- /api/customers
- /api/tariffs
- /api/events

Разрешены все REST API операции, кроме апдейта в событиях (events)
