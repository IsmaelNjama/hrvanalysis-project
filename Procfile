release: python manage.py migrate
web: gunicorn hrvscihub.wsgi
worker: celery -A hrvscihub worker -E -l debug