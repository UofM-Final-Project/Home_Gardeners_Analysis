. venv/bin/activate
export FLASK_APP=app.py
export SQLALCHEMY_DATABASE_URI="postgresql://postgres:<db_password>@127.0.0.1:5432/freeze_analysis"
export SECRET_KEY="sasdasdasdasdafwq"
export PYTHONPATH=.
export FLASK_ENV=development
flask run