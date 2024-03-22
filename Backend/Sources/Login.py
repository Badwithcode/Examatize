from flask import request
from flask_restful import Resource
from Models.Redis import r_conn
from Core.Middleware import create_access_token, jwt_required, get_identity
from pydantic import ValidationError
from Schemas.LoginSchema import LoginBase


from Models.MongoSchema import Users


class LoginResource(Resource):
    def post(self):
        try:
            data = LoginBase.model_validate(
                request.json
            ).model_dump()  # Data Validation
            # Get values from request
            email = data["email"]
            password = data["password"]
            # check if user exists in database
            user = Users.objects(email=email).first()
            if user is not None and user.check_password(password=password):
                role_db = user.role  # Accessing role directly from the user instance
                access_token = create_access_token(
                    identity=email, payload={"role": role_db}
                )
                r_conn.setex(
                    f"access_token:{email}", time=60 * 60 * 24, value=access_token
                )
                return {"status": True, "access_token": access_token}, 200
            return {
                "status": False,
                "message": "User Not Found or Invalid Password",
            }, 401
        except ValidationError as e:
            return {
                "status": False,
                "message": {
                    "username": "Should end with @sece.ac.in",
                    "password": "Has Length more than 8",
                },
            }, 400
        except KeyError as e:
            return {"status": False, "message": str(e)}, 400
        except Exception as e:
            return {"status": False, "message": str(e)}, 500


class LogoutResource(Resource):
    @jwt_required()
    def get(self):
        try:
            identity = get_identity()
            r_conn.delete(f"access_token:{identity}")
            return {"status": True}, 200
        except Exception as e:
            return {"status": False, "message": f"Error: {e}"}, 400
