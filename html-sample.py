#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
myApp = Flask(__name__)

@myApp.route('/')
def home():
    return '''
<html>
    <head>
        <title>Home Page<title>
    </head>
    <body>
        <h1>Hello, ramy</h1>
    </body>
</html>'''

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=999)
