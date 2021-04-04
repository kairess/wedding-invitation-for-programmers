!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development

flask run --host=0.0.0.0
# authbind --deep gunicorn app:app -b :80
