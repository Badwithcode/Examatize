from flask import jsonify, request
from flask_restful import Resource
from Models.Mongodb import users_table
from Models.Redis import r_conn
from Core.Middleware import create_access_token, jwt_required, get_identity
from pydantic import BaseModel, Field, ValidationError


class LoginBase(BaseModel):
    username: str = Field(pattern='^[a-zA-Z0-9._%+-]+@sece\.ac\.in$')
    password: str = Field(min_length=6)



class LoginResource(Resource):
    def post(self):
        try:
            data = LoginBase.model_validate(request.json).model_dump() # Data Validation
            # Get value from user
            username = data["username"]
            password = data["password"]
            # check if user exist in database
            user = users_table.find_one({"user_name": username})
            if user == None:
                return {"status": "Username Not found"}, 401
            # Get value from database by check the db with username and password
            username_db = user["user_name"]
            email_db = user["email"]
            role_db = user["role"]
            password_db = user["password"]
            # Check if username and password is correct
            if username_db == username and password_db == password:
                access_token = create_access_token(
                    identity=email_db, payload={"role": role_db}
                )
                r_conn.setex(
                    f"access_token:{email_db}", time=60 * 60 * 24, value=access_token
                )
                return {"status": True, "access_token": access_token}, 200
            else:
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
