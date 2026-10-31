<script setup>
import { onMounted, onBeforeUnmount, ref } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

// Leaflets Standard-Icon-Pfade brechen unter Vite standardmäßig,
// deshalb hier explizit setzen.
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

// Platzhalter-Standorte: eine Filiale pro deutscher Landeshauptstadt.
const locations = [
  { city: "Stuttgart", state: "Baden-Württemberg", lat: 48.7758, lng: 9.1829, address: "Musterstraße 1, 70173 Stuttgart" },
  { city: "München", state: "Bayern", lat: 48.1351, lng: 11.582, address: "Musterstraße 2, 80331 München" },
  { city: "Berlin", state: "Berlin", lat: 52.52, lng: 13.405, address: "Musterstraße 3, 10117 Berlin" },
  { city: "Potsdam", state: "Brandenburg", lat: 52.3906, lng: 13.0645, address: "Musterstraße 4, 14467 Potsdam" },
  { city: "Bremen", state: "Bremen", lat: 53.0793, lng: 8.8017, address: "Musterstraße 5, 28195 Bremen" },
  { city: "Hamburg", state: "Hamburg", lat: 53.5511, lng: 9.9937, address: "Musterstraße 6, 20095 Hamburg" },
  { city: "Wiesbaden", state: "Hessen", lat: 50.0782, lng: 8.2398, address: "Musterstraße 7, 65183 Wiesbaden" },
  { city: "Schwerin", state: "Mecklenburg-Vorpommern", lat: 53.6355, lng: 11.4012, address: "Musterstraße 8, 19053 Schwerin" },
  { city: "Hannover", state: "Niedersachsen", lat: 52.3759, lng: 9.732, address: "Musterstraße 9, 30159 Hannover" },
  { city: "Düsseldorf", state: "Nordrhein-Westfalen", lat: 51.2277, lng: 6.7735, address: "Musterstraße 10, 40213 Düsseldorf" },
  { city: "Mainz", state: "Rheinland-Pfalz", lat: 49.9929, lng: 8.2473, address: "Musterstraße 11, 55116 Mainz" },
  { city: "Saarbrücken", state: "Saarland", lat: 49.2401, lng: 6.9969, address: "Musterstraße 12, 66111 Saarbrücken" },
  { city: "Dresden", state: "Sachsen", lat: 51.0504, lng: 13.7373, address: "Musterstraße 13, 01067 Dresden" },
  { city: "Magdeburg", state: "Sachsen-Anhalt", lat: 52.1205, lng: 11.6276, address: "Musterstraße 14, 39104 Magdeburg" },
  { city: "Kiel", state: "Schleswig-Holstein", lat: 54.3233, lng: 10.1228, address: "Musterstraße 15, 24103 Kiel" },
  { city: "Erfurt", state: "Thüringen", lat: 50.9848, lng: 11.0299, address: "Musterstraße 16, 99084 Erfurt" },
];

const mapEl = ref(null);
const activeCity = ref(null);
let map;
const markerByCity = {};

onMounted(() => {
  map = L.map(mapEl.value, {
    scrollWheelZoom: false,
  }).setView([51.1657, 10.4515], 6);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap-Mitwirkende",
    maxZoom: 18,
  }).addTo(map);

  locations.forEach((loc) => {
    const marker = L.marker([loc.lat, loc.lng]).addTo(map);
    marker.bindPopup(`<strong>Hasenfutter ${loc.city}</strong><br />${loc.address}`);
    marker.on("click", () => {
      activeCity.value = loc.city;
    });
    markerByCity[loc.city] = marker;
  });
});

onBeforeUnmount(() => {
  if (map) {
    map.remove();
  }
});

function focusLocation(loc) {
  activeCity.value = loc.city;
  const marker = markerByCity[loc.city];
  if (map && marker) {
    map.flyTo([loc.lat, loc.lng], 12, { duration: 0.8 });
    marker.openPopup();
  }
}
</script>

<template>
  <div class="locations-page">
    <section class="locations-hero">
      <p class="eyebrow">Unsere Standorte</p>
      <h1>In jeder Landeshauptstadt zu Hause</h1>
      <p class="lead">
        Platzhalter-Filialen in allen 16 deutschen Landeshauptstädten. Adressen
        und Öffnungszeiten hier später durch echte Daten ersetzen.
      </p>
    </section>

    <section class="locations-content container">
      <div ref="mapEl" class="map" aria-label="Karte mit allen Standorten"></div>

      <ul class="location-list">
        <li
          v-for="loc in locations"
          :key="loc.city"
          :class="{ active: activeCity === loc.city }"
        >
          <button type="button" @click="focusLocation(loc)">
            <span class="location-city">Hasenfutter {{ loc.city }}</span>
            <span class="location-state">{{ loc.state }}</span>
            <span class="location-address">{{ loc.address }}</span>
          </button>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.locations-page {
  min-height: 100vh;
  padding-bottom: 5rem;
}

.locations-hero {
  padding: 5.5rem 1.5rem 3.5rem;
  text-align: center;
  background: linear-gradient(180deg, var(--color-forest-dark), var(--color-forest));
  color: var(--color-white);
}

.locations-hero .eyebrow {
  color: var(--color-honey);
}

.locations-hero h1 {
  margin: 0;
  font-family: var(--font-heading);
  font-size: clamp(2.4rem, 5vw, 3.6rem);
  line-height: 1.1;
}

.locations-hero .lead {
  max-width: 600px;
  margin: 1.25rem auto 0;
  color: hsl(0, 0%, 92%);
  font-size: 1.05rem;
  line-height: 1.7;
}

.locations-content {
  display: grid;
  grid-template-columns: 1.6fr 1fr;
  gap: 2rem;
  margin-top: 3.5rem;
  align-items: start;
}

.map {
  height: 560px;
  border-radius: var(--radius-lg);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.location-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.6rem;
  max-height: 560px;
  overflow-y: auto;
}

.location-list button {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  padding: 0.9rem 1.1rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-white);
  text-align: left;
  transition: border-color var(--transition), background var(--transition), transform var(--transition);
}

.location-list button:hover {
  border-color: var(--color-forest-light);
  transform: translateY(-1px);
}

.location-list li.active button {
  border-color: var(--color-forest);
  background: var(--color-honey-light);
}

.location-city {
  font-weight: 700;
  color: var(--color-forest-dark);
}

.location-state {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--color-honey-dark);
}

.location-address {
  font-size: 0.88rem;
  color: var(--color-ink-soft);
}

@media (max-width: 900px) {
  .locations-content {
    grid-template-columns: 1fr;
  }

  .map {
    height: 420px;
  }

  .location-list {
    max-height: none;
  }
}
</style>