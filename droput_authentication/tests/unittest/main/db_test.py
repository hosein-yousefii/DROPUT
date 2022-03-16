import pytest

from droput_auth.droput_auth import db

def test_database(app):
    with app.app_context():

        result = db.engine.execute("SELECT * from user limit 1;").first()
        return result
    assert result[0] == "droput_auth"
    
