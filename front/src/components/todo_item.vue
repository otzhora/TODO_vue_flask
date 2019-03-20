<template>
    <div>
        <p> {{ todo.text }} </p>
        <button @click="$emit('del-todo', todo.id)"> x </button>
    </div>
</template>


<script>
export default {
    name: 'todoItem',
    props: ['todo']
}
</script>

<style scoped>
div{
    display: flex;
    align-content: center;
    justify-content: space-between;
    text-align: center;
}
</style>
