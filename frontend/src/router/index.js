import Vue from "vue";
import VueRouter from "vue-router";
import Book from "@/components/Book.vue";
import Grocery from "@/components/Grocery.vue";
import Category from "@/components/Category.vue";

Vue.use(VueRouter);

const routes = [
  { path: "/", component: Category },
  { path: "/book", component: Book },
  { path: "/grocery", component: Grocery },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
