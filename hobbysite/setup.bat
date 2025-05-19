cd ../venv/scripts && activate && cd ../../hobbysite &&^
python manage.py makemigrations accounts profile merchstore wiki blog forum commissions &&^
python manage.py migrate && python manage.py createsuperuser --no-input
