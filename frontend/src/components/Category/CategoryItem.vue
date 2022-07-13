<template>
  <div class="category">
    <p><b>Title: </b>{{ category.title }}</p>
  </div>
</template>

<script>
export default {
  name: "CategoryItem",
  props: ["category"],
};
</script>
