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

async function get_todos() {
  let posts = await axios.get('http://localhost:5001/api')
  posts = posts.data
  let todos = []
  for(let key in posts) {
    todos = [...todos, {
      'id': key,
      'text': posts[key]
    }]
  }
  return todos
}

function get_id(todos) {
  let id = 0
  for(let todo in todos) {
    id = id > parseInt(todos[todo]['id']) ? id :parseInt(todos[todo]['id'])
  }
  return id + 2
}

export default {
  name: 'app',
  components: {
    todos,
    AddTodo
  },
  data() {
    return {
      todos: [],
      id: 1
    }
  },
  methods: {
    async delete_todo (id){
      await axios.delete(`http://localhost:5001/api/${id}`)

      this.todos = await get_todos()
    },
    async add_todo(newTodo){
      let id = get_id(this.todos)
      
      await axios.post(`http://localhost:5001/api/${id}`, {
        data: {
          'text': newTodo['text']
        }, 
        headers: {
          'Content-Type': 'application/json'
        }
      })
      this.todos = await get_todos()
    }
  },
  async created() {
    this.todos = await get_todos()
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
