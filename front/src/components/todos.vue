<template>
    <div class='todo_cont'>
        <div class='todo' v-for='todo in todos' v-bind:key='todo.id'>
            <todoItem v-bind:todo='todo' v-on:del-todo='$emit("del-todo", todo.id)'/>
        </div>
    </div>
</template>

<script>
import todoItem from './todo_item'

export default {
    name: 'Todos',
    components: {
        todoItem
    },
    props: ['todos']
}
</script>

<style scoped>
.todo_cont{
    margin: auto;
    width: 50%;
    text-align: center;
}
</style>
