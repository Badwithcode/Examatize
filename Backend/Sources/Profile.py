from flask_restful import Resource, request
from Core.Middleware import jwt_required, get_claims
from Models.MongoSchema import Users


class ProfileResource(Resource):
    @jwt_required()
    def get(self):
        try:
            claims = get_claims(request.headers["Authorization"].split()[1])
            user_data = (
                Users.objects(email=claims["sub"])
                .exclude("id")
                .exclude("password")
                .first()
            )
            user_dict = user_data.to_mongo().to_dict()
            return {"status": True, "User": user_dict}
        except Exception as e:
            return {"status": False, "message": f"{e}"}
