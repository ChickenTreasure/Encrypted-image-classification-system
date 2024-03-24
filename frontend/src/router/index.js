import Vue from "vue";
import Router from "vue-router";
// import Login from "@/views/Login"

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            name: "login",
            component: () => import("@/views/Login.vue"), 
        },
        {
            path: "/search",
            name: "search",
            component: () => import("@/views/Search.vue"),
        },
        {
            path: "/collect",
            name: "collect",
            component: () => import("@/views/Collection.vue"),
        }
    ]
});
