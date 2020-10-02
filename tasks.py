import os
from celery import Celery
from celery.schedules import crontab

from flask import Flask, flash, render_template, redirect, request


app = Celery('tasks', broker=os.getenv("CELERY_BROKER_URL", "redis://localhost"))


@app.task
def add(x, y):
    print(x + y)
    return x + y


app.conf.beat_schedule = {
    "add_2_plus_2_every_minute": {
        "task": "tasks.add",
        "schedule": crontab(),
        'args': (2, 2)
    },
}


# celery beat doesn't expose a port that render can use for a health check, so adding this
# dummy flask app that I will run in background that will respond with a 200 if OK
dummy_flask_app = Flask(__name__)


@dummy_flask_app.route('/is_healthy')
def is_healthy():
    return "ok", 200