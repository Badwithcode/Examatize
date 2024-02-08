from pymongo import MongoClient, ASCENDING, errors
import os
from dotenv import load_dotenv

load_dotenv()

MongoDB_URI = os.getenv("mongodb_uri")


Mongo_conn = MongoClient(host=MongoDB_URI)
mongo_db = Mongo_conn["Examatize"]
users_table = mongo_db["Users"]
question_table = mongo_db["Questions"]

users_table.create_index([('email', ASCENDING)], unique=True)
users_table.create_index([('phone', ASCENDING)], unique=True)
