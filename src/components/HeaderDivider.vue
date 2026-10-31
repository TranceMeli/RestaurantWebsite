<script setup>
import carrotIcon from "../assets/carrot-divider.svg";
</script>

<template>
  <div class="header-divider">
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
  width: 100px;
  height: auto;
  object-fit: contain;
}

/* Zahnrad (Original oben) zeigt nach links, Spitze nach innen */
.carrot-left {
  transform: rotate(-90deg);
  margin-left: 10rem;
}

/* Zahnrad (Original oben) zeigt nach rechts, Spitze nach innen */
.carrot-right {
  transform: rotate(90deg);
  margin-right: 10rem;
}

@media (max-width: 480px) {
  .carrot-horizontal {
    width: 40px;
    height: 120px;
  }
}
</style>