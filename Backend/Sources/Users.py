from flask_restful import Resource

class UsersResource(Resource):
    def get(self):
        return "This is a get method of UserResources"