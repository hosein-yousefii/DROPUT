from droput_auth.droput_auth import ma
from droput_auth.model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    password = ma.auto_field(load_only=True)
    created_at = ma.auto_field(dump_only=True)
    expires_at = ma.auto_field(dump_only=True)
    last_active_at = ma.auto_field(dump_only=True)
    failed_auth_at = ma.auto_field(dump_only=True)
    failed_auth_count = ma.auto_field(dump_only=True)
    status = ma.auto_field()
    
