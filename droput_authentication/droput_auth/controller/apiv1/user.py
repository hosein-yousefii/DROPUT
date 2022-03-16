from flask import request
from droput_auth.droput_auth import db
from droput_auth.model import User
from droput_auth.schema.apiv1 import UserSchema
from droput_auth.util import debugiport, now, user_expires_at


class UserController:
	
	def get_users():
		users_schema = UserSchema(many=True)
		try:
			users = User.query.all()
		except:
			return debugiport(status=500,code=102)		# DB ERR
		return debugiport({"users": users_schema.dump(users)})

	def get_user(user_id):
		user_schema = UserSchema()
		try:
			user = User.query.get(user_id)
		except:
			return debugiport(status=500, code=102)		#DB ERR

		if user is None:
			return debugiport(status=404, code=103)		# User not found
		return debugiport({"user": user_schema.dump(user)}, status=201, code=100)

	def create_user():
		if not request.is_json:
			return debugiport(status=415, code=101)		# unsupported request format
		user_schema = UserSchema(only=["username", "password"])
		try:
			data = user_schema.load(request.get_json())
		except:
			return debugiport(status=400, code=104)		# request validation failed

		if not data["username"] or not data["password"]:
			return debugiport(status=400, code=105)  # Empty data.

		try:
			user = User.query.filter_by(username=data["username"]).first()
		except:
			return debugiport(status=500, code=102)		# DB ERR

		if user is not None:
			return debugiport(status=409, code=106)		# user is already exist

		user = User(username=data["username"], password=data["password"])
		db.session.add(user)

		try:
			db.session.commit()
		except:
			db.session.rollback()
			return debugiport(status=500, code=102)		# DB ERR

		user_schema = UserSchema()
		return debugiport({"user": user_schema.dump(user)}, status=201)

	def delete_user(user_id):

		try:
			user = User.query.get(user_id)
		except:
			return debugiport(status=500, code=102)  # DB ERR

		if user is None:
			return debugiport(status=404, code=103)		# user not found

		db.session.delete(user)
		try:
			db.session.commit()
		except:
			db.session.rollback()
			return debugiport(status=500, code=102)  # DB ERR

		return debugiport(status=201,code=100)
