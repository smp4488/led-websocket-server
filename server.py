from led import set_color_hex
import eventlet
import socketio

# sio = socketio.Server()
sio = socketio.Server(cors_allowed_origins=['*'])
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    print('message ', data)

@sio.event
def set_color(sid, data):
    print('set_color ', data)

@sio.event
def set_color_hex(sid, data):
    print('set_color ', data)
    set_color_hex(data)

@sio.event
def get_color(sid, data):
    print('set_color ', data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)