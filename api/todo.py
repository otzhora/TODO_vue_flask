class TODO_manager:
    def __init__(self):
        self.todos = {'1':'test'}
        print('initialized')

    def add(self, todo_id, todo):
        self.todos[todo_id] = todo

    def delete(self, todo_id):
        del self.todos[todo_id]
