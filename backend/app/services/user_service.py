from app.db.database import get_db
from app.models.user import User
from app.schemas.user_schema import UserCreate
from fastapi import Depends
from sqlalchemy.orm import Session


class UserService:

    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate) -> User:
        db_user = User(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> User | None:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user

    def update_user(self, user_id: int, user: UserCreate) -> User | None:
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            self.db.commit()
            self.db.refresh(db_user)
        return db_user


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)
