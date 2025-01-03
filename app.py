from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS

from resources.socket_helper import SocketHelper

app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*", async_mode='eventlet')



 
@app.route('/') 
def hello(): 
    return 'Hello, World!'

from database.database import init_database
init_database(app)

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    SocketHelper.on_connect(request,socketio)

@socketio.on('data')
def handle_message(data):
    """event listener when client types a message"""
    SocketHelper.on_data(data,socketio,request)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    SocketHelper.on_disconnect(request,socketio)

