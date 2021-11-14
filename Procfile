web: gunicorn core.wsgi
release: python manege.py makemigrations --noinput
release: python manege.py collectstatic --noinput
release: python manege.py migrate --noinput
