from sqlalchemy.engine import Engine
from .connection import db_connetion_handler

def test_connect_to_db():
    assert db_connetion_handler.get_engine() is None
    
    db_connetion_handler.connect_to_db()
    db_engine = db_connetion_handler.get_engine()
    
    assert db_engine is not None
    assert isinstance(db_engine, Engine)