from flask_restful import Resource
from Core.Middleware import is_teacher
from Models.MongoSchema import Users
from flask import request, jsonify
from Curd.StudentAddDatabase import get_student_details_in_excel


class StudentCreateResource(Resource):
    @is_teacher()
    def post(self):
        try:
            file = request.files
            result = get_student_details_in_excel(file["details"])
            if result["status"]:
                # print(result['result'])
                for student in result["result"]:
                    print(student)
                    user = Users(**student)
                    user.save()
                return jsonify({"file": True})
        except Exception as e:
            return {"status": False, "message": f"{e}"}, 409
