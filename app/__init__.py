from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database_file = "postgres://postgres:infosec@MCAR611@localhost/online_banking"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy()
db.init_app(app)

from app import routes



app.run(debug = True)