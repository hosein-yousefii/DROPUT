from droput_auth.droput_auth import apiv1 as api
from droput_auth.resource.apiv1.user import UserResource


api.add_resource(
    UserResource,
    "/users",
    methods=["GET", "POST"],
    endpoint="users"
)
api.add_resource(
    UserResource,
    "/users/<user_id>",
    methods=["GET", "DELETE"],
    endpoint="user"
)
