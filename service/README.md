# Сервис для SibirCTF2018

## Руководство по установке

### Вручную 

- Установить PostgreSQL.

- Создать пользователя и БД. Дать пользователю права на создания БД.

- Настроить thefakebook.settings или вносить настройки в thefakebook.settings_local.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': ''
    }
}
```

- Выполнить:

```commandline
sudo apt-get install python3-pip
pip3 install -r requirements.txt
python3 manage.py makemigrations core
python3 manage.py migrate
python3 python manage.py test
gunicorn thefakebook.wsgi:application --bind 0.0.0.0:8000
```

### docker

#### build

```commandline
docker build . -t thefakebook_web
```

#### database

```commandline
docker run --name thefakebook_db --rm postgres
```

#### web

```commandline
docker run --link thefakebook_db:thefakebook_db -p 8000:8000 \
           --name thefakebook_web --rm -i -t thefakebook_web \
           bash -c "python manage.py makemigrations core && \
                    python manage.py migrate && \
                    python manage.py test && \
                    gunicorn thefakebook.wsgi:application --bind 0.0.0.0:8000"
```

### docker-compose

#### build

```commandline
docker-compose build
```

#### database

```commandline
docker-compose up thefakebook_db       # wait a minute 
```

#### web


```commandline
docker-compose up thefakebook_web
```