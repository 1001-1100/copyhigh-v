release: python manage.py makemigrations hello && python manage.py migrate hello --no-input && python manage.py makemigrations && python manage.py migrate --no-input
web: gunicorn dlsuscheduler.wsgi
