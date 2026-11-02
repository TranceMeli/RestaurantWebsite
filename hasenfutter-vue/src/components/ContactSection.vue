<script setup>
import { onMounted, onBeforeUnmount, ref } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

const cards = [
  { label: "Adresse", lines: ["Musterstraße 123", "12345 Musterstadt"] },
  { label: "Telefon", link: { href: "tel:+491234567890", text: "+49 123 4567890" } },
  { label: "E-Mail", link: { href: "mailto:hallo@hasenfutter.de", text: "hallo@hasenfutter.de" } },
  { label: "Öffnungszeiten", lines: ["Mo bis Sa · 17:00 bis 23:00 Uhr", "Montag · Ruhetag"] },
];

// Platzhalter-Koordinaten (Karlsruhe), bei echter Adresse austauschen.
const restaurantLocation = { lat: 49.0069, lng: 8.4037 };

const mapEl = ref(null);
let map;

onMounted(() => {
  map = L.map(mapEl.value, {
    scrollWheelZoom: false,
  }).setView([restaurantLocation.lat, restaurantLocation.lng], 15);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap-Mitwirkende",
    maxZoom: 18,
  }).addTo(map);

  L.marker([restaurantLocation.lat, restaurantLocation.lng])
    .addTo(map)
    .bindPopup("<strong>Hasenfutter</strong><br />Musterstraße 123, 12345 Musterstadt")
    .openPopup();
});

onBeforeUnmount(() => {
  if (map) {
    map.remove();
  }
});
</script>

<template>
  <section id="kontakt" class="section section-light">
    <div class="container">
      <div class="contact-grid">
        <div class="section-heading">
          <p class="eyebrow">Kontakt</p>
          <h2>Wir freuen uns auf dich.</h2>
          <p>Platzhalter für Kontaktinformationen, Öffnungszeiten und weitere Hinweise.</p>
        </div>

        <div class="contact-cards">
          <article class="contact-card" v-for="card in cards" :key="card.label">
            <span class="contact-label">{{ card.label }}</span>
            <p v-if="card.lines">
              <template v-for="(line, i) in card.lines" :key="line">
                {{ line }}<br v-if="i < card.lines.length - 1" />
              </template>
            </p>
            <p v-else-if="card.link">
              <a :href="card.link.href">{{ card.link.text }}</a>
            </p>
          </article>
        </div>
      </div>

      <div ref="mapEl" class="contact-map" aria-label="Karte mit dem Standort des Restaurants"></div>
    </div>
  </section>
</template>

<style scoped>
.contact-grid {
  display: grid;
  grid-template-columns: 0.8fr 1.2fr;
  gap: 5rem;
  align-items: start;
}

.contact-cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.contact-card {
  padding: 1.4rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-cream);
}

.contact-label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--color-honey-dark);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.contact-card p {
  margin: 0;
}

.contact-card a {
  color: var(--color-forest);
  font-weight: 700;
}

.contact-map {
  min-height: 320px;
  height: 380px;
  margin-top: 3rem;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

@media (max-width: 900px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}

@media (max-width: 720px) {
  .contact-cards {
    grid-template-columns: 1fr;
  }
}
</style>