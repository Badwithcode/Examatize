from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from Sources.Users import UsersResource
from Sources.Login import LoginResource

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(UsersResource, "/users")
api.add_resource(LoginResource, "/login")


@app.get("/test")
def test_route():
    return "Hello World 123"
