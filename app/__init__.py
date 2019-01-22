from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#atabase_file = "postgres://postgres:infosec@MCAR611@localhost/online_banking"
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# app.config['SQLALCHEMY_DATABASE_URI'] = database_file
# app.secret_key = "\x181\x9b$\xcc\x83\xf60]<\x91R\xa7+\xb0\x08'!\x1a\xdd\x1c\xa6\x7f\xee"
db = SQLAlchemy()
db.init_app(app)

from app import routes



app.run(debug = True)