from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from api.delivery import stickers
from extension import db

from database_config import DatabaseConfig

load_dotenv()
app = Flask('sample')


app.register_blueprint(stickers.blueprint)

app.config.from_object(DatabaseConfig)


db.init_app(app)
migrate = Migrate(app, db)
from models import models
