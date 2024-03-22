from flask_restful import Resource, request
from Core.Middleware import is_teacher, get_identity
from Models.MongoSchema import Batch, Users
from datetime import datetime, timedelta
from Curd.QuestionAddDatabase import get_student_details_in_excel
import pytz


class AddBatchResource(Resource):
    @is_teacher()
    def post(self):
        try:
            file = request.files
            data = request.form
            start_time = datetime.strptime(data["start_time"], "%Y-%m-%dT%H:%M:%S")
            end_time = datetime.strptime(data["end_time"], "%Y-%m-%dT%H:%M:%S")
            time_offset = timedelta(hours=5, minutes=30)
            current_time_utc = datetime.utcnow() + time_offset
            if start_time >= end_time or start_time <= current_time_utc:
                return {"status": False, "message": "Check Start time and end time"}
            questions = get_student_details_in_excel(file["questions"])

            teacher = Users.objects(email=get_identity()).first()
            batch = Batch(
                name=data["name"],
                subject=data["subject"],
                description=data["description"],
                Strattime=start_time,
                Endtime=end_time,
                teacher=teacher["user_name"],
                questions=list(questions["result"]),
                assigned_time=current_time_utc,
            )
            print("e")
            batch.save()
            return {"status": True}
        except Exception as e:
            return {"status": False, " message": f"{e}"}
