from fastapi import HTTPException
from serializers import todo as serializer
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.todo import TodoCreate, TodoUpdate
from database import todo_collection


class TodoCrud:

    @staticmethod
    def create_todo(todo_data: TodoCreate):
        todo_data = jsonable_encoder(todo_data)
        todo_document_data = todo_collection.insert_one(todo_data)
        todo_id = todo_document_data.inserted_id
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        return serializer.todo_serializer(todo)
    

    
    @staticmethod
    def get_todo(todo_id: str):
        try:
            todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
            if todo:
                return serializer.todo_serializer(todo)
            raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    def get_todos():
        todos = todo_collection.find()
        return serializer.todos_serializer(todos)
    
    @staticmethod
    def get_user_todos(user_id: str):
        todos = todo_collection.find({"user_id": user_id})
        return serializer.todos_serializer(todos)
    
    @staticmethod
    def update_todo(todo_id: str, todo_data: TodoUpdate):
        todo_data = jsonable_encoder(todo_data)
        todo_collection.update_one(
            {"_id": ObjectId(todo_id)},
            {"$set": todo_data}
        )
        todo = todo_collection.find_one({"_id": ObjectId(todo_id)})
        if todo:
            return serializer.todo_serializer(todo)
        raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
    
    @staticmethod
    def delete_todo(todo_id: str):
        delete_result = todo_collection.delete_one({"_id": ObjectId(todo_id)})
        if delete_result.deleted_count == 1:
            return {"status": "success", "message": f"Todo with ID {todo_id} deleted successfully"}
        raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
    
    


todo_crud = TodoCrud()
