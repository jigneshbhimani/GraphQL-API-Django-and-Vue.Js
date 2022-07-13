<template>
  <div>
    <h4 v-if="loading">Loading...</h4>
    <h1><u>CATEGORY</u></h1>
    <category-item
      v-for="category in categories"
      :key="category.id"
      :category="category"
    >
    </category-item>
  </div>
</template>

<script>
import { CATEGORY_LIST_QUERY } from "../../constant/graphql.js";
import CategoryItem from "./CategoryItem";

export default {
  name: "Book",
  data() {
    return {
      categories: [],
      loading: 0,
    };
  },
  components: {
    CategoryItem,
  },
  apollo: {
    categories: {
      query: CATEGORY_LIST_QUERY,
    },
  },
};
</script>
