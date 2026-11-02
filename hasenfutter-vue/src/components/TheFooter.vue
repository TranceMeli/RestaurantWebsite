<script setup>
const year = new Date().getFullYear();
</script>

<template>
  <footer class="site-footer">
    <div class="container footer-content">
      <div>
        <span class="brand-name">Hasenfutter</span>
        <p>Freude am Mümmeln.</p>
      </div>

      <nav class="footer-links" aria-label="Footer-Navigation">
        <router-link to="/">Startseite</router-link>
        <router-link to="/speisekarte">Speisekarte</router-link>
        <router-link to="/standorte">Standorte</router-link>
        <router-link to="/#buchen">Buchen</router-link>
        <router-link to="/#kontakt">Kontakt</router-link>
      </nav>
    </div>

    <div class="container footer-legal">
      <p>&copy; {{ year }} Hasenfutter. Fiktives Restaurant, Portfolio-Projekt.</p>
      <nav class="footer-links" aria-label="Rechtliches">
        <router-link to="/impressum">Impressum</router-link>
        <router-link to="/datenschutz">Datenschutz</router-link>
      </nav>
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  padding: 2.5rem 0;
  background: var(--color-forest-dark);
  color: hsl(0 0% 100% / 0.88);
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  flex-wrap: wrap;
}

.brand-name {
  color: var(--color-honey);
  font-family: var(--font-heading);
  font-size: 1.4rem;
  font-weight: 700;
}

.footer-content p {
  margin: 0.2rem 0 0;
  color: hsl(0 0% 100% / 0.65);
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
}

.footer-links a {
  color: hsl(0 0% 100% / 0.78);
}

.footer-links a:hover {
  color: var(--color-honey);
}

.footer-legal {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 1.75rem;
  padding-top: 1.25rem;
  border-top: 1px solid hsl(0 0% 100% / 0.15);
  font-size: 0.88rem;
}

.footer-legal p {
  margin: 0;
  color: hsl(0 0% 100% / 0.65);
}

@media (max-width: 720px) {
  .footer-content {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
