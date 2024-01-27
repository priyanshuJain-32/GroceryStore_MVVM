from flask import current_app as app
from celery import Celery
from zoneinfo import ZoneInfo

celery = Celery("project", 
                broker_url = "redis://localhost:6379/1",
                result_backend = "redis://localhost:6379/2",
                backend='redis://localhost',
                broker="redis://localhost",
                broker_connection_retry_on_startup = True,
                timezone = ZoneInfo("Asia/Kolkata"))

class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)