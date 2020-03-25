#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
import os

myApp = Flask(__name__)

@myApp.route('/')
def home():
    #concaten = ""
    liste = []
    for parent, dnames, fnames in os.walk("files/"):
        for fname in fnames:
            filename = os.path.join(parent, fname)
            liste.append(filename)
    return render_template('machines.html', liste=liste)

@myApp.route('/<path:path>')
def machines(path):
  contenu = []
  with open(path) as f:
    for line in f:
      contenu.append(line)
  return render_template('contenu.html', contenu=contenu) 


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=999)
