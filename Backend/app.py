from flask import Flask
from flask_cors import CORS
from flask_restful import Api
<<<<<<< HEAD
from Sources.Users import UsersResource
from Sources.Login import LoginResource
from schema.studentSchema import add_user
=======

from Sources import (
    LoginResource,
    LogoutResource,
    StudentCreateResource,
    PasswordResource,
    TokenResource,
    UsersResource,
)
>>>>>>> ea3d47b221642f9ea068505dc81786f8e43b0163

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(UsersResource, "/users")
api.add_resource(LoginResource, "/login")
api.add_resource(TokenResource, "/token")
api.add_resource(StudentCreateResource, "/addstudent")
api.add_resource(PasswordResource, "/changepassword")
api.add_resource(LogoutResource, "/logout")


@app.get("/test")
def test_route():
    return "Hello World 123"

@app.post("/test2")
def add_user1():
    add_user()
    return True