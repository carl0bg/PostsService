#!/bin/bash
set -e

# Дождаться доступности PostgreSQL
/wait-for-it.sh postgres:5432 --timeout=30 --strict

# Создать миграции для всех приложений (если их ещё нет)
python manage.py makemigrations --noinput

# Применить все миграции
python manage.py migrate --noinput

# Запустить сервер
exec "$@"
