#!/bin/bash
cd ~/myFolder/projectRoot/backend

source auth/bin/activate
celery -A project.celery worker -l info
