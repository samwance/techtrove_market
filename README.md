# Онлайн платформа торговой сети электроники

### Description: 
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья - её уровень - 1.
## Getting Started:

1) Clone the repository:
```
git clone https://github.com/samwance/techtrove_market.git
```
2) Navigate to the project directory:
```
cd techtrove_market
```
3) Create a .env file with the required environment variables. You can find a sample .env file in the project directory.

4) Run the Django migrations to set up the database:
```
python manage.py migrate
```
To create a superuser for the Django admin site:
```
python manage.py createsuperuser
```

Start the Django development server:
```
python manage.py runserver
```
Open your web browser and navigate to http://localhost:8000/admin/ to access the Django admin site.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
