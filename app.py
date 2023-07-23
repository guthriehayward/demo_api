# Importing necessary libraries. Flask for API, SQLALchemy for database and Marshmallow for serialization
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Set SQLAlchemy app as the database
db = SQLAlchemy(app)

#set Marshmallow as whatever the ma is. LOOK THIS UP
ma = Marshmallow(app)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'

