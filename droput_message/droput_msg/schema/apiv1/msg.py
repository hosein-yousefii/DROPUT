from droput_msg.droput_msg import ma
from droput_msg.model import Msg


class MsgSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Msg

    id = ma.auto_field(dump_only=True)
    sender = ma.auto_field()
    content = ma.auto_field()
    message_sent_at = ma.auto_field(dump_only=True)
    receiver = ma.auto_field()
    read = ma.auto_field(dump_only=True)
