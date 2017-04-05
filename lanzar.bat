cd src
C:\Python27\python -m pip install -r requirements.txt
manage.py makemigrations
manage.py migrate
REM manage.py loaddata location/fixtures/initial_data.xml
manage.py runserver 127.0.0.1:8000 --insecure
pause