import os
from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL", "redis://localhost"))


app.conf.beat_schedule = {
    "add_2_plus_2_every_minute": {
        "task": "tasks.add",
        "schedule": crontab(),
        'args': (2, 2)
    },
}


@app.task
def add(x, y):
    print(x + y)
    return x + y
