web: gunicorn mainApp.wsgi --log-file - 

web: python manage.py migrate && gunicorn MainApp.wsgi