# arrancar gunicorn desde dolphin_test
PYTHONPATH=`pwd`/.. gunicorn --bind 0.0.0.0:8000 dolphin_site.wsgi:application

# arrancar wsgi desde dolphin_test
PYTHONPATH=`pwd`/.. uwsgi --http :8000 --module myproject.wsgi

