import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./style/variables.css";
import "./style/base.css";

createApp(App).use(router).mount("#app");