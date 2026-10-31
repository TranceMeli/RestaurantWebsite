<script setup>
import TheHeader from "./components/TheHeader.vue";
import HeaderDivider from "./components/HeaderDivider.vue";
import TheFooter from "./components/TheFooter.vue";
</script>

<template>
  <div class="side-decor side-decor-left" aria-hidden="true"></div>
  <div class="side-decor side-decor-right" aria-hidden="true"></div>

  <TheHeader />
  <HeaderDivider />
  <main>
    <router-view />
  </main>
  <TheFooter />
</template>

<style scoped>
/* Dekorativer Rand links/rechts, nach dem Möhren-Schema aus der
   Referenzgrafik: schmaler grüner Abschnitt, gefolgt von einem
   größeren goldenen Abschnitt, über die ganze Seite wiederholt. */
.side-decor {
  position: fixed;
  top: 0;
  bottom: 0;
  width: 60px;
  z-index: 1500;
  pointer-events: none;
  background: repeating-linear-gradient(
    to bottom,
    var(--color-forest) 0,
    var(--color-forest) 60px,
    var(--color-honey) 40px,
    var(--color-honey) 300px
  );
}

.side-decor-left {
  left: 0;
}

.side-decor-right {
  right: 0;
}

@media (max-width: 480px) {
  .side-decor {
    width: 8px;
  }
}
</style>