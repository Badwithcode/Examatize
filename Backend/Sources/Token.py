from flask_restful import Resource, request
from Core.Middleware import jwt_required, get_claims


class TokenResource(Resource):
    @jwt_required()
    def get(self):
        try:
            claims = get_claims(request.headers["Authorization"].split()[1])
            claims.update({"status": True})
            return claims
        except Exception as e:
            return {"status": False, "message": f"{e}"}
