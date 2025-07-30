web: gunicorn beaunity.wsgi
worker: celery -A beaunity worker --loglevel=info
beat: celery -A beaunity beat --loglevel=info