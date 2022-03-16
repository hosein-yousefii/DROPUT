from flask_restful import Resource
from droput_auth.controller.apiv1 import UserController


class UserResource(Resource):

    def get(self, user_id=None):
        """
        GET /users --> Get list of users.
        GET /users/<user_id> --> Get user info.
        """
        if user_id is None:
            return UserController.get_users()   # Get list of users.
        else:
            return UserController.get_user(user_id)   # Get user info.

    def post(self):
        """
        POST /users --> Create new user.
        POST /users/<user_id> --> Not allowed.
        """
        return UserController.create_user()   # Create new user.

    def delete(self, user_id):
        """
        DELETE /users --> Not allowed.
        DELETE /users/<user_id> --> Delete the user.
        """
        return UserController.delete_user(user_id)  # Delete the user.

