from flask import request
from flask_restful import Resource
from app import db
from models import User

class UserResource(Resource):

    def get(self,user_id):
        user = User.query.get(user_id)
        return user.serialize()
    
    def post(self):
        user = User(username=request.json['username'],
                    email=request.json['email'],
                    password=request.json['password'])
        db.session.add(user)
        db.session.commit()
        return user.serialize(), 201
    
class UserListResource(Resource):

    def get(self):
        users = User.query.all()
        return [user.serialize() for user in users]
    