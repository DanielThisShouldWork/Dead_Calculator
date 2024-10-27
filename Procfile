web: gunicorn mainApp.wsgi:application --bind 0.0.0.0:8080


web: python manage.py migrate && gunicorn MainApp.wsgi