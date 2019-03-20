from flask import Flask
app = Flask(__name__)

from todo import TODO_manager
todo_manager = TODO_manager()

from flask import jsonify
from flask import request

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

    
if __name__ == '__main__':
    app.run(port=5001)