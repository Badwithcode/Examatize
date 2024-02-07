from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from Sources import (
    LoginResource,
    LogoutResource,
    StudentCreateResource,
    PasswordResource,
    TokenResource,
    UsersResource,
)

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