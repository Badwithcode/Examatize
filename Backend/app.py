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
    ProfileResource,
    UpcomingTestResource,
    TestResource,
    CompletedTestResource,
    AddBatchResource,
    AdminPasswordResource,
    TestBatchResource,
    ScoreTestResource,
)

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(UsersResource, "/users")
api.add_resource(LoginResource, "/login")
api.add_resource(TokenResource, "/token")
api.add_resource(StudentCreateResource, "/addstudent")
api.add_resource(PasswordResource, "/changepassword")
api.add_resource(AdminPasswordResource, "/adminchangepassword")
api.add_resource(LogoutResource, "/logout")
api.add_resource(ProfileResource, "/profile")
api.add_resource(UpcomingTestResource, "/upcoming")
api.add_resource(TestResource, "/tests")
api.add_resource(CompletedTestResource, "/completed")
api.add_resource(AddBatchResource, "/addbatch")
api.add_resource(TestBatchResource, "/test/<string:batch_name>")
api.add_resource(ScoreTestResource, "/score/<string:batch_name>")


@app.get("/apitest")
def test_route():
    return "Hello World 123"
