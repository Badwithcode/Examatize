from mongoengine import Document, StringField, BooleanField
from passlib.hash import bcrypt
import pymongo
import os
from dotenv import load_dotenv
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from passlib.hash import bcrypt
load_dotenv()

MongoDB_URI = os.environ.get('mongodb_uri')


Mongo_conn = pymongo.MongoClient(host=MongoDB_URI)
mongo_db = Mongo_conn['Examatize']
users_table = mongo_db['Users']

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'your_database_name'
db = MongoAlchemy(app)


User=users_table
class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)
    pic = db.StringField(default="https://icon-library.com/images/anonymous-avatar-icon/anonymous-avatar-icon-25.jpg")
    isAdmin = db.BoolField(default=False, required=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith("$2a$"):
            # Encrypt the password if it's not already encrypted
            self.password = bcrypt.hash(self.password, rounds=10)
        super(User, self).save(*args, **kwargs)

# Create a dummy user document
dummy_user = User(
    name="John Doe",
    email="john.doe@example.com",
    password="hashed_password",  # Replace with the actual hashed password
    isAdmin=True
)

# Save the dummy user document to the database
dummy_user.save()

print("Dummy user created and saved.") 