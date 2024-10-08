# pip install python-socketio

import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def receive_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://localhost:8080')
    await sio.emit('send_message', {'message': input()})
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())
