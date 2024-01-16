import os
from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
import argparse


app = Flask(__name__,
    template_folder='templates',
    static_url_path='', 
    static_folder='static'
)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo1')
def demo1():
    return render_template('multiverse/index.html')

@app.route('/demo2')
def demo2():
    return render_template('parallelism/index.html')

@app.route('/landingtree')
def landingtree():
    return render_template('aerial/index.html')

@app.route('/signup')
def signup():
    return render_template('eventually/index.html')


# Route to serve vooo
#@app.route('/')
#def vooo():
#   return render_template('vooo/index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

