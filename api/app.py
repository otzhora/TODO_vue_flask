from flask import Flask
from flask_cors import CORS
app = Flask(__name__, static_url_path="")
CORS(app)

from todo import TODO_manager
todo_manager = TODO_manager()

from flask import jsonify
from flask import request
from flask import send_from_directory
from flask import render_template

import os


@app.route('/api')
def main():
    return jsonify(todo_manager.todos)


@app.route('/api/<id>', methods=['GET', 'POST', 'DELETE'])
def manage_todos(id=None):
    if request.method == 'GET':
        return todo_manager.todos[id]
    if request.method == 'POST':
        todo_manager.add(id, request.form['text'])
        return 'OK'
    if request.method == 'DELETE':
        todo_manager.delete(id)
        return 'OK'
    return 'NOT OK'

    

@app.route('/css/<path:path>')
def send_css(path):
    print(os.getcwd() + '/dist/css' + path)
    return send_from_directory(os.getcwd() + '/dist/css', path)


@app.route('/')
def send_index():
    print(os.getcwd())
    print(os.getcwd() + '/dist/')
    return send_from_directory(os.getcwd() + '/dist/', 'index.html')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.getcwd() + '/dist/js',  path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(os.getcwd() + '/dist/img',  path)


if __name__ == '__main__':
    app.run(port=5001)