import jwt
from datetime import datetime, timedelta
from flask import current_app
from config import SECRET_KEY


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(seconds=900)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def verify_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return payload
