<template>
  <div>
    <h4 v-if="loading">Loading...</h4>
    <h1><u>GROCERY</u></h1>
    <grocery-item
      v-for="grocery in groceries"
      :key="grocery.id"
      :grocery="grocery"
    >
    </grocery-item>
  </div>
</template>

<script>
import { GROCERY_LIST_QUERY } from "../../constant/graphql.js";
import GroceryItem from "./GroceryItem";

export default {
  name: "Grocery",
  data() {
    return {
      groceries: [],
      loading: 0,
    };
  },
  components: {
    GroceryItem,
  },
  apollo: {
    groceries: {
      query: GROCERY_LIST_QUERY,
    },
  },
};
</script>
