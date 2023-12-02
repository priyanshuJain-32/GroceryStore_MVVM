from flask import Flask
from celery import Celery, Task
from .celeryconfig import celery_config

def celery_init_app(app):
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(celery_config)
    # celery_app.set_default()
    # app.extensions["celery"] = celery_app
    return celery_app