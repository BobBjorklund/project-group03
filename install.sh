
dropdb goats
createdb goats
psql -U lion -d goats -a -f setup.sql
source venv/bin/activate
cd venv/final/theGoats
python -m manage runserver & firefox 127.0.0.1:8000/


