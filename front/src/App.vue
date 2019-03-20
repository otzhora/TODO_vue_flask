<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <AddTodo v-on:add-todo='add_todo'/>
    <todos v-bind:todos='todos' v-on:del-todo='delete_todo' />
  </div>
</template>

<script>
import todos from './components/todos'
import AddTodo from './components/add_todo'

export default {
  name: 'app',
  components: {
    todos,
    AddTodo
  },
  data() {
    return {
      todos: [{
        'id': 1,
        'text': 'ses'
      },
      {
        'id': 2,
        'text': 'kek'
      },
      {
        'id': 3,
        'text': 'lol'
      }]
    }
  },
  methods: {
    delete_todo (id){
      this.todos = this.todos.filter(todo => todo.id !== id)
      
    },
    add_todo(newTodo){
      this.todos = [...this.todos, newTodo]
    }
  },
  created() {
    // TODO
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
