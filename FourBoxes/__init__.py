# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 19:08:40 2019

@author: 은비
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')