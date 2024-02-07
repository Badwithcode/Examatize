import jwt
from dotenv import load_dotenv
import os
import time
from functools import wraps
from flask import request
<<<<<<< HEAD

=======
from Models.Redis import r_conn
>>>>>>> ea3d47b221642f9ea068505dc81786f8e43b0163

load_dotenv()


SECRET_KEY = os.environ.get("secret_key")
JWT_ALGORITHM = os.environ.get(
    "jwt_algorithm", "HS256"
)  # Mostly they use HS256 algorithm to make create jwt
ACCESS_TOKEN_EXPIRE_TIME = 60 * 60 * 24


def create_access_token(identity: any, payload: dict):
    payload.update(
        {
            "sub": identity,
            "iat": int(time.time()),
            "exp": int(time.time()) + ACCESS_TOKEN_EXPIRE_TIME,
        }
    )
    access_token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=JWT_ALGORITHM)
    return access_token


def get_claims(token: str) -> dict:
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=JWT_ALGORITHM)
        exist_token = r_conn.get(f'access_token:{payload["sub"]}')
        if exist_token != token.encode('utf-8'):
            raise Exception("Invalid/Old Token")
        return payload
    except jwt.exceptions.InvalidSignatureError:
        raise ValueError("Invalid Secret key")
    except jwt.exceptions.InvalidAlgorithmError:
        raise ValueError("Invalid Algorithm")
    except jwt.exceptions.ExpiredSignatureError:
        raise ValueError("Token Expired")
    except Exception as e:
        raise Exception(f'{e}')


def is_bearer(auth_token):
    try:
        splitted_token = auth_token.split()
        if splitted_token[0] == "Bearer":
            return splitted_token[1]
        raise ValueError("This is not at Bearer Schema")
    except:
        raise ValueError("Not a bearar Token")


def get_token_from_header():
    try:
        Auth_token = request.headers["Authorization"]
        token = is_bearer(Auth_token)
        return token
    except:
        raise ValueError("No token is available in header")


def get_role():
    token = get_token_from_header()
    claims = get_claims(token)
    return claims["role"]


def get_identity():
    token = get_token_from_header()
    claims = get_claims(token)
    return claims["sub"]


def is_teacher():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                token = get_token_from_header()
                claims = get_claims(token)
                if claims["role"] == "teacher":
                    return fn(*args, **kwargs)
                else:
                    raise ValueError( "Invalid Access")
            except Exception as e:
                return {'status':False,'message':f'{e}'}, 401

        return decorator

    return wrapper


def is_student():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                token = get_token_from_header()
                claims = get_claims(token)
                if claims["role"] == "student":
                    return fn(*args, **kwargs)
                else:
                    raise ValueError( "Invalid Access")
            except Exception as e:
                return {'status':False,'message':f'{e}'}, 401

        return decorator

    return wrapper


def is_admin():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                token = get_token_from_header()
                claims = get_claims(token)
                if claims["role"] == "admin":
                    return fn(*args, **kwargs)
                else:
                    raise ValueError( "Invalid Access")
            except Exception as e:
                return {'status':False,'message':f'{e}'}, 401

        return decorator

    return wrapper


def jwt_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                token = get_token_from_header()
                claims = get_claims(token)
                return fn(*args, **kwargs)
            except Exception as e:
                return {'status':False,'message':f'{e}'}, 401

        return decorator
    return wrapper
