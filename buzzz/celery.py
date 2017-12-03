from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buzzz.settings')

app = Celery('proj')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))

from celery.schedules import crontab

# app.conf.beat_schedule = {
#     'bithumb_get_orderbook_every_minute': {
#         'task': 'bithumb_get_base_orderbook',
#         'schedule': crontab(),
#         'args': (),
#     },
# }

import random

app.conf.beat_schedule = {
#    'add-every-5-seconds-forever': {
#        'task': 'sum_two_numbers',
#        'schedule': 5.0,
#        'args': (random.randint(1, 100), random.randint(1, 100)),
#    },

    'scrape-naver-ohlcv-at-4': {
    	'task': 'scrape_naver_ohlcv',
    	'schedule': crontab(),
        'args': (),
    }
}
