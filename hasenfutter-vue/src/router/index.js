import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MenuView from "../views/MenuView.vue";
import LocationsView from "../views/LocationsView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: HomeView },
    { path: "/speisekarte", name: "speisekarte", component: MenuView },
    { path: "/standorte", name: "standorte", component: LocationsView },
  ],
  scrollBehavior(to) {
    if (to.hash) {
      return { el: to.hash, behavior: "smooth" };
    }
    return { top: 0 };
  },
});

export default router;