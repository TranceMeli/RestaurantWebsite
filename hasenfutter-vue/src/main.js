import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "@fontsource/lora/400.css";
import "@fontsource/lora/500.css";
import "@fontsource/lora/600.css";
import "@fontsource/lora/700.css";
import "@fontsource/lora/400-italic.css";
import "./style/variables.css";
import "./style/base.css";

createApp(App).use(router).mount("#app");