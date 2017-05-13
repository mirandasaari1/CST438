import flask
import os
from random import randint



app = flask.Flask(__name__)

@app.route('/')


def index():
    print "This is a debug statement!" #prints to terminal
    #return "Hello, world!" #return html too
    #return "<b>Hello, world!<b>"
    return flask.render_template("index.html")
    
    
@app.route('/random')


def randomPage (random=None):
    random=randint(0,9)
    #return "<h4>" +  str(random) + "</h4>"
    return flask.render_template("index.html", random=random)
    
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return flask.render_template('index.html', name=name)
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)