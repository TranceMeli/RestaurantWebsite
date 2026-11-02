<script setup>
import { onBeforeUnmount, onMounted, ref } from "vue";
import carrotIcon from "../assets/carrot-divider.svg";

// Die Möhren bleiben beim Scrollen direkt unter dem sticky Header stehen,
// im freigehaltenen Seitenrand (siehe `main .container` in base.css).
// Dessen Höhe ändert sich mit der Breite, deshalb wird sie beobachtet.
const headerHeight = ref(0);
let observer;

onMounted(() => {
  const header = document.querySelector(".site-header");
  if (!header) {
    return;
  }
  observer = new ResizeObserver(() => {
    headerHeight.value = header.offsetHeight;
  });
  observer.observe(header);
});

onBeforeUnmount(() => observer?.disconnect());
</script>

<template>
  <div class="header-divider" :style="{ '--header-height': headerHeight + 'px' }">
    <img :src="carrotIcon" alt="" class="carrot-horizontal carrot-left" />
    <img :src="carrotIcon" alt="" class="carrot-horizontal carrot-right" />
  </div>
</template>

<style scoped>
.header-divider {
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--color-cream);
  border-bottom: 1px solid var(--color-border);
}

.carrot-horizontal {
  position: fixed;
  top: calc(var(--header-height) + 45px);
  z-index: 900;
  width: 36px;
  height: auto;
  object-fit: contain;
  pointer-events: none;
}

/* Zahnrad (Original oben) zeigt nach links, Spitze nach innen */
.carrot-left {
  transform: translateY(-50%) rotate(-90deg);
  left: 111px; /* gedreht: sichtbar von 72px bis ca. 186px */
}

/* Zahnrad (Original oben) zeigt nach rechts, Spitze nach innen */
.carrot-right {
  transform: translateY(-50%) rotate(90deg);
  right: 111px;
}

/* Unter 1100px ist im Seitenrand kein Platz für die Möhren, dann entfällt
   auch der leere Trennstreifen. */
@media (max-width: 1100px) {
  .header-divider {
    display: none;
  }
}
</style>
