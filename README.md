# Django-Dashboard - Linux

git clone https://github.com/shubhamgoel01/Django-Dashboard.git
python -m venv env

source env/bin/activate

pip install -r req.txt

# For DB-Admin
python manage.py makemigrations

python manage.py migrate

# To Start
Dashboard - nohup python manage.py  runserver 0.0.0.0.8000


cd /opt/Nessus_Map

cd Nessus_Map-BETA
nohup python manage.py  runserver 0.0.0.0:9001

Nessus_Map-ALL		nohup python manage.py  runserver 0.0.0.0:9000

Nessus_Map-BETA		nohup python manage.py  runserver 0.0.0.0:9001

Nessus_Map-DCE		nohup python manage.py  runserver 0.0.0.0:9002

Nessus_Map-DCW		nohup python manage.py  runserver 0.0.0.0:9003
