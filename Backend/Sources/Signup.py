from flask_restful import Resource
from Core.Middleware import is_teacher
from Models.Mongodb import users_table, errors
from bcrypt import hashpw, gensalt
from Schemas.StudentSchema import UserAddBase
from flask import request, jsonify
from Curd.StudentAddDatabase import get_student_details_in_excel


class StudentCreateResource(Resource):
    @is_teacher()
    def post(self):
        try:
            file = request.files
            result = get_student_details_in_excel(file["details"])
            if result["status"]:
                users_table.insert_many(result["result"])
                return jsonify({"file": True})
        except Exception as e:
            return {"status": False, "message": f"{e}"}, 409
