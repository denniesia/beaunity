from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beaunity.settings')

app = Celery('beaunity')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-reminders-every-morning' : {
        'task': 'beaunity.common.tasks.send_reminders',
        'schedule':  crontab(hour=8, minute=0),
        # 'schedule': 30.0
    },
    'update_is_new_status_daily': {
        'task': 'beaunity.common.tasks.update_is_new_status',
        'schedule': crontab(hour=0, minute=0),
        # 'schedule': 30.0
    }
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {}'.format(self.request))