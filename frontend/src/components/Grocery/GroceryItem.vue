<template>
  <div>
    <h1>{{ grocery.name }}</h1>
    <p><b>Product Tag: </b>{{ grocery.productTag }}</p>
    <p><b>Category: </b>{{ grocery.category.title }}</p>
    <p><b>Price: </b>{{ grocery.price }}</p>
    <p><b>Quantity: </b>{{ grocery.quantity }}</p>
    <p><b>Image URL: </b>{{ grocery.imageurl }}</p>
    <p><b>Status: </b>{{ grocery.status }}</p>
    <p><b>Date Created: </b>{{ grocery.dateCreated }}</p>
  </div>
</template>

<script>
export default {
  name: "GroceryItem",
  props: ["grocery"],
};
</script>
