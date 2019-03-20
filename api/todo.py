

class TODO_manager:
    def init(self):
        self.todos = {}

    def add(self, todo):
        self.todos[todo.id] = todo.body

    def delete(self, todo_id):
        del self.todos[todo_id]