# Django ORM
https://platform.productstar.ru/dd5ed729/aacf59c0-fc47-4770-8c3c-2a628ce398a4?tab=class


## Разработать базу данных сотрудников организации. 
Необходимо создать связанные таблицы **Сотрудники**, **Отделы** и **Филиалы** и разработать запросы для работы с БД.

### Сотрудники:
```
*Полное имя (обязательное)
*Должность (обязательное)
Номер телефона
Дата рождения
Email
```

### Отделы:
```
*Название (Например “Отдел маркетинга”, “Технический отдел”)
*Этаж, на котором расположен отдел (отдел не может занимать более одного этажа)
```

### Филиалы:
```
*Адрес (Например, “Москва, ул. Л. Кассиля, д. 1, корпус 3”)
*Короткое название (Например “Возле м. Внуково”)
```

>*Сотрудник* работает в каком-либо *Отделе*. *Отдел* принадлежит какому-либо *Филиалу*.
При удалении *Филиала* - все его отделы должны **оставаться без указания на филиал**. 
При удалении *Отдела* - все его сотрудники **удаляются каскадно**


## Этапы реализации
```
1. Создать новый проект на актуальной версии Django, добавить в него приложение “company”
2. Создать модели
3. Сгенерировать и применить миграции
4. Установить между моделями связи
5. Сгенерировать и применить миграции
6. Заполнить таблицы тестовыми данными: 3 филиала, в каждом 2-5 отделов по 3-10 сотрудников
7. Через ORM сформировать запросы, написать их код и sql-соответствие (не нужно писать циклы и принты):
	- количество сотрудников с должностью “Менеджер”
	- список сотрудников, работающих на четвертых этажах
	- по известным двум ID филиала получить список всех сотрудников, работающих в них (с помощью Q и с помощью лукапа проверки вхождения ID в список)
	- список ФИО сотрудников, у которых не указан email
	- список сотрудников, чей год рождения 1990	 
```

## Выполнение

### п.1
```
python -m venv venv
.\venv\Scripts\activate
pip install pip-tools
create file requirements.in (Django==5.1.1 ipython)
pip-compile.exe (generate requirements.txt)
pip-sync.exe
django-admin startproject main .
python manage.py startapp company
python manage.py showmigrations
python manage.py migrate
```

### п.2
```
python .\manage.py makemigrations company --dry-run (preview)
python .\manage.py makemigrations company
python manage.py sqlmigrate company 0001
python manage.py migrate company 
```

### п.2
```
added django-seed & psycopg2 in requirements.in
pip-compile.exe (generate requirements.txt)
pip-sync.exe
python manage.py seed company --number=50
```

## вход в SHELL
```
python manage.py shell
```
### Заполнение базы данных (вручную)
```
    from company.models import *

    v = Employee()
    v.fio = "Петров Семен Семенович"
    v.job = "Архитектор"
    v.save()
    v.pk

    v = Employee.objects.get(pk=1)
    v.fio = "Новое Имя"
    v.department
    v.save()
    v.delete()
    try: 
        v = Employee.objects.get(job='Сантехник2')
    except Employee.DoesNotExist as e:
        print(e)

    v = Employee(fio="Иванов Иван Петрович",job="Сантехник")
    v.save()    

    v = Employee.objects.create(fio="Иванов Иван Петрович",job="Сантехник")

    for e in Employee.objects.filter(department__gte=2).all():
        print(e.pk, e.fio)

    v = Employee.objects.get(pk=2)
    v.department.name
```

### С помощью django_seed
```
    from django.db import connection
    from django_seed import Seed

    office_count = 3
    departmens_per_office = 4
    employees_per_department = 7

    seeder = Seed.seeder()
    seeder.add_entity(Office, office_count)

    for i in range(office_count):    
        seeder.add_entity(Department, departmens_per_office, {
            'office_id': i+1
        })

    for i in range(office_count*departmens_per_office):
        seeder.add_entity(Employee, employees_per_department, {
            'department_id': i+1
        })

    seeder.execute()

    Offices.objects.filter(id__gt=3).delete()       оставляем три филиала
    Department.objects.filter(age__isnull=True).delete()   убираем отделы без филиалов
    Employee.objects.update(job='Менеджер')
```    