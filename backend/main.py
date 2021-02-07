import flask
from flask import render_template 
import pymongo


app = flask.Flask("__main__")
#routing to the landing page of site. 
@app.route("/")
def my_index():
    return flask.render_template("index.html")

app.run(debug=True)