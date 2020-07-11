# django-restful-api - Django

  This is a simple Django restful api to improve my skills with Django-Rest-Framework where you can add Heros.
 
## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/Kburak/django-restful-api.git
$ cd django/django-restful-api
```
##### Create the virtualenv and activate it
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Or on Windows cmd::
```bash
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Create a Super User to access admin panel
```bash
$ python manage.py createsuperuser
```

##### Make Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

##### Run the app
```bash
$ python manage.py runserver
```
