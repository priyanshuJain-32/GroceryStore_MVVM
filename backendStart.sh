#!/bin/bash
cd backend

source auth/bin/activate
export FLASK_APP=project
export FLASK_DEBUG=1
flask run
