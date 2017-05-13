import os
import flask
import flask_socketio
#import flask_sqlalchemy

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

#import models


@app.route('/')
# def index():
    # messages = models.Message.query.all()
    # html = ['<li>' + m.text + '</li>' for m in messages]
    # return '<ul>' + ''.join(html) + '</ul>'
    
def hello():
    return flask.render_template('myindex.html')


@socketio.on('connect')
def on_connect():
    print 'Someone connected!'

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'

all_messages=[]
@socketio.on('new message')
def on_new_message(data):
    print "Got an event for new message with data:", data
    all_messages.append=(data['message'])
    socketio.emit('all messages',{
        'messages' : all_messages})
    
if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

