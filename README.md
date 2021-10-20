## Проект Foodgram
![example workflow](https://github.com/vavsar/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

Проект Foodgram позволяет пользователям публиковать рецепты, добавлять рецепты в избранное и список покупок, 
подписыватся на других пользователей и скачивать список продуктов.

## Проект доступен по адрессу:
[Foodgram](http://84.252.137.235/)

## Технологии
- Python
- Django Rest Framework
- Docker
- postgresql
- nginx
- gunicorn

## Начало работы

Клонируйте репозиторий на локальную машину и перейдите в созданную папку.
```
git clone https://github.com/vavsar/foodgram-project-react.git && cd foodgram-project-react/
```

### Подготовка развертывания приложения

Для работы с проектом в контейнерах должен быть установлен Docker и docker-compose.  
Для установки запустите скрипт docker-setup.
```
./docker-setup
```

### Развертывание приложения
1. Для запуска проекта необходимо переименовать .env.dev в .env и заполнить значения переменных  

2. Необходимо запустить сборку контейнеров
```
cd infra/ && docker-compose up -d --build
```
3. Необходимо выполнить миграции и собрать статику приложения, для этого запустите скрипт
```
docker exec -ti infra_backend_1 python manage.py migrate
```
4. Для использования панели администратора по адресу http://localhost/admin/ необходимо создать суперпользователя.
```
docker exec -it infra_backend_1 python manage.py createsuperuser
```

## Технологии используемые в проекте
Python, Django, Django REST Framework, PostgreSQL, Nginx, Docker
