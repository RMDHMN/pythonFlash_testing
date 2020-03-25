#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import platform
import netifaces

myApp = Flask(__name__)

@myApp.route('/')
def home():
    data = {'user': 'ramy', 'machine':platform.node(), 'os':platform.system(), 'dist':platform.linux_distribution(), 'interfaces':netifaces.interfaces()}

    return render_template('index.system.html', title='Home', data=data)

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=999)
