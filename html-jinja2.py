#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
myApp = Flask(__name__)

@myApp.route('/')
def home():
    data = {'user': 'ramy', 'machine':'fedora31'}

    return render_template('index.html', title='Home', data=data)

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=999)
