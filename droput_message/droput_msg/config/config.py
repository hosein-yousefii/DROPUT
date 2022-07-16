from os import environ


class Config:

    # ============================== Global Configuration ==============================

    ENV = environ.get("DROPUT_MSG_ENV", "development")

    USER_AUTH_URL = environ.get("DROPUT_AUTH_URL", "http://127.0.0.1:5000")

    TESTING = int(environ.get("DROPUT_MSG_TESTING", "0"))

    DEBUG = int(environ.get("DROPUT_MSG_DEBUG", "1"))

    TIMEZONE = environ.get("DROPUT_MSG_TIMEZONE", "Asia/Tehran")

    TEST_USER = environ.get("DROPUT_MSG_TEST_USER", "test")
    # ============================= Database Configuration =============================

    SQLALCHEMY_DATABASE_URI = environ.get("DROPUT_MSG_DATABASE_URI", "sqlite:////tmp/droput_msg.db")

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_RECORD_QUERIES = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    # ============================= CACHE Configuration =============================

    REDIS_HOST = environ.get("DROPUT_MSG_REDIS_HOST", "localhost")

    REDIS_PORT = int(environ.get("DROPUT_MSG_REDIS_PORT", "6379"))

    REDIS_DATABASE = int(environ.get("DROPUT_MSG_REDIS_DATABASE", "0"))

    REDIS_PASSWORD = environ.get("DROPUT_MSG_REDIS_PASSWORD", "qazwsx")

    REDIS_CACHE_EXPIRE_SECONDS = int(environ.get("DROPUT_MSG_REDIS_CACHE_EXPIRE_SECONDS", "60"))

