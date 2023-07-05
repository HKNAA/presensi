from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask import Flask

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app=app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.repository.pegawai.entity import Pegawai

from app.controller.api import *