#!/bin/bash
cd ~/myFolder/projectRoot/backend

source auth/bin/activate
celery -A project.celery beat --max-interval 1 -l info
