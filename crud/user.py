from fastapi import HTTPException
from serializers import user as serializer
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from schemas.user import UserCreate, UserUpdate
from database import user_collection


class UserCrud:

    @staticmethod
    def create_user(user_data: UserCreate):
        user_data = jsonable_encoder(user_data)
        user_document_data = user_collection.insert_one(user_data)
        user_id = user_document_data.inserted_id
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        return serializer.user_serializer(user)
    
    @staticmethod
    def get_user(user_id: str):
        try:
            user = user_collection.find_one({"_id": ObjectId(user_id)})
            if user:
                return serializer.user_serializer(user)
            raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    def get_users():
        users = user_collection.find()
        return serializer.users_serializer(users)
    
    @staticmethod
    def update_user(user_id: str, user_data: UserUpdate):
        user_data = jsonable_encoder(user_data)
        user_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user_data}
        )
        user = user_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            return serializer.user_serializer(user)
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    
    @staticmethod
    def delete_user(user_id: str):
        delete_result = user_collection.delete_one({"_id": ObjectId(user_id)})
        if delete_result.deleted_count == 1:
            return {"status": "success", "message": f"User with ID {user_id} deleted successfully"}
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    

   


user_crud = UserCrud()
