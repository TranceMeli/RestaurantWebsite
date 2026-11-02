<script setup>
import { onBeforeUnmount, onMounted, ref } from "vue";
import logo from "../assets/logo.svg";

const isOpen = ref(false);

// Der Header ist fixiert und schrumpft beim Scrollen. Ein Platzhalter in
// voller Höhe hält den Platz frei, damit der Inhalt dabei nicht springt.
const headerEl = ref(null);
const isScrolled = ref(false);
const fullHeight = ref(0);

// Gemessen wird nur im aufgeklappten Zustand und nicht mittendrin in der
// Animation. Die Pause entspricht der Dauer der Logo-Transition.
let animating = false;
let animationTimer;
let observer;

function measure() {
  if (!isScrolled.value && !animating && headerEl.value) {
    fullHeight.value = headerEl.value.offsetHeight;
  }
}

function onScroll() {
  // Zwei Schwellen, damit der Zustand an der Grenze nicht flackert.
  const shouldShrink = isScrolled.value ? window.scrollY >= 10 : window.scrollY > 40;
  if (shouldShrink === isScrolled.value) {
    return;
  }
  isScrolled.value = shouldShrink;
  animating = true;
  clearTimeout(animationTimer);
  animationTimer = setTimeout(() => {
    animating = false;
    measure();
  }, 300);
}

onMounted(() => {
  measure();
  onScroll();
  observer = new ResizeObserver(measure);
  observer.observe(headerEl.value);
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", measure);
});

onBeforeUnmount(() => {
  observer?.disconnect();
  clearTimeout(animationTimer);
  window.removeEventListener("scroll", onScroll);
  window.removeEventListener("resize", measure);
});

function toggleMenu() {
  isOpen.value = !isOpen.value;
}

function closeMenu() {
  isOpen.value = false;
}
</script>

<template>
  <div class="header-slot" :style="{ height: fullHeight ? fullHeight + 'px' : undefined }">
  <header ref="headerEl" class="site-header" :class="{ 'is-scrolled': isScrolled }">
    <nav class="navbar container" aria-label="Hauptnavigation">
      <router-link class="brand" to="/" aria-label="Hasenfutter Startseite" @click="closeMenu">
        <img :src="logo" alt="Hasenfutter" class="brand-logo" />
      </router-link>

      <button
        class="nav-toggle"
        type="button"
        :aria-expanded="isOpen"
        aria-label="Menü öffnen"
        @click="toggleMenu"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>

      <ul class="nav-links" :class="{ 'is-open': isOpen }">
        <li><router-link to="/#willkommen" @click="closeMenu">Willkommen</router-link></li>
        <li><router-link to="/#restaurant" @click="closeMenu">Über das Restaurant</router-link></li>
        <li><router-link to="/speisekarte" @click="closeMenu">Speisekarte</router-link></li>
        <li><router-link to="/standorte" @click="closeMenu">Standorte</router-link></li>
        <li><router-link class="nav-button" to="/#buchen" @click="closeMenu">Buchen</router-link></li>
        <li><router-link to="/#kontakt" @click="closeMenu">Kontakt</router-link></li>
      </ul>
    </nav>
  </header>
  </div>
</template>

<style scoped>
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: hsl(0 0% 100% / 0.94);
  border-bottom: 1px solid var(--color-border);
  backdrop-filter: blur(10px);
}

.navbar {
  min-height: 92px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-start;
  gap: 1rem 2rem;
  padding-block: 0.5rem;
}

.brand {
  display: inline-flex;
  align-items: center;
  flex-shrink: 0;
}

.brand-logo {
  height: 200px;
  width: auto;
  transition: height 0.25s ease;
}

.site-header.is-scrolled .brand-logo {
  height: 72px;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem clamp(0.75rem, 2vw, 1.6rem);
  list-style: none;
  margin: 0 0 0 auto;
  padding: 0;
}

.nav-links a {
  display: inline-block;
  white-space: nowrap;
  color: var(--color-ink);
  font-size: 0.95rem;
  font-weight: 600;
  transition: color var(--transition);
}

.nav-links a:hover {
  color: var(--color-forest-light);
}

.nav-links .nav-button {
  padding: 0.7rem 1.15rem;
  border-radius: 999px;
  background: var(--color-forest);
  color: white;
}

.nav-links .nav-button:hover {
  background: var(--color-forest-dark);
  color: white;
}

.nav-toggle {
  display: none;
  width: 44px;
  height: 44px;
  padding: 0.65rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-white);
}

.nav-toggle span {
  display: block;
  width: 100%;
  height: 2px;
  margin: 5px 0;
  background: var(--color-ink);
}

@media (max-width: 720px) {
  .navbar {
    min-height: 76px;
  }

  .brand-logo,
  .site-header.is-scrolled .brand-logo {
    height: 38px;
  }

  .nav-toggle {
    display: block;
    margin-left: auto;
  }

  .nav-links {
    position: absolute;
    inset: 68px 1rem auto 1rem;
    margin: 0;
    display: none;
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
    padding: 1rem;
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    background: var(--color-white);
    box-shadow: var(--shadow-md);
  }

  .nav-links.is-open {
    display: flex;
  }

  .nav-links a {
    display: block;
    padding: 0.7rem;
  }

  .nav-links .nav-button {
    text-align: center;
  }
}
</style>