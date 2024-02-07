from flask_restful import Resource, request
from Models.Mongodb import users_table
from bcrypt import checkpw, hashpw, gensalt


class PasswordResource(Resource):
    def put(self):
        try:
            data = request.get_json()
            email = data["email"]
            old_password = data["old_password"]
            new_password = data["new_password"]
            user = users_table.find_one({"email": email})
            if checkpw(old_password.encode("utf-8"), user["password"]):
                new_hash_password = hashpw(new_password.encode("utf-8"), gensalt())
                users_table.update_one(
                    {"email": email}, {"$set": {"password": new_hash_password}}
                )
                return {"status": True}
            return {"status": False, "message": "Invalid Old password"}
        except Exception as e:
            return {"status": False, "message": f"Error{e}"}
