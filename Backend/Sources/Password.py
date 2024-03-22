from flask_restful import Resource, request
from Models.MongoSchema import Users
from bcrypt import hashpw, gensalt
from Core.Middleware import is_admin


class PasswordResource(Resource):
    def put(self):
        try:
            data = request.get_json()
            email = data["email"]
            old_password = data["old_password"]
            new_password = data["new_password"]
            user = Users.objects(email=email).first()
            if user.check_password(old_password):
                new_hash_password = hashpw(new_password.encode("utf-8"), gensalt())
                user.password = new_hash_password.decode("utf-8")
                user.save()
                return {"status": True}
            return {"status": False, "message": "Invalid Old password"}
        except Exception as e:
            return {"status": False, "message": f"Error{e}"}


class AdminPasswordResource(Resource):
    @is_admin()
    def put(self):
        try:
            data = request.get_json()
            email = data["email"]
            new_password = data["new_password"]
            user = Users.objects(email=email).first()
            if user:
                new_hash_password = hashpw(new_password.encode("utf-8"), gensalt())
                user.password = new_hash_password
                user.save()
                return {"status": True}
            return {"status": False, "message": "Invalid Old password"}
        except Exception as e:
            return {"status": False, "message": f"Error{e}"}
