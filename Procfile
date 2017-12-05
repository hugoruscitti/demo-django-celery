web: gunicorn backend.wsgi --log-file - --chdir backend --reload
worker: celery -A backend worker --workdir backend
