import os
from pymongo import mongo_client
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_CONNECTION_URI = os.environ.get('MONGO_DB_CONNECTION_URI')




client = mongo_client.MongoClient(MONGO_DB_CONNECTION_URI)
 
  

db = client["todoapp"]
user_collection = db["users"]
todo_collection = db["todo"]






todo_data_collection = db["todo_data"]


