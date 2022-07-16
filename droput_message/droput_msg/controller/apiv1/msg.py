from flask import request
import requests
from sqlalchemy import or_
from droput_msg.config import Config
from droput_msg.droput_msg import db, redis
from droput_msg.model import Msg
from droput_msg.schema.apiv1 import MsgSchema
from droput_msg.util import debugiport, now


class MsgController:

    def get_msgs():

        if redis.exists("msgs_cache"):
            msg_ids = redis.keys("msg:*")
            msgs = []
            for msg_id in msg_ids:
                msg = redis.hgetall(msg_id)
                msgs.append(msg)
            return debugiport({"msgs": msgs})

        msgs_schema = MsgSchema(many=True)
        try:
            msgs = Msg.query.all()
        except:
            return debugiport(status=500, code=102)  #DB ERR

        redis.setex("msgs_cache", Config.REDIS_CACHE_EXPIRE_SECONDS, "yes")
        for msg in msgs:
            redis.hset (
                ":".join(["msg", msg.id]),
                mapping={
                    "id": msg.id,
                    "content": msg.content,
                    "sender": msg.sender,
                    "receiver": msg.receiver
                }
            )

        return debugiport({"msgs": msgs_schema.dump(msgs)})         # return all masgs

    def get_msg(user_id):

        url = Config.USER_AUTH_URL + "/api/v1/users"
        response = requests.get(url=url)
        data = response.json()
        user_exist = 0
        for i in range(0, len(data["users"])):
            if user_id == data["users"][i]["username"]:
                user_exist = 1
                break
        if user_exist != 1:
            return debugiport(status=404, code=103)

        msg_schema = MsgSchema(many=True)
        try:
            msg = Msg.query.filter(or_(Msg.sender == user_id, Msg.receiver == user_id))
        except:
            return debugiport(status=500, code=102)  #DB ERR

        return debugiport({"msg": msg_schema.dump(msg)})                # return user masgs

    def create_msg():

        received_data = request.get_json()
        user = received_data["sender"]

        url = Config.USER_AUTH_URL + "/api/v1/users"
        response = requests.get(url=url)
        data = response.json()

        user_exist = 0

        for i in range(0, len(data["users"])):
            if user == data["users"][i]["username"]:
                user_exist = 1
                break
        if user_exist != 1:
            return debugiport(status=404, code=103)

        if not request.is_json:
            return debugiport(status=415, code=101)
        msg_schema = MsgSchema(only=["sender", "receiver", "content"])
        try:
            data = msg_schema.load(received_data)  # Request validation.
        except:
            return debugiport(status=400, code=104)

        if not data["sender"] or not data["receiver"]:
            return debugiport(status=400, code=105)  # Empty data.

        msg = Msg(sender=data["sender"], receiver=data["receiver"], content=data["content"])

        db.session.add(msg)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return debugiport(status=500, code=102)  # Database error.

        redis.hset (
            ":".join(["msg", msg.id]),
            mapping={
                "id": msg.id,
                "content": msg.content,
                "sender": msg.sender,
                "receiver": msg.receiver
            }
        )

        msg_schema = MsgSchema()
        return debugiport({"msg": msg_schema.dump(msg)}, status=201)

    def delete_msg(msg_id):

        try:
                msg = Msg.query.get(msg_id)
        except:
            return debugiport(status=500, code=102)  # Database error.
        if msg is None:
            return debugiport(status=500, code=103)
        db.session.delete(msg)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return debugiport(status=500, code=102)  # Database error.

        return debugiport(status=201, code=100)

