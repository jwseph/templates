# pip install python-socketio

import socketio

from urllib.parse import parse_qs
import uuid
from collections import defaultdict

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio, socketio_path='/socket.io')

@sio.event
async def connect(sid, environ):
    print('connect', sid)
    query = parse_qs(environ['QUERY_STRING'])
    username, password = query['username'][0], query['password'][0]
    assert accounts[username]['password'] == password
    uid = str(uuid.uuid4())
    async with sio.session(sid) as session:
        # save sesison info

@sio.event
async def chat_message(sid, data):
    print(f'{sid=} {data=}')

@sio.event
async def disconnect(sid):
    print('disconnect', sid)
    async with sio.session(sid) as session:
        # remove session info

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)
