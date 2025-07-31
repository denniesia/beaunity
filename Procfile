web: gunicorn beaunity.wsgi --bind 0.0.0.0:$PORT
worker: celery -A beaunity worker --loglevel=info
beat: celery -A beaunity beat --loglevel=info