web: gunicorn mainApp.wsgi:application --log-file - 

web: python manage.py migrate && gunicorn MainApp.wsgi