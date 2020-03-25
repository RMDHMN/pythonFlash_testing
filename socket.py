#!/usr/bin/python
from flask import Flask, render_template
import socket
app = Flask(__name__)


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    message = "Bonjour, je suis " + hostname + "\n"
    data = {'user': 'rami', 'machine': hostname}
    return render_template('index.html', title='Home Page', data=data)

@app.route('/toto')
def simple():
    hostname = socket.gethostname()
    message = "Bonjour  " + hostname + "\n"
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0')
