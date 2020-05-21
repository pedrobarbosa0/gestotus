# Gestotus

## Getting started

### Installing the dependencies
- Python 3.6+;

#### Create  and active virtualenv
```shell script
$ python3 -m venv env
$ source env/bin/activate
```
#### Install requirements
```shell script
$ pip install -r gestotus/requirements.txt
```

### Build project
#### Run the migrations
```shell script
$ cd gestotus
$ python manage.py makemigrations
$ python manage.py migrate
```
#### Now run project
```shell script
$ python manage.py runserver
```
