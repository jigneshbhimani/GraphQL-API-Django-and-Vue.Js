<template>
  <div id="app">
    <div class="container">
      <div class="card">
        <div class="card-body">
          <Category />
        </div>
      </div>
    </div>
    <br />
    <hr />
    <br />
    <div class="container">
      <div class="card">
        <div class="card-body">
          <Book />
        </div>
      </div>
    </div>
    <br />
    <hr />
    <br />
    <div class="container">
      <div class="card">
        <div class="card-body">
          <Grocery />
        </div>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
import Book from "./components/Book/Book.vue";
import Category from "./components/Category/Category.vue";
import Grocery from "./components/Grocery/Grocery.vue";

export default {
  components: {
    Book,
    Category,
    Grocery,
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
