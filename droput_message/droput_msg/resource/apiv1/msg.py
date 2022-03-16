from flask_restful import Resource
from droput_msg.controller.apiv1 import MsgController


class MsgResource(Resource):
	
	def get(self, user_id=None):
		"""
		GET /msgs --> Get list of messages.
		GET /msgs/<user_id> --> Get message info.
		"""

		if user_id is None:
			return MsgController.get_msgs()
		else:
			return MsgController.get_msg(user_id)
			
	def post(self):
		"""
		POST /msgs --> Create new message.
		POST /msgs/<user_id> --> Not allowed.
		"""
		return MsgController.create_msg()
		
	def delete(self, user_id):
		"""
		DELETE /msgs --> Not allowed.
		DELETE /msgs/<user_id> --> Delete the message.
		"""
		return MsgController.delete_msg(user_id)
