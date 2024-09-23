from app.schemas.user_schema import User, UserCreate
from app.services.user_service import UserService, get_user_service
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/users")


@router.post("/", response_model=User)
def create_user(
    user: UserCreate, user_service: UserService = Depends(get_user_service)
):
    return user_service.create_user(user=user)


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    db_user = user_service.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=list[User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    user_service: UserService = Depends(get_user_service),
):
    return user_service.get_users(skip=skip, limit=limit)


@router.delete("/{user_id}", response_model=User)
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    db_user = user_service.delete_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int,
    user: UserCreate,
    user_service: UserService = Depends(get_user_service),
):
    db_user = user_service.update_user(user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
