web: gunicorn beaunity.wsgi
worker: celery -A myproject worker --loglevel=info
beat: celery -A myproject beat --loglevel=info