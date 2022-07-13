<template>
  <div>
    <h4 v-if="loading">Loading...</h4>
    <h1><u>BOOK</u></h1>
    <book-item v-for="book in books" :key="book.id" :book="book"> </book-item>
  </div>
</template>

<script>
import { BOOK_LIST_QUERY } from "../../constant/graphql.js";
import BookItem from "./BookItem";

export default {
  name: "Book",
  data() {
    return {
      books: [],
      loading: 0,
    };
  },
  components: {
    BookItem,
  },
  apollo: {
    books: {
      query: BOOK_LIST_QUERY,
    },
  },
};
</script>
