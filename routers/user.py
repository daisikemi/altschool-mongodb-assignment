from fastapi import APIRouter, Path
from crud.user import user_crud
from schemas import user as user_schema
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=user_schema.User)
def create_user_endpoint(user: user_schema.UserCreate):
    return user_crud.create_user(user)



@router.get("/{user_id}", response_model=user_schema.User)
def get_user_endpoint(user_id: str):
    return user_crud.get_user(user_id)


@router.get("/", response_model=List[user_schema.User])
def get_users_endpoint():
    return user_crud.get_users()


@router.put("/{user_id}", response_model=user_schema.User)
def update_user_endpoint(
    user_id: str,
    user: user_schema.UserUpdate
):
    return user_crud.update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user_endpoint(user_id: str):
    return user_crud.delete_user(user_id)
