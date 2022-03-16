from os import environ



class Config:

    # ============================== Global Configuration ==============================

    ENV = environ.get("DROPUT_AUTH_ENV", "development")

    TESTING = int(environ.get("DROPUT_AUTH_TESTING", "0"))

    DEBUG = int(environ.get("DROPUT_AUTH_DEBUG", "1"))

    TIMEZONE = environ.get("DROPUT_AUTH_TIMEZONE", "Asia/Tehran")

    SECRET_KEY = environ.get("DROPUT_AUTH_SECRET_KEY", "HARDSECRET")

    TEST_USER = environ.get("DROPUT_AUTH_TEST_USER", "test")
    # ============================= Database Configuration =============================

    SQLALCHEMY_DATABASE_URI = environ.get("DROPUT_AUTH_DATABASE_URI", "sqlite:////tmp/droput_auth.db")

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_RECORD_QUERIES = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    # =============================== User Configuration ===============================

    USER_DEFAULT_EXPIRY_TIME = int(environ.get("DROPUT_AUTH_USER_DEFAULT_EXPIRY_TIME", "365"))

    USER_DEFAULT_STATUS = int(environ.get("DROPUT_AUTH_USER_DEFAULT_STATUS", "3"))

    USER_DEFAULT_TOKEN_EXPIRY_TIME = int(environ.get("DROPUT_AUTH_USER_DEFAULT_TOKEN_EXPIRY_TIME", "86400"))

    USER_DEFAULT_TOKEN_ALGO = environ.get("DROPUT_AUTH_USER_DEFAULT_TOKEN_ALGO", "HS512")

