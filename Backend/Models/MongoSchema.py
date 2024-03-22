from mongoengine import (
    Document,
    ListField,
    StringField,
    IntField,
    DateTimeField,
    connect,
    Q,
)
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()


MongoDB_URI = os.getenv("mongodb_uri")
connect(host=MongoDB_URI, db="Examatize")


class Users(Document):
    user_name = StringField(required=True)
    roll_no = StringField(required=True)
    email = StringField(unique=True, index=True)
    password = StringField(required=True)
    role = StringField(required=True, choices=["admin", "teacher", "student"])
    phone = IntField()
    department = StringField()
    batch = IntField()

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))


class Batch(Document):
    name = StringField(unique=True, index=True)
    description = StringField(required=True)
    Strattime = DateTimeField(required=True)
    Endtime = DateTimeField(required=True)
    teacher = StringField(required=True)
    questions = ListField(required=True)
    assigned_time = DateTimeField(required=True)
    subject = StringField(required=True)
