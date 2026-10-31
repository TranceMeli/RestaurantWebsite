<script setup>
import heroRestaurant from "../assets/images/hero-restaurant.jpg";
</script>

<template>
  <section id="willkommen" class="hero section">
    <div class="hero-content container">
      <div class="hero-text">
        <p class="eyebrow">Willkommen bei Hasenfutter</p>
        <h1>Gutes Essen.<br /><span>Gute Gesellschaft.</span></h1>
        <p class="hero-description">
          Ein gemütlicher Ort für besondere Abende, entspanntes Essen und
          kleine Genussmomente.
        </p>

        <div class="hero-actions">
          <a class="button button-primary" href="#buchen">Tisch buchen</a>
          <a class="button button-secondary" href="#restaurant">Restaurant entdecken</a>
        </div>
      </div>

      <div class="hero-image">
        <img :src="heroRestaurant" alt="Gastraum im Hasenfutter mit warmem Licht und gedeckten Tischen" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: calc(100vh - 76px);
  display: flex;
  align-items: center;
  background:
    radial-gradient(circle at 80% 20%, hsl(35 92% 58% / 0.14), transparent 32%),
    linear-gradient(135deg, var(--color-cream), var(--color-linen));
}

.hero-content {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  align-items: center;
  gap: 5rem;
}

.hero-text {
  max-width: 650px;
}

.hero-description {
  max-width: 560px;
  margin-bottom: 2rem;
  color: var(--color-ink-soft);
  font-size: 1.15rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem;
}

.hero-image {
  min-height: 320px;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

@media (max-width: 900px) {
  .hero-content {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .hero {
    min-height: auto;
    padding-top: 5rem;
    padding-bottom: 5rem;
  }
}

@media (max-width: 480px) {
  .hero-actions {
    flex-direction: column;
  }

  .hero-actions .button {
    width: 100%;
  }
}
</style>