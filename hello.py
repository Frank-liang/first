#!/usr/bin/env python
##
from flask import Flask,make_response,redirect,abort
app = Flask(__name__)
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s</h1>' %name
@app.route('/redirect')
def redir():
    return redirect('http://www.baidu.com')
@app.route('/use/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>hello,%s</h1>' %use.name

if __name__== '__main__':
    app.run(host='0.0.0.0',port=9999,debug=True)

