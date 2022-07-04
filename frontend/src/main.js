import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import Vue from "vue";
import VueApollo from "vue-apollo";

import App from "./App";

Vue.config.productionTip = false;

const httpLink = new HttpLink({
    uri: "http://127.0.0.1:8000/graphql",
});

const apolloClient = new ApolloClient({
    link: httpLink,
    cache: new InMemoryCache(),
    connectToDevTools: true,
});

Vue.use(VueApollo);

const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
});

new Vue({
    el: "#app",
    provide: apolloProvider.provide(),
    render: (h) => h(App),
});
