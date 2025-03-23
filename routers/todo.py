from fastapi import APIRouter
from crud.todo import todo_crud
from schemas import todo as todo_schema
from typing import List

router = APIRouter(prefix="/todos", tags=["Todos"])



@router.post("/", response_model=todo_schema.Todo, status_code=201)
def create_todo_endpoint(todo: todo_schema.TodoCreate):
    return todo_crud.create_todo(todo)

@router.get("/{todo_id}", response_model=todo_schema.Todo, status_code=200)
def get_todo_endpoint(todo_id: str):
    return todo_crud.get_todo(todo_id)


@router.get("/", response_model=List[todo_schema.Todo], status_code=200)
def get_todos_endpoint():
    return todo_crud.get_todos()


@router.get("/user/{user_id}", response_model=List[todo_schema.Todo],status_code=200)
def get_user_todos_endpoint(user_id: str):
    return todo_crud.get_user_todos(user_id)


@router.put("/{todo_id}", response_model=todo_schema.Todo, status_code=201)
def update_todo_endpoint(
    todo_id: str,
    todo: todo_schema.TodoUpdate
):
    return todo_crud.update_todo(todo_id, todo)


@router.delete("/{todo_id}")
def delete_todo_endpoint(todo_id: str):
    return todo_crud.delete_todo(todo_id)
