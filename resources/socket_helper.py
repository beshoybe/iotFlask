from flask import json
from database.devices.model import Device

class SocketHelper:

    @staticmethod
    def on_connect(request,socketio):
        print("connected")
        print(request.args)
        query = request.args
        id = query.get("id")
        device = Device.query.get(id)
        if device:
            device.update_connection(value=True)
            socketio.emit("deviceConnection",{"id":id,"connected":True})
    @staticmethod
    def on_disconnect(request,socketio):
        print("disconnected")
        print(request.args)
        query = request.args
        id = query.get("id")
        device = Device.query.get(id)
        if device:
            device.update_connection(value=False)
            socketio.send("deviceConnection",{"id":id,"connected":False})

    @staticmethod
    def on_data(data,socketio,request):
        print(data)
        print(request.args)
        query = request.args
        id = query.get("id")
        device = Device.query.get(id)
        data = json.loads(data)
        rate = str(data.get("rate"))
        quantity = str(data.get("quantity"))
        if device:
            device.update(rate,quantity)
            socketio.emit("dataReceived",{"id":id,"rate":rate,"quantity":quantity})