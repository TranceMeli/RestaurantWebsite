<script setup>
import restaurantInterior from "../assets/images/restaurant-interior.jpg";
import kuecheImage from "../assets/images/feature-kueche.jpg";
import ambienteImage from "../assets/images/feature-ambiente.jpg";
import momenteImage from "../assets/images/feature-momente.jpg";

const features = [
  {
    image: kuecheImage,
    title: "Frische Küche",
    text: "Rustikal, vegan und ohne Schnickschnack — bei uns kommt auf den Tisch, was schmeckt, nicht was glänzt.",
  },
  {
    image: ambienteImage,
    title: "Gemütliches Ambiente",
    text: "Warmes Licht, dunkles Holz und der Duft frischer Kräuter — bei uns wird jeder Abend automatisch gemütlich.",
  },
  {
    image: momenteImage,
    title: "Besondere Momente",
    text: "Ob du einfach nur den Tag ausklingen lässt oder deinen Geburtstag feierst — bei uns ist für beides Platz.",
  },
];
</script>

<template>
  <section id="restaurant" class="section section-light">
    <div class="container">
      <div class="section-heading">
        <p class="eyebrow">Unser Restaurant</p>
        <h2>Mit Liebe gemacht</h2>
        <p>
          Platzhaltertext für die Geschichte, Philosophie und besondere
          Atmosphäre des Restaurants.
        </p>
      </div>

      <div class="about-grid">
        <div class="about-image">
          <img :src="restaurantInterior" alt="Gastraum im Hasenfutter mit Backsteinwänden und gedeckten Tischen" />
        </div>

        <div class="about-content">
          <h3>Ein Ort zum Wohlfühlen</h3>
          <p>
            Bei uns gibt's das, worauf man nach einem langen Tag wirklich
            Lust hat: ehrliche Hausmannskost, wie man sie von früher kennt —
            nur komplett pflanzlich. Schnitzel, Sauerbraten, Käsespätzle,
            Currywurst: Wir nehmen die Klassiker, die man liebt, und zeigen,
            dass darauf niemand verzichten muss, um vegan zu essen.
          </p>
          <p>
            Was auf den Teller kommt, richtet sich nach der Saison und kommt
            möglichst aus der Region. Wir arbeiten mit Lieferanten aus der
            Umgebung zusammen und kochen mit dem, was gerade wächst — frisch,
            unaufgeregt und mit Liebe zum Detail.
          </p>
        </div>
      </div>

      <div class="feature-list">
        <div class="feature-card" v-for="feature in features" :key="feature.title">
          <div class="feature-image">
            <img :src="feature.image" :alt="feature.title" />
          </div>
          <h4>{{ feature.title }}</h4>
          <p>{{ feature.text }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about-grid {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: 5rem;
  align-items: center;
}

.about-image {
  min-height: 500px;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
}

.about-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.about-content {
  max-width: 680px;
}

.about-content > p {
  color: var(--color-ink-soft);
}

.feature-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
  margin-top: 4rem;
}

.feature-card {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-cream);
  overflow: hidden;
  padding-bottom: 1.25rem;
}

.feature-image {
  height: 180px;
  overflow: hidden;
}

.feature-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.feature-card h4 {
  margin: 1rem 1.25rem 0.35rem;
  font-size: 1.05rem;
}

.feature-card p {
  margin: 0 1.25rem;
  color: var(--color-ink-soft);
}

@media (max-width: 900px) {
  .about-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  .about-image {
    min-height: 360px;
  }
}

@media (max-width: 720px) {
  .feature-list {
    grid-template-columns: 1fr;
  }
}
</style>