# Hasenfutter: Freude am Mümmeln

![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Vue Router](https://img.shields.io/badge/Vue_Router-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-A30000?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

Fiktive vegane Restaurant-Website mit Tischreservierung. Portfolio-Projekt.
Klassische Hausmannskost, komplett pflanzlich, mit saisonalen Zutaten und
regionalen Lieferanten.

---

## Screenshot

<img width="1911" height="1067" alt="image" src="https://github.com/user-attachments/assets/6de6233b-ea86-4c7e-8898-0ac31d1deb3a" />


## Features

- **Startseite** mit Hero-Bereich, Abschnitt "Über das Restaurant" (inklusive
  drei Bildkarten zu Küche, Ambiente und besonderen Momenten),
  Reservierungsformular und Kontaktbereich
- **Speisekarte** als eigene Seite mit Kategorie-Filter (Schnitzel & Steak,
  Deutsche Klassiker, Pasta, Vegetarische Klassiker, Fisch & Meer)
- **Standorte-Seite** mit interaktiver Karte (Leaflet und OpenStreetMap) und
  Filialen in allen 16 deutschen Landeshauptstädten
- **Kontaktbereich** mit Adresse, Telefon, E-Mail, Öffnungszeiten und
  eingebetteter Karte
- **Reservierungsformular** mit Client-seitiger Validierung (Pflichtfelder,
  E-Mail-Format, kein Datum in der Vergangenheit) und Anbindung an ein
  Django-Backend
- **Eigenes Logo** mit integriertem Schriftzug, zusätzlich als Favicon
- **Dekorative Elemente** im Möhren-Stil: zwei Möhren als Trenner unter dem
  Header sowie ein durchgehender Randstreifen links und rechts
- **Eigenes Farbsystem** auf HSL-Basis, zentral in CSS-Custom-Properties
  gepflegt
- **Fluide Schriftgröße**, die mit der Bildschirmbreite mitwächst
  (16px bis 19px), damit der Text auch auf großen Monitoren gut lesbar bleibt
- **Responsive Navigation**: Linknamen brechen nie über zwei Zeilen um, bei
  wenig Platz rutschen ganze Links in die nächste Zeile, auf dem Handy gibt
  es ein Hamburger-Menü

## Tech-Stack

**Frontend**
- Vue 3 (Composition API, `<script setup>`)
- Vite als Build-Tool
- Vue Router für Speisekarte und Standorte als eigene Routen
- Leaflet für die interaktiven Karten
- Google Fonts: Lora für Überschriften

**Backend**
- Django und Django REST Framework für die Reservierungs-API
- SQLite als Datenbank
- django-cors-headers für die Verbindung zum Vite-Dev-Server

## Projektstruktur

```
hasenfutter-vue/
  index.html
  public/
    logo.svg                      Logo als Favicon
  src/
    main.js                       Einstiegspunkt, registriert den Router
    App.vue                       Header, Trenner, router-view, Footer, Randstreifen
    router/
      index.js                    Routen: / , /speisekarte , /standorte
    style/
      variables.css               Farbpalette und Design-Tokens (HSL)
      base.css                    Reset, fluide Schriftgröße, Typografie, Buttons
    assets/
      logo.svg                    Logo mit Schriftzug
      carrot-divider.svg          Möhre für den Header-Trenner
      images/
        hero-restaurant.jpg       Foto im Hero-Bereich
        restaurant-interior.jpg   Foto bei "Über das Restaurant"
        feature-kueche.jpg        Bildkarte "Frische Küche"
        feature-ambiente.jpg      Bildkarte "Gemütliches Ambiente"
        feature-momente.jpg       Bildkarte "Besondere Momente"
    components/
      TheHeader.vue               Logo, Navigation, mobiles Menü
      HeaderDivider.vue           Trenner mit zwei Möhren unter dem Header
      TheFooter.vue
      HeroSection.vue             Willkommen
      AboutSection.vue            Über das Restaurant
      BookingSection.vue          Buchen, Formular mit Validierung
      ContactSection.vue          Kontakt mit Karte
    views/
      HomeView.vue                Bündelt Hero, About, Booking und Contact
      MenuView.vue                Speisekarte mit Kategorie-Filter
      LocationsView.vue           Standorte-Karte und Filialliste

hasenfutter-backend/              Separates Django-Projekt
  config/
    settings.py
    urls.py
  reservations/
    models.py
    serializers.py
    views.py
    urls.py
    admin.py
```

## Setup

### Frontend

```bash
cd hasenfutter-vue
npm install
npm run dev
```

Läuft standardmäßig unter `http://localhost:5173`.

### Backend

```bash
cd hasenfutter-backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install django djangorestframework django-cors-headers

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Läuft standardmäßig unter `http://localhost:8000`. Das Admin-Interface ist
unter `http://localhost:8000/admin/` erreichbar.

Für die Reservierungsfunktion müssen Frontend und Backend gleichzeitig laufen.

## Farbpalette

Alle Farben liegen als HSL-Custom-Properties in `src/style/variables.css`:

| Rolle | Variable | Wert |
|---|---|---|
| Primär (Waldgrün) | `--color-forest` | `hsl(152, 62%, 25%)` |
| Primär dunkel | `--color-forest-dark` | `hsl(152, 65%, 18%)` |
| Primär hell | `--color-forest-light` | `hsl(152, 42%, 42%)` |
| Akzent (Honiggold) | `--color-honey` | `hsl(35, 92%, 58%)` |
| Akzent dunkel | `--color-honey-dark` | `hsl(35, 80%, 47%)` |
| Akzent hell | `--color-honey-light` | `hsl(37, 100%, 91%)` |
| Hintergrund (Creme) | `--color-cream` | `hsl(40, 33%, 96%)` |
| Fläche (Weiß) | `--color-white` | `hsl(0, 0%, 100%)` |
| Fläche warm (Leinen) | `--color-linen` | `hsl(39, 38%, 92%)` |
| Text (Tinte) | `--color-ink` | `hsl(152, 18%, 18%)` |
| Text sanft | `--color-ink-soft` | `hsl(152, 10%, 42%)` |
| Linien und Rahmen | `--color-border` | `hsl(38, 20%, 84%)` |

## Typografie

- Überschriften: Lora (Google Fonts), Fallback Georgia
- Fließtext: Gill Sans, Fallback Calibri und Trebuchet MS
- Die Root-Schriftgröße skaliert fluide zwischen 16px und 19px
