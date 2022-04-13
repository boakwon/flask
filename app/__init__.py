from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
# login_manager.login_view = 'login'

ma = Marshmallow(app)

app.app_context().push()

from app import routes, models