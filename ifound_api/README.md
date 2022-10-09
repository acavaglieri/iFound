# Server-side FastAPI/Python app:

## Pre-Install
```sh
$ sudo apt-get install libpq-dev
$ sudo apt install libmariadb3 libmariadb-dev
```


## Install
```sh
$ sudo apt install python3-pip
$ pip3 install virtualenv
$ python3.7 -m venv env
```

## Run
```sh
$ source env/bin/activate
(env)$ pip3 install wheel
(env)$ pip3 install -r requirements.txt
(env)$ uvicorn main:app --reload

./run.sh server
```

## Migrate

### Auto generate from models
```sh
(env)$ alembic revision --autogenerate -m "put a nice message here"
```

### Run all migrations
```sh
(env)$ alembic upgrade head
```

## .env Files

```
DATABASE_URL = db_plugins://user:password@url:port/db_name
```
