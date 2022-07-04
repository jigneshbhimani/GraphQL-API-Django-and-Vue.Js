<template>
    <div>
        <h1>
            {{ book.title }}
        </h1>
        <p>{{ book.author }}</p>
        <p>{{ book.isbn }}</p>
        <p>{{ book.pages }}</p>
        <p>{{ book.price }}</p>
        <p>{{ book.quantity }}</p>
        <p>{{ book.description }}</p>
        <p>{{ book.status }}</p>
        <p>{{ book.date_created }}</p>
    </div>
</template>

<script>
export default {
    name: "BookItem",
    props: ["book"],
};
</script>
