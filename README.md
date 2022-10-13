# Smartphone 
## List of brands

- [ ] Apple
- [ ] Samsung
- [ ] Huawei
- [ ] Xiaomi
- [ ] Oppo
- [ ] Vivo
- [ ] Nokia

## Structure of the project
### 1. Design of the project database
### 2. Design of the project interface
### 3. Design of the project test
### 4. Design of the project report
### 5. Design of the project presentation

## List of tasks
### 1. Design of the project database
- [ ] Create the database
- [ ] Create the tables
- [ ] Create the relations
- [ ] Create the views

### 2. Design of the project interface

- [ ] Create the interface
- [ ] Create the forms
- [ ] Create the reports

### 3. Design of API endpoints
- [ ] Create the API endpoints
- [ ] Create the API documentation

### 4. List of API endpoints

- [ ] GET /api/brands # Get all brands
- [ ] GET /api/brands/{id} # Get a brand
- [ ] POST /api/brands # Create a brand
- [ ] POST /api/brands/{id} # Update a brand
- [ ] DELETE /api/brands/{id} # Delete a brand


# List of task
- [x] Create the project

```django-admin startproject smartphone .```

- [x] Create the app

```python manage.py startapp smartphone_app```

- [x] Create the django's project database

```bash
python manage.py migrate
```

- [x] Create the superuser

```python manage.py createsuperuser```

- [x] Create the smartphone's app database tables

## Database schema
### 1. Brand
| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(255) | NO | | NULL | |
| company | varchar(255) | NO | | NULL | |
| color | varchar(255) | NO | | NULL | |
| RAM | int(11) | NO | | NULL | |
| memory | int(11) | NO | | NULL | |
| price | int(11) | NO | | NULL | |
| created_at | datetime | NO | | NULL | |
| updated_at | datetime | NO | | NULL | |
| img_url | varchar(255) | NO | | NULL | |

- [x] Create the smartphone's app database models

```python
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    RAM = models.IntegerField()
    memory = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_url = models.CharField(max_length=255)
    def __str__(self):
        return self.name
```

- [ ] Register the smartphone's app database models

```python
from django.contrib import admin
from .models import Product
admin.site.register(Product)
```

- [ ] Register the smartphone's app to the django's project

```python
INSTALLED_APPS = [
    'smartphone_app.apps.SmartphoneAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
