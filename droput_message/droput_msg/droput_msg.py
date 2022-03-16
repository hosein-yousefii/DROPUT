from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from droput_msg.config import Config


db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

from droput_msg import resource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)          # Load application configs.
    db.init_app(app)                        # Initialize SQLAlchemy instance.
    mg.init_app(app, db)                    # Initialize Database Migrate instance.
    ma.init_app(app)                        # Initialize Serialization/Validation instance.
    app.register_blueprint(apiv1_bp)
    return app

