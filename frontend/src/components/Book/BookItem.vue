<template>
  <div>
    <h1>{{ book.title }}</h1>
    <p><b>Author: </b>{{ book.author }}</p>
    <p><b>ISBN: </b>{{ book.isbn }}</p>
    <p><b>Pages: </b>{{ book.pages }}</p>
    <p><b>Price: </b>{{ book.price }}</p>
    <p><b>Quantity: </b>{{ book.quantity }}</p>
    <p><b>Description: </b>{{ book.description }}</p>
    <p><b>Status: </b>{{ book.status }}</p>
    <p><b>Date Created: </b>{{ book.date_created }}</p>
  </div>
</template>

<script>
export default {
  name: "BookItem",
  props: ["book"],
};
</script>
