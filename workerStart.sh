#!/bin/bash
cd backend

source auth/bin/activate
celery -A project.celery worker -l info
