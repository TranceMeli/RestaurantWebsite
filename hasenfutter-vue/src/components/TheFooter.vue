<script setup></script>

<template>
  <footer class="site-footer">
    <div class="container footer-content">
      <div>
        <span class="brand-name">Hasenfutter</span>
        <p>Freude am Mümmeln.</p>
      </div>

      <div class="footer-links">
        <a href="#willkommen">Startseite</a>
        <a href="#restaurant">Restaurant</a>
        <a href="#buchen">Buchen</a>
        <a href="#kontakt">Kontakt</a>
      </div>
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

@media (max-width: 720px) {
  .footer-content {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>