It is an application created for the purposes of recruitment for Optimo Development.

To run application use following commands:
```
docker-compose up -d
```
To build application use (in web container):
```
python manage.py buildapp --profile development
```
To load python packages manually use (in web container):
```
python manage.py loadpackagesdata
```
To configure pagination page limit set in .env file:
```
...
PACKAGES_PAGINATION_PAGE_LIMIT=30
...
```

