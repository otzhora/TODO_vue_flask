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
import axios from 'axios'

export default {
  name: 'app',
  components: {
    todos,
    AddTodo
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    delete_todo (id){
      axios.delete(`http://localhost:5001/api/{todo.id}`)
        .then(res => this.todos = this.todos.filter(todo => todo.id !== id))
      
    },
    add_todo(newTodo){
      axios.post(`http://localhost:5001/api/{newTodo.id}`, newTodo.text)
        .then(res => this.todos = [...this.todos, newTodo])
    }
  },
  created() {
    axios.get('http://localhost:5001/api')
      .then(res => {
        this.todos = res.data
        print(res)
      })
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
