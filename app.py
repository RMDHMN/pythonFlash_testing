#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
myApp = Flask(__name__)

@myApp.route('/')
def bonjour():
    message = 'Bonjour, je suis Ramy \n'
    return message

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=8080)
