from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from Sources.Users import UsersResource
from Sources.Login import LoginResource
from Sources import (
    LoginResource,
    LogoutResource,
    StudentCreateResource,
    PasswordResource,
    TokenResource,
    UsersResource,
)

from Sources.Users import UsersResource
from Sources.Login import LoginResource, LogoutResource
from Sources.Signup import StudentCreateResource
from Sources.Token import TokenResource

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(UsersResource, "/users")
api.add_resource(LoginResource, "/login")
api.add_resource(TokenResource, '/token')
api.add_resource(StudentCreateResource, '/addstudent')
api.add_resource(LogoutResource, "/logout")


@app.get("/test")
def test_route():
    return "Hello World 123"
