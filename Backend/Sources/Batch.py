from flask_restful import Resource
from flask import jsonify
from Core.Middleware import jwt_required
from Models.MongoSchema import Batch, Q
from datetime import datetime, timedelta


class UpcomingTestResource(Resource):
    @jwt_required()
    def get(self):
        print("Upcoming")
        try:
            time_offset = timedelta(hours=5, minutes=30)
            current_time_utc = datetime.utcnow() + time_offset
            batches = (
                Batch.objects(Q(Strattime__gt=current_time_utc))
                .exclude("questions", "id")
            )
            batch_dicts = []
            for batch in batches:
                batch_dict = batch.to_mongo()
                batch_dicts.append(batch_dict)
            print(batches)
            return jsonify({"status": True, "Batches": batch_dicts})
        except Exception as e:
            return {"status": False, "message": str(e)}


class TestResource(Resource):
    @jwt_required()
    def get(self):
        try:
            batches = (
                Batch.objects()
                .exclude("questions", "id")
                .only("Strattime", "description", "name", "teacher")
            )
            batch_dicts = []
            for batch in batches:
                batch_dict = batch.to_mongo()
                batch_dicts.append(batch_dict)
            return jsonify({"status": True, "Batches": batch_dicts})
        except Exception as e:
            return {"status": False, "message": str(e)}


class CompletedTestResource(Resource):
    @jwt_required()
    def get(self):
        try:
            time_offset = timedelta(hours=5, minutes=30)
            current_time_utc = datetime.utcnow() + time_offset
            batches = (
                Batch.objects(Q(Strattime__lt=current_time_utc))
                .exclude("questions", "id")
                .only("Strattime", "description", "name", "teacher")
            )
            batch_dicts = []
            for batch in batches:
                batch_dict = batch.to_mongo()
                batch_dicts.append(batch_dict)
            return jsonify({"status": True, "Batches": batch_dicts})
        except Exception as e:
            return {"status": False, "message": str(e)}
