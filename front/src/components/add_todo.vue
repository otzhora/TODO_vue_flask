<template>
    <div>
        <form @submit="addTodo">
            <input type="text" name='title' placeholder="add todo" v-model="text">
            <input type="submit" value="Submit" >
        </form>
    </div>
</template>

<script>
import uuid from 'uuid'

export default {
    name: 'AddTodo',
    data() {
        return {
            text: ''
        }
    }, 
    methods: {
        addTodo(e) {
            e.preventDefault();
            
            const newTodo = {
                id: uuid.v4(),
                text: this.text
            }
            this.text = ''
            this.$emit('add-todo', newTodo)
        }
    },
}
</script>

