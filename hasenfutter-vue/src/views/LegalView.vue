<script setup>
import { computed } from "vue";

const props = defineProps({
  page: { type: String, required: true },
});

const isImprint = computed(() => props.page === "impressum");
</script>

<template>
  <div class="legal-page">
    <div class="container legal-content">
      <p class="legal-note">
        Hasenfutter ist ein fiktives Restaurant und diese Seite ein
        Portfolio-Projekt. Alle Angaben sind Platzhalter und ersetzen keine
        Rechtsberatung.
      </p>

      <template v-if="isImprint">
        <h1>Impressum</h1>

        <h2>Angaben gemäß § 5 DDG</h2>
        <p>
          Hasenfutter GmbH<br />
          Musterstraße 123<br />
          12345 Musterstadt
        </p>

        <h2>Vertreten durch</h2>
        <p>Geschäftsführerin: Erika Mustermann</p>

        <h2>Kontakt</h2>
        <p>
          Telefon: +49 123 4567890<br />
          E-Mail: hallo@hasenfutter.de
        </p>

        <h2>Registereintrag</h2>
        <p>
          Eingetragen im Handelsregister des Amtsgerichts Musterstadt<br />
          Registernummer: HRB 000000
        </p>

        <h2>Umsatzsteuer-ID</h2>
        <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE000000000</p>

        <h2>Verantwortlich für den Inhalt</h2>
        <p>Erika Mustermann, Anschrift wie oben</p>
      </template>

      <template v-else>
        <h1>Datenschutzerklärung</h1>

        <h2>1. Verantwortlicher</h2>
        <p>
          Verantwortlich für die Datenverarbeitung auf dieser Website ist die
          Hasenfutter GmbH, Musterstraße 123, 12345 Musterstadt,
          E-Mail: hallo@hasenfutter.de.
        </p>

        <h2>2. Aufruf der Website</h2>
        <p>
          Beim Aufruf der Seite verarbeitet der Webserver technisch notwendige
          Daten, zum Beispiel IP-Adresse, Datum und Uhrzeit, aufgerufene Seite
          und Browsertyp. Das ist nötig, um die Seite auszuliefern und sicher
          zu betreiben (Art. 6 Abs. 1 lit. f DSGVO). Die Daten werden nach
          kurzer Zeit gelöscht und nicht mit anderen Daten zusammengeführt.
        </p>
        <p>
          Wir setzen keine Cookies zu Werbe- oder Analysezwecken ein und
          verwenden keine Tracking-Tools. Schriftarten sind lokal eingebunden,
          es findet keine Verbindung zu Schriftarten-Servern Dritter statt.
        </p>

        <h2>3. Tischreservierung</h2>
        <p>
          Wenn du einen Tisch reservierst, speichern wir Name, E-Mail-Adresse,
          Datum, Uhrzeit, Personenanzahl und deine optionale Nachricht. Wir
          verwenden die Angaben ausschließlich, um deine Reservierung zu
          bearbeiten und zu bestätigen (Art. 6 Abs. 1 lit. b DSGVO). Die Daten
          werden spätestens drei Monate nach dem Reservierungstermin gelöscht.
          Bitte schreibe keine sensiblen Angaben, etwa zur Gesundheit, in das
          Nachrichtenfeld. Allergiehinweise gibst du freiwillig an.
        </p>

        <h2>4. Karten von OpenStreetMap</h2>
        <p>
          Auf den Seiten Kontakt und Standorte laden wir Kartenkacheln von
          OpenStreetMap (OpenStreetMap Foundation, Vereinigtes Königreich).
          Dabei erhält der Anbieter technisch bedingt deine IP-Adresse. Die
          Karten werden erst geladen, wenn du die jeweilige Seite aufrufst
          (Art. 6 Abs. 1 lit. f DSGVO). Mehr dazu in der Datenschutzerklärung
          von OpenStreetMap.
        </p>

        <h2>5. Deine Rechte</h2>
        <p>
          Du hast das Recht auf Auskunft, Berichtigung, Löschung,
          Einschränkung der Verarbeitung, Datenübertragbarkeit und
          Widerspruch. Außerdem kannst du dich bei einer
          Datenschutz-Aufsichtsbehörde beschweren. Schreibe uns dafür an
          hallo@hasenfutter.de.
        </p>

        <h2>6. Änderungen</h2>
        <p>
          Wir passen diese Erklärung an, wenn sich die Website oder die
          rechtlichen Vorgaben ändern. Stand: November 2026.
        </p>
      </template>

      <router-link class="legal-back" to="/">Zurück zur Startseite</router-link>
    </div>
  </div>
</template>

<style scoped>
.legal-page {
  padding: 4rem 0 6rem;
}

.legal-content {
  max-width: 760px;
}

.legal-note {
  margin-bottom: 2rem;
  padding: 0.9rem 1.1rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  background: var(--color-honey-light);
  font-size: 0.92rem;
}

h1 {
  margin-bottom: 1.5rem;
  font-family: var(--font-heading);
}

h2 {
  margin: 2rem 0 0.5rem;
  font-family: var(--font-heading);
  font-size: 1.25rem;
}

.legal-back {
  display: inline-block;
  margin-top: 2.5rem;
  color: var(--color-forest);
  font-weight: 700;
}
</style>
