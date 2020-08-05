from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restplus import Api

# Custom
from resources import api
from resources import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
