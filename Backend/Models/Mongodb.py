import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MongoDB_URI = os.getenv("mongodb_uri")


Mongo_conn = pymongo.MongoClient(host=MongoDB_URI)
<<<<<<< HEAD
mongo_db = Mongo_conn['Examatize']
users_table = mongo_db['Users'] 
=======
mongo_db = Mongo_conn["Examatize"]
users_table = mongo_db["Users"]
question_table = mongo_db["Questions"]
>>>>>>> ea3d47b221642f9ea068505dc81786f8e43b0163
