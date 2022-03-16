from datetime import timedelta
from droput_auth.config import Config
from droput_auth.util import now


def user_expires_at():
    return now() + timedelta(days=Config.USER_DEFAULT_EXPIRY_TIME)
    
