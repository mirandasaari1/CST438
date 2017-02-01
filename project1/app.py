import flask
import os


app = flask.Flask(__name__)

@app.route('/')


def index(quoteAPI=None):
    #print "This is a debug statement!" #prints to terminal

        
    return flask.render_template("index.html", quoteAPI=quoteAPI)

    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)