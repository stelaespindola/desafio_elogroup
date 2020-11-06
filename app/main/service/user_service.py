import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        new_user = User(data['username'])
        new_user.set_password(data['password'])
        save_changes(new_user)
        response_object = {
            'method': 'save_new_user',
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'method': 'save_new_user',
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()

def get_a_user(token):
    return User.get_user_by_token(token);

def generate_token(user):
    try:
        auth_token = user.get_token()
        response_object = {
            'method': 'generate_token',
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'method': 'generate_token',
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()
