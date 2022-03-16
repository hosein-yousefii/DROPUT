from droput_auth.droput_auth import db
from droput_auth.config import Config
from droput_auth.util import uuidgen, now, user_expires_at

class User(db.Model):

    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=now)
    expires_at = db.Column(db.DateTime, nullable=False, default=user_expires_at)
    last_active_at = db.Column(db.DateTime)
    failed_auth_at = db.Column(db.DateTime)
    failed_auth_count = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.Integer, nullable=False, default=Config.USER_DEFAULT_STATUS)
