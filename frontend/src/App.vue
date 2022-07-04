<template>
    <div id="app">
        <Book />
        <router-view />
    </div>
</template>

<script>
import Book from "./components/Book.vue";

export default {
    components: {
        Book,
    },
};
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
</style>
