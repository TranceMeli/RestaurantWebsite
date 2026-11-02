<script setup>
import { reactive, ref } from "vue";

const timeOptions = ["17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30"];
const guestOptions = ["1 Person", "2 Personen", "3 Personen", "4 Personen", "5 Personen", "6+ Personen"];

const form = reactive({
  name: "",
  email: "",
  date: "",
  time: "",
  guests: "",
  message: "",
});

const errors = reactive({
  name: "",
  email: "",
  date: "",
  time: "",
  guests: "",
});

const submitted = ref(false);
const isSubmitting = ref(false);
const errorMessage = ref("");

const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000";

// Heutiges Datum in lokaler Zeit als YYYY-MM-DD (toISOString wäre UTC und
// abends schon der nächste Tag), fürs <input min="..."> und die Validierung.
function localToday() {
  const now = new Date();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  return `${now.getFullYear()}-${month}-${day}`;
}

const today = ref(localToday());

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function validate() {
  errors.name = form.name.trim() ? "" : "Bitte gib deinen Namen an.";

  if (!form.email.trim()) {
    errors.email = "Bitte gib deine E-Mail-Adresse an.";
  } else if (!emailPattern.test(form.email.trim())) {
    errors.email = "Das sieht nicht nach einer gültigen E-Mail-Adresse aus.";
  } else {
    errors.email = "";
  }

  if (!form.date) {
    errors.date = "Bitte wähle ein Datum.";
  } else if (form.date < localToday()) {
    errors.date = "Das Datum darf nicht in der Vergangenheit liegen.";
  } else {
    errors.date = "";
  }

  errors.time = form.time ? "" : "Bitte wähle eine Uhrzeit.";
  errors.guests = form.guests ? "" : "Bitte wähle die Personenanzahl.";

  return Object.values(errors).every((message) => message === "");
}

async function handleSubmit() {
  errorMessage.value = "";

  if (!validate()) {
    return;
  }

  isSubmitting.value = true;

  try {
    const response = await fetch(`${API_URL}/api/reservierungen/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });

    if (response.status === 400) {
      const data = await response.json();
      let hasFieldError = false;
      for (const key of Object.keys(errors)) {
        if (data[key]) {
          errors[key] = [].concat(data[key]).join(" ");
          hasFieldError = true;
        }
      }
      if (hasFieldError) {
        return;
      }
    }

    if (!response.ok) {
      throw new Error("Die Reservierung konnte nicht gespeichert werden.");
    }

    submitted.value = true;
  } catch {
    errorMessage.value = "Da ist etwas schiefgelaufen. Bitte versuch es noch einmal.";
  } finally {
    isSubmitting.value = false;
  }
}

function resetForm() {
  submitted.value = false;
  form.name = "";
  form.email = "";
  form.date = "";
  form.time = "";
  form.guests = "";
  form.message = "";
  errors.name = "";
  errors.email = "";
  errors.date = "";
  errors.time = "";
  errors.guests = "";
}
</script>

<template>
  <section id="buchen" class="section booking-section">
    <div class="container booking-wrapper">
      <div class="section-heading section-heading-light">
        <p class="eyebrow">Reservierung</p>
        <h2>Deinen Tisch buchen</h2>
        <p>
          Fülle das Formular aus, wir bestätigen deine Reservierung im Anschluss
          per E-Mail.
        </p>
      </div>

      <form class="booking-form" @submit.prevent="handleSubmit" v-if="!submitted" novalidate>
        <p v-if="errorMessage" class="form-error form-error-general">{{ errorMessage }}</p>

        <div class="form-grid">
          <div class="form-group">
            <label for="name">Name</label>
            <input
              type="text"
              id="name"
              v-model="form.name"
              placeholder="Max Mustermann"
              :aria-invalid="!!errors.name"
            />
            <span v-if="errors.name" class="form-error">{{ errors.name }}</span>
          </div>

          <div class="form-group">
            <label for="email">E-Mail</label>
            <input
              type="email"
              id="email"
              v-model="form.email"
              placeholder="max@beispiel.de"
              :aria-invalid="!!errors.email"
            />
            <span v-if="errors.email" class="form-error">{{ errors.email }}</span>
          </div>

          <div class="form-group">
            <label for="date">Datum</label>
            <input
              type="date"
              id="date"
              v-model="form.date"
              :min="today"
              :aria-invalid="!!errors.date"
            />
            <span v-if="errors.date" class="form-error">{{ errors.date }}</span>
          </div>

          <div class="form-group">
            <label for="time">Uhrzeit</label>
            <select id="time" v-model="form.time" :aria-invalid="!!errors.time">
              <option value="" disabled>Bitte wählen</option>
              <option v-for="t in timeOptions" :key="t" :value="t">{{ t }}</option>
            </select>
            <span v-if="errors.time" class="form-error">{{ errors.time }}</span>
          </div>

          <div class="form-group">
            <label for="guests">Personen</label>
            <select id="guests" v-model="form.guests" :aria-invalid="!!errors.guests">
              <option value="" disabled>Bitte wählen</option>
              <option v-for="g in guestOptions" :key="g" :value="g">{{ g }}</option>
            </select>
            <span v-if="errors.guests" class="form-error">{{ errors.guests }}</span>
          </div>

          <div class="form-group form-group-full">
            <label for="message">Besondere Wünsche</label>
            <textarea
              id="message"
              v-model="form.message"
              rows="4"
              placeholder="Zum Beispiel Allergien, besondere Wünsche oder Hinweise ..."
            ></textarea>
          </div>
        </div>

        <button class="button button-accent" type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? "Wird gesendet …" : "Reservierung anfragen" }}
        </button>
      </form>

      <div class="booking-confirmation" v-else>
        <h3>Danke, {{ form.name }}!</h3>
        <p>
          Deine Anfrage für {{ form.guests }} am {{ form.date }} um {{ form.time }} Uhr
          wurde erfasst. Wir bestätigen den Tisch in Kürze per E-Mail.
        </p>
        <button class="button button-secondary" type="button" @click="resetForm">
          Neue Reservierung
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.booking-section {
  background: linear-gradient(135deg, var(--color-forest-dark), var(--color-forest));
}

.booking-wrapper {
  max-width: 960px;
}

.booking-form,
.booking-confirmation {
  padding: clamp(1.5rem, 4vw, 3rem);
  border: 1px solid hsl(0 0% 100% / 0.12);
  border-radius: var(--radius-lg);
  background: hsl(0 0% 100% / 0.08);
  box-shadow: var(--shadow-md);
  backdrop-filter: blur(8px);
}

.booking-confirmation {
  color: white;
}

.booking-confirmation h3 {
  color: white;
}

.booking-confirmation p {
  color: hsl(0 0% 100% / 0.85);
  margin-bottom: 1.5rem;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
}

.form-group-full {
  grid-column: 1 / -1;
}

.form-group label {
  color: hsl(0 0% 100% / 0.92);
  font-size: 0.9rem;
  font-weight: 700;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  border: 1px solid hsl(0 0% 100% / 0.18);
  border-radius: var(--radius-sm);
  outline: none;
  padding: 0.9rem 1rem;
  background: hsl(0 0% 100% / 0.96);
  color: var(--color-ink);
  transition: border-color var(--transition), box-shadow var(--transition);
}

.form-group textarea {
  resize: vertical;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  border-color: var(--color-honey);
  box-shadow: 0 0 0 3px hsl(35 92% 58% / 0.2);
}

.form-group input[aria-invalid="true"],
.form-group select[aria-invalid="true"] {
  border-color: hsl(0, 75%, 65%);
}

.form-error {
  color: hsl(0, 85%, 80%);
  font-size: 0.82rem;
  font-weight: 600;
}

.form-error-general {
  margin: 0 0 1.25rem;
  padding: 0.75rem 1rem;
  border: 1px solid hsl(0, 75%, 65% / 0.5);
  border-radius: var(--radius-sm);
  background: hsl(0, 75%, 65% / 0.12);
}

@media (max-width: 720px) {
  .form-grid {
    grid-template-columns: 1fr;
  }

  .form-group-full {
    grid-column: auto;
  }
}
</style>