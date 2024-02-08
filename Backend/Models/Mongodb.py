import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MongoDB_URI = os.getenv("mongodb_uri")


Mongo_conn = pymongo.MongoClient(host=MongoDB_URI)
mongo_db = Mongo_conn["Examatize"]
users_table = mongo_db["Users"]
question_table = mongo_db["Questions"]
