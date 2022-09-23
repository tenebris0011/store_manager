python manage.py collectstatic
systemctl restart nginx
gunicorn --bind :8000 --workers 3 core.wsgi:application