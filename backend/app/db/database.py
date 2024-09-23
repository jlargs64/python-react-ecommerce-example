from app.db.session import SessionLocal
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
