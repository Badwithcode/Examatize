from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from Sources.Users import UsersResource
from Sources.Login import LoginResource
from schema.studentSchema import add_user

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(UsersResource, "/users")
api.add_resource(LoginResource, "/login")


@app.get("/test")
def test_route():
    return "Hello World 123"

@app.post("/test2")
def add_user1():
    add_user()
    return True