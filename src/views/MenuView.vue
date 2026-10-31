<script setup>
import { ref, computed } from "vue";

const activeCategory = ref("Alle");

const categories = [
  "Alle",
  "Schnitzel & Steak",
  "Deutsche Klassiker",
  "Pasta",
  "Vegetarische Klassiker",
  "Fisch & Meer",
];

const dishes = [
  {
    name: "Wiener Schnitzel",
    description: "Knusprig paniertes veganes Schnitzel mit Kartoffelsalat und Preiselbeeren.",
    price: "18,90 €",
    category: "Schnitzel & Steak",
    tag: "Klassiker",
  },
  {
    name: "Cordon Bleu",
    description: "Gefülltes veganes Schnitzel mit cremiger Füllung, dazu goldbraune Pommes.",
    price: "19,90 €",
    category: "Schnitzel & Steak",
    tag: "Beliebt",
  },
  {
    name: "Jägerschnitzel",
    description: "Veganes Schnitzel mit cremiger Champignonrahmsauce und hausgemachten Spätzle.",
    price: "18,90 €",
    category: "Schnitzel & Steak",
    tag: "Klassiker",
  },
  {
    name: "Rahmschnitzel",
    description: "Zartes veganes Schnitzel mit feiner Rahmsauce und knusprigen Kroketten.",
    price: "18,50 €",
    category: "Schnitzel & Steak",
  },
  {
    name: "Steak mit Kräuterbutter",
    description: "Veganes Steak mit aromatischer Kräuterbutter und knusprigen Bratkartoffeln.",
    price: "23,90 €",
    category: "Schnitzel & Steak",
    tag: "Beliebt",
  },
  {
    name: "Zwiebelrostbraten",
    description: "Vegane Variante des Klassikers mit Röstzwiebeln, Spätzle und Bratensauce.",
    price: "22,90 €",
    category: "Schnitzel & Steak",
    tag: "Klassiker",
  },
  {
    name: "Sauerbraten",
    description: "Herzhafter veganer Sauerbraten mit Kartoffelklößen und Apfel-Rotkohl.",
    price: "21,90 €",
    category: "Deutsche Klassiker",
    tag: "Hausklassiker",
  },
  {
    name: "Rouladen",
    description: "Herzhafte vegane Rouladen mit Rotkohl, Kartoffelklößen und kräftiger Sauce.",
    price: "21,50 €",
    category: "Deutsche Klassiker",
  },
  {
    name: "Gulasch",
    description: "Kräftiges veganes Gulasch mit hausgemachten Spätzle und Gurkensalat.",
    price: "17,90 €",
    category: "Deutsche Klassiker",
  },
  {
    name: "Hackbraten",
    description: "Saftiger veganer Hackbraten mit Kartoffelpüree und dunkler Bratensauce.",
    price: "17,50 €",
    category: "Deutsche Klassiker",
  },
  {
    name: "Currywurst",
    description: "Vegane Bratwurst mit hausgemachter Currysauce und goldbraunen Pommes.",
    price: "14,90 €",
    category: "Deutsche Klassiker",
    tag: "Beliebt",
  },
  {
    name: "Bratwurst",
    description: "Vegane Bratwurst mit Sauerkraut, Kartoffelpüree und kräftiger Bratensauce.",
    price: "15,50 €",
    category: "Deutsche Klassiker",
  },
  {
    name: "Königsberger Klopse",
    description: "Vegane Klopse in cremiger Kapernsauce, serviert mit Salzkartoffeln.",
    price: "17,90 €",
    category: "Deutsche Klassiker",
  },
  {
    name: "Spaghetti Bolognese",
    description: "Klassische Spaghetti mit herzhafter veganer Bolognese und Parmesan-Alternative.",
    price: "15,90 €",
    category: "Pasta",
    tag: "Klassiker",
  },
  {
    name: "Spaghetti Carbonara",
    description: "Cremige vegane Carbonara mit würzigen Räucheraromen und Parmesan-Alternative.",
    price: "16,50 €",
    category: "Pasta",
  },
  {
    name: "Lasagne Bolognese",
    description: "Hausgemachte vegane Lasagne mit Bolognese, Béchamel und Käse-Alternative.",
    price: "17,90 €",
    category: "Pasta",
    tag: "Beliebt",
  },
  {
    name: "Käsespätzle",
    description: "Hausgemachte vegane Spätzle mit cremiger Käse-Alternative und Röstzwiebeln.",
    price: "16,90 €",
    category: "Vegetarische Klassiker",
    tag: "Beliebt",
  },
  {
    name: "Maultaschen",
    description: "Vegane Maultaschen mit Zwiebelschmelze und frischem Kartoffelsalat.",
    price: "16,50 €",
    category: "Vegetarische Klassiker",
    tag: "Klassiker",
  },
  {
    name: "Backfischfilet",
    description: "Knusprig paniertes veganes Filet mit Kartoffelsalat und hausgemachter Remoulade.",
    price: "17,90 €",
    category: "Fisch & Meer",
  },
  {
    name: "Fish & Chips",
    description: "Veganes Backfischfilet mit knusprigen Pommes und cremiger Remoulade.",
    price: "17,50 €",
    category: "Fisch & Meer",
    tag: "Beliebt",
  },
];

const filteredDishes = computed(() => {
  if (activeCategory.value === "Alle") {
    return dishes;
  }

  return dishes.filter((dish) => dish.category === activeCategory.value);
});
</script>

<template>
  <div class="menu-page">
    <section class="menu-hero">
      <span class="eyebrow">Unsere Küche</span>
      <h1>Speisekarte</h1>
      <p>Klassische Lieblingsgerichte. Neu interpretiert. 100&nbsp;% pflanzlich.</p>
    </section>

    <nav class="category-nav" aria-label="Speisekategorien">
      <button
        v-for="category in categories"
        :key="category"
        :class="{ active: activeCategory === category }"
        @click="activeCategory = category"
      >
        {{ category }}
      </button>
    </nav>

    <section class="menu-content">
      <div class="menu-grid">
        <article v-for="dish in filteredDishes" :key="dish.name" class="dish-card">
          <div class="dish-header">
            <div>
              <span v-if="dish.tag" class="dish-tag">{{ dish.tag }}</span>
              <h2>{{ dish.name }}</h2>
            </div>
            <span class="price">{{ dish.price }}</span>
          </div>

          <p class="description">{{ dish.description }}</p>

          <div class="dish-footer">
            <span class="vegan">
              <span class="vegan-dot"></span>
              100&nbsp;% vegan
            </span>
          </div>
        </article>
      </div>
    </section>

    <section class="menu-note">
      <span class="note-icon">✦</span>
      <div>
        <strong>Alles pflanzlich.</strong>
        <p>Alle Gerichte auf unserer Speisekarte werden vollständig vegan und mit frischen Zutaten zubereitet.</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.menu-page {
  min-height: 100vh;
  padding-bottom: 5rem;
}

/* Hero */

.menu-hero {
  padding: 5.5rem 1.5rem 4rem;
  text-align: center;
  background: linear-gradient(180deg, var(--color-forest-dark), var(--color-forest));
  color: var(--color-white);
}

.menu-hero .eyebrow {
  color: var(--color-honey);
}

.menu-hero h1 {
  margin: 0;
  font-family: var(--font-heading);
  font-size: clamp(3rem, 7vw, 5rem);
  line-height: 1;
}

.menu-hero p {
  max-width: 620px;
  margin: 1.5rem auto 0;
  color: hsl(0, 0%, 92%);
  font-size: 1.08rem;
  line-height: 1.7;
}

/* Kategorie-Navigation */

.category-nav {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  padding: 1.6rem 1.25rem;
  background: var(--color-white);
  border-bottom: 1px solid var(--color-border);
}

.category-nav button {
  padding: 0.6rem 1.1rem;
  border: 1px solid var(--color-border);
  border-radius: 999px;
  background: transparent;
  color: var(--color-ink-soft);
  font-size: 0.9rem;
  font-weight: 600;
  transition:
    background var(--transition),
    color var(--transition),
    border-color var(--transition),
    transform var(--transition);
}

.category-nav button:hover {
  border-color: var(--color-forest-light);
  color: var(--color-forest);
  transform: translateY(-1px);
}

.category-nav button.active {
  border-color: var(--color-forest);
  background: var(--color-forest);
  color: var(--color-white);
}

/* Gerichte */

.menu-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 4rem 1.5rem;
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
}

.dish-card {
  padding: 1.7rem 1.8rem 1.4rem;
  background: var(--color-white);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  transition: transform var(--transition), box-shadow var(--transition);
}

.dish-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}

.dish-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1.25rem;
}

.dish-header h2 {
  margin: 0.3rem 0 0;
  font-family: var(--font-heading);
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--color-forest-dark);
}

.dish-tag {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  background: var(--color-honey-light);
  color: var(--color-honey-dark);
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.price {
  flex-shrink: 0;
  color: var(--color-forest);
  font-size: 1.05rem;
  font-weight: 800;
}

.description {
  margin: 0.9rem 0 1.4rem;
  color: var(--color-ink-soft);
  font-size: 0.94rem;
  line-height: 1.65;
}

.dish-footer {
  padding-top: 0.9rem;
  border-top: 1px solid var(--color-border);
}

.vegan {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--color-forest-light);
  font-size: 0.75rem;
  font-weight: 700;
}

.vegan-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-forest-light);
}

/* Hinweis */

.menu-note {
  display: flex;
  align-items: flex-start;
  gap: 1.1rem;
  max-width: 760px;
  margin: 0 auto;
  padding: 1.6rem 1.75rem;
  background: var(--color-linen);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
}

.note-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: var(--color-honey);
  color: var(--color-forest-dark);
}

.menu-note strong {
  color: var(--color-forest-dark);
}

.menu-note p {
  margin: 0.3rem 0 0;
  color: var(--color-ink-soft);
  font-size: 0.9rem;
  line-height: 1.6;
}

/* Responsive */

@media (max-width: 760px) {
  .menu-hero {
    padding: 4.4rem 1.25rem 3rem;
  }

  .menu-grid {
    grid-template-columns: 1fr;
  }

  .menu-content {
    padding: 2.8rem 1rem;
  }

  .dish-card {
    padding: 1.4rem;
  }

  .dish-header h2 {
    font-size: 1.2rem;
  }

  .category-nav {
    justify-content: flex-start;
    flex-wrap: nowrap;
    overflow-x: auto;
    padding: 1.1rem 1rem;
  }

  .category-nav button {
    flex-shrink: 0;
  }

  .menu-note {
    margin: 0 1rem;
  }
}
</style>