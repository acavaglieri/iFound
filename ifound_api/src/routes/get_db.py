from src.database.database import *
from sqlalchemy.orm import Session


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Gerenciador de sessões criado para uso nas Tasks (ou externo ao FastAPI)
def get_db_tasks():
    db = Session(engine)
    try:
        return db
    except:
        db.rollback()
        raise
    finally:
        db.close()
