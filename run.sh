#!/bin/bash
export FLASK_APP=server.py
export FLASK_ENV=development

flask run --host=0.0.0.0
# authbind --deep gunicorn server:app -b :80
