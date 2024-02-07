from flask import jsonify, request
from flask_restful import Resource
from Models.Mongodb import users_table
from Models.Redis import r_conn
from Core.Middleware import create_access_token, jwt_required, get_identity
from pydantic import ValidationError
from Schemas.LoginSchema import LoginBase
from bcrypt import checkpw



class LoginResource(Resource):
    def post(self):
        try:
            data = LoginBase.model_validate(request.json).model_dump() # Data Validation
            # Get value from user
            email = data["email"]
            password = data["password"]
            # check if user exist in database
            user = users_table.find_one({"email": email})
            if user != None:
                if checkpw(password.encode('utf-8'),user['password']):
                    role_db = user["role"]
                    access_token = create_access_token(
                        identity=email, payload={"role": role_db}
                    )
                    r_conn.setex(
                        f"access_token:{email}", time=60 * 60 * 24, value=access_token
                    )
                    return {"status": True, "access_token": access_token}, 200
            return {"status": False, 'message':'User Not Found'}, 401
        except ValidationError as e:
            return {'status':False, 'message':{
                'username': 'Should end with @sece.ac.in',
                'password': 'Has Length moredhan 8'
            }}
        except KeyError as e:
            return {"status": False, "message": str(e)}, 400
        except Exception as e:
            return {"status": False, "message": str(e)}, 500


class LogoutResource(Resource):
    @jwt_required()
    def post(self):
        try:
            identity = get_identity()
            r_conn.delete(f"access_token:{identity}")
            return {"status": True}, 200
        except Exception as e:
            return {"status": False, "message": f"Error: {e}"}, 400
