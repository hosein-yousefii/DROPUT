import pytest

from droput_msg.droput_msg import db

def test_database(app):
    with app.app_context():

        result = db.engine.execute("SELECT * from msg limit 1;").first()
        return result
    assert result[0] == "droput_msg"
    
