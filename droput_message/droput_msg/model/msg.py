from droput_msg.droput_msg import db
from droput_msg.config import Config
from droput_msg.util import uuidgen, now


class Msg(db.Model):

    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    sender = db.Column(db.String(128), index=True, nullable=False)
    content = db.Column(db.String(256), nullable=True)
    message_sent_at = db.Column(db.DateTime, nullable=False, default=now)
    receiver = db.Column(db.String(128), index=True, nullable=False)
    read = db.Column(db.Boolean, nullable=False, default=False)
    
