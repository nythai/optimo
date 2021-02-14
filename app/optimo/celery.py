import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'optimo.settings')

app = Celery('optimo')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://' + settings.REDIS_HOST + ':' + settings.REDIS_PORT + '/0'
app.autodiscover_tasks()
