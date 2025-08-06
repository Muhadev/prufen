from celery import Celery
import os

celery_app = Celery("worker", broker=os.getenv("REDIS_URL"))

@celery_app.task
def test_task():
    return "Task executed"
