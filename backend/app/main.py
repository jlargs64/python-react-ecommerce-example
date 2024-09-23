from app.db.database import Base
from app.db.session import engine
from app.routes.users_router import router as users_router
from fastapi import FastAPI

# Create tables
Base.metadata.create_all(bind=engine)

# Init app and routes
app = FastAPI()
app.include_router(users_router)
