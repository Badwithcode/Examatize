from flask_restful import Resource, request
from flask import jsonify
from Core.Middleware import jwt_required
from Models.MongoSchema import Batch
from datetime import datetime , timedelta


class TestBatchResource(Resource):
    @jwt_required()
    def get(self, batch_name):
        batch = Batch.objects(name=batch_name).exclude("id").first()
        if batch.Strattime >= datetime.utcnow() +  timedelta(hours=5, minutes=30):
            return jsonify({"status": True, "message": "Test Not Started"})
        questions_response = []
        for question_data in batch.questions:
            question_response = {
                "id": question_data.get("id"),
                "question": question_data.get("question"),
                "options": question_data.get("options"),
                "difficulty": question_data.get("difficulty"),
                "tags": question_data.get("tags"),
            }
            questions_response.append(question_response)
        return jsonify({"status": True, "questions": questions_response})


class ScoreTestResource(Resource):
    @jwt_required()
    def post(self, batch_name):
        data = request.get_json()
        batch = Batch.objects(name=batch_name).exclude("id").first()
        answer_response = []
        for question in batch.questions:
            answer_response.append(question.get("answer"))
        print(answer_response)
        return {"status": True, "message": "Ok", "answers": answer_response}
