from droput_msg.droput_msg import apiv1 as api
from droput_msg.resource.apiv1.msg import MsgResource

api.add_resource(
	MsgResource,
	"/msgs",
	methods=["GET","POST"],
	endpoint="msgs"
)

api.add_resource(
	MsgResource,
	"/msgs/<user_id>",
	methods=["GET","DELETE"],
	endpoint="msg"
)
