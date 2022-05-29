import os
from celery import Celery
"""
Celery configuration
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')

app = Celery('eshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
