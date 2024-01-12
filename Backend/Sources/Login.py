from flask import jsonify,request
from flask_restful import Resource
from Models.Mongodb import users_table
from Models.Redis import r_conn
from Core.Middleware import create_access_token
# db = client['your_database_name']

users_collection = users_table


class LoginResource(Resource):
    # def get(self, username):
    #     if username in users:
    #         return {'username': users[username]['username']}
    #     else:
    #         return {'message': 'User not found'}, 404
    def post(self):
        try:
            data=request.json
            # Get value from user
            username = data['username']
            password = data['password']
            # check if user exist in database
            user = users_collection.find_one({'user_name':username})
            if(user==None):
                return {'status': 'Username Not found'}, 401
            
            # Get value from database by check the db with username and password
            username_db = user["user_name"]
            email_db = user["email"]
            role_db=user["role"]
            password_db = user["password"]

            # Check if username and password is correct
            if(username_db==username and password_db==password):
                print("success")
                access_token = create_access_token(identity=email_db, payload={'role': role_db})
                r_conn.setex(f"access_token:{email_db}", time=60 * 60 * 24, value=access_token)
                return {'status': True, 'access_token': access_token}, 200
            else:
                print("username not found")
                return {'status': 'Username Not found'}, 401
            
        except KeyError as e:
            return {'status': 'failed', 'message': str(e)}, 400
        except Exception as e:
            return {'status': 'failed', 'message': str(e)}, 500