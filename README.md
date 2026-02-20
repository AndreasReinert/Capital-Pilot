# ✈️ Capital Pilot — Strategic Withdrawal Simulation (v5.1)

<p align="center">
  <img src="https://img.shields.io/badge/version-5.1-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Version 5.1">
  <img src="https://img.shields.io/badge/languages-21-a78bfa?style=for-the-badge&labelColor=0f172a" alt="21 Languages">
  <img src="https://img.shields.io/badge/currencies-20-fbbf24?style=for-the-badge&labelColor=0f172a" alt="20 Currencies">
  <img src="https://img.shields.io/badge/offline-100%25-34d399?style=for-the-badge&labelColor=0f172a" alt="Offline Ready">
  <img src="https://img.shields.io/badge/mobile-optimized-fbbf24?style=for-the-badge&labelColor=0f172a" alt="Mobile Ready">
  <img src="https://img.shields.io/badge/license-MIT-fb7185?style=for-the-badge&labelColor=0f172a" alt="MIT License">
</p>

<p align="center">
  <b>Can you retire early without running out of money?</b><br>
  <i>Kannst du früh in Rente gehen, ohne dass das Geld ausgeht?</i>
</p>

---

## EN — Overview

**Capital Pilot** is a single-file, offline-friendly retirement withdrawal simulator. It answers one question:  
**How much can I spend per month — and will my strategy survive decades of market chaos?**

It models a **three-bucket setup** (ETF depot + cash buffer + war chest), **taxes**, **housing** (rent vs. ownership), and a **crisis engine** that lets you navigate real history and generate random crisis-driven futures.

### What’s new in v5.1

- **Crisis Engine navigation**
  - **← 5Y / 5Y →**: move through real history in 5-year steps
  - **↻ Random Forecast**: generates a new future every click, starting from **19 Feb 2026**
- **Historical crises updated**
  - Added **Trump Tariff Crisis (early 2025)** as the newest historical event
- **Random crisis generator improved**
  - Random crises are distributed across the **full withdrawal duration** (e.g., 30 years)
  - Rule: **at least 1 major crisis per decade** + smaller crises in-between
- **Currency-aware capital slider**
  - Starting capital min/max/step **adapt to the selected currency**
  - Example: **CHF** uses **100k–10M**; high-inflation / low-value currencies scale accordingly and the step size is auto-rounded
- **CHF-only Eigenmietwert logic**
  - The **Eigenmietwert (imputed rent)** control is **shown only for CHF**
  - In tax calculations it is **included only for CHF** and **ignored for all other currencies**
- **Updated defaults**
  - Starting capital: **1'200'000**
  - Inflation: **1.5%**
  - Expected return: **6.0%**
  - Pension: **1'800 / month**

---

## EN — Key Features

### Three-bucket withdrawal strategy

| Bucket | Purpose | Behavior |
|---|---|---|
| 🔵 **ETF Depot** | Growth engine | Compounds with expected return. Withdrawals come from here in normal markets. |
| 🟢 **Cash Buffer** | Crisis shield | Covers expenses when markets crash (withdrawals from ETFs can stop). |
| 🟡 **War Chest** | Opportunity fund | Reserved for dip-buying at drawdown thresholds; **never used for living expenses**. |

### Crisis Engine (History + Random Forecast)

**History mode (← 5Y / 5Y →)**  
- Scroll through real historical windows and see crisis markers and shading.

**Random forecast mode (↻)**  
- Anchors start at **19 Feb 2026**
- Picks from realistic crisis types:
  - **Banking crisis**
  - **Oil price shock**
  - **Pandemic**
  - **Hyperinflation**
- Places events across the full horizon, with:
  - **≥ 1 major crisis per 10 years**
  - additional smaller crises randomly in-between
- Each click generates a **new, different future**

### Tax & Housing

- **Taxes**
  - Income tax (%)
  - Capital gains tax (%)
  - Wealth tax (% p.a.)
  - **Eigenmietwert** is applied **only when currency = CHF**
- **Housing toggle**
  - 🏠 Rent: rent + utilities + living costs
  - 🏡 Own: property value, mortgage, mortgage interest, maintenance, appreciation  
    (Eigenmietwert shown only for CHF)
- **Net budget breakdown**
  - Gross → Taxes → Housing → Net available spending

### Currency & Language

- **20 currencies** (e.g., CHF, EUR, USD, GBP, PLN, SEK, NOK, RUB, TRY, INR, CNY, JPY, CAD, AUD, BRL …)
- **21 languages** (EN, DE, FR, ES, IT, PT, NL, PL, RU, TR, SV, DA, NO, FI, CS, HU, RO, EL, UK, HI, ZH)
- **Decoupled pickers**: choose any language with any currency
- **Tooltips**: all parameter tooltips + navigation tooltips translated across supported languages

---

## EN — Historical Crisis Database (1973–2025)

Includes (selection):
- 1973 Oil Crisis
- Volcker Recession
- Black Monday (1987)
- Gulf War / Early 90s recession
- Asian / LTCM Crisis (1997–1998)
- Dotcom Crash (2000)
- Global Financial Crisis (2008)
- EU Debt Crisis (2011)
- China / Oil Shock (2015)
- COVID-19 Crash (2020)
- 2022 Bear Market (2022)
- **Trump Tariff Crisis (2025)**

---

## EN — Getting Started

### Option 1: Open the file
Open `index.html` in any modern browser.

### Option 2: GitHub Pages
1. Commit `index.html` to a repository
2. Enable **GitHub Pages** → deploy from `main` / root

### Option 3: Local server
```bash
python3 -m http.server 8080
# http://localhost:8080/
```

---

## EN — Defaults & Ranges (current calibration)

| Parameter | Default | Range |
|---|---:|---:|
| Starting Capital | 1'200'000 | **Currency-dependent** (e.g., CHF 100k–10M) |
| Duration | 30 years | 10 – 50 |
| Target Legacy | 0 | 0 – 5'000'000 |
| Inflation | 1.5% | 0 – 10% |
| Expected Return | 6.0% | 1 – 20% |
| Pension (monthly) | 1'800 | 0 – 10'000 |
| War Chest | 10% | 0 – 40% |
| Cash Buffer | 2 years | 0 – 6 |
| Max SWR | 4.0% | 2 – 7% |
| Income Tax | 20% | 0 – 50% |
| Capital Gains Tax | 0% | 0 – 35% |
| Wealth Tax | 0.20% p.a. | 0 – 2% |

---

## EN — Architecture (single-file)

```
index.html
│
├── HTML (UI + sliders + chart canvas)
├── CSS  (responsive glass UI)
└── JS
    ├── i18n (21 languages)
    ├── currency engine (20 currencies, scaled ranges)
    ├── housing + tax engine (CHF-only Eigenmietwert)
    ├── crisis DB (1973–2025)
    ├── crisis engine (history navigation + random forecast)
    ├── simulation engine (buffer + war chest + stop rules)
    └── Chart.js rendering (shading + crisis tags)
```

---

## EN — License
MIT

---

# DE — Überblick

**Capital Pilot** ist ein Entnahme‑Simulator in **einer einzigen HTML‑Datei** (offline‑freundlich). Er beantwortet die Kernfrage:  
**Wie viel kann ich pro Monat ausgeben – und überlebt meine Strategie Jahrzehnte voller Marktkrisen?**

Modelliert werden eine **Drei‑Topf‑Strategie** (ETF‑Depot + Cash‑Puffer + Kriegskasse), **Steuern**, **Wohnen** (Miete vs. Eigentum) sowie eine **Krisen‑Engine** (reale Historie + Zufalls‑Zukunft).

### Neu in v5.1

- **Krisen‑Engine Navigation**
  - **← 5Y / 5Y →**: Navigation durch die reale Historie in 5‑Jahres‑Schritten
  - **↻ Zufallsprognose**: erzeugt bei jedem Klick eine neue Zukunft, Start ab **19.02.2026**
- **Historische Krisen aktualisiert**
  - Neu: **Trump‑Zoll‑Krise (Anfang 2025)** als aktuellstes historisches Ereignis
- **Zufalls‑Krisen verbessert**
  - Verteilung über die **gesamte Entnahmedauer** (z. B. 30 Jahre)
  - Regel: **mindestens 1 große Krise pro Dekade** + kleinere Krisen zufällig dazwischen
- **Währungsabhängiger Startkapital‑Slider**
  - Min/Max/Step passen sich **automatisch** an die gewählte Währung an
  - Beispiel: **CHF** nutzt **100k–10M**; andere Währungen skalieren entsprechend, Step wird sinnvoll gerundet
- **Eigenmietwert nur in CHF**
  - Eigenmietwert‑Slider wird **nur bei CHF** angezeigt
  - Steuerberechnung berücksichtigt Eigenmietwert **nur bei CHF** und ignoriert ihn sonst
- **Neue Default‑Werte**
  - Startkapital: **1'200'000**
  - Inflation: **1.5%**
  - Erwartete Rendite: **6.0%**
  - Pension: **1'800 / Monat**

---

## DE — Hauptfunktionen

### Drei‑Topf‑Strategie

| Topf | Zweck | Verhalten |
|---|---|---|
| 🔵 **ETF‑Depot** | Wachstums‑Motor | Verzinst mit erwarteter Rendite. Entnahmen in normalen Märkten. |
| 🟢 **Cash‑Puffer** | Krisen‑Schutz | Deckt Ausgaben bei Crashs (ETF‑Entnahmen können stoppen). |
| 🟡 **Kriegskasse** | Chancen‑Topf | Für Dip‑Käufe bei Drawdowns; **nie für Lebenshaltung**. |

### Krisen‑Engine (Historie + Zufall)

**Historie (← 5Y / 5Y →)**  
- Reale Zeitfenster durchblättern, Krisen‑Marker & Schattierung sehen.

**Zufallsprognose (↻)**  
- Start ab **19.02.2026**
- Krisen‑Pool:
  - **Bankenkrise**
  - **Ölpreisschock**
  - **Pandemie**
  - **Hyperinflation**
- Platzierung über den kompletten Horizont:
  - **≥ 1 große Krise pro 10 Jahre**
  - zusätzliche kleinere Krisen zufällig dazwischen
- Jeder Klick erzeugt eine **andere Zukunft**

### Steuern & Wohnen

- **Steuern**
  - Einkommenssteuer (%)
  - Kapitalertragssteuer (%)
  - Vermögenssteuer (% p.a.)
  - **Eigenmietwert nur bei CHF**
- **Wohnen**
  - 🏠 Miete: Miete + NK + Lebenshaltung
  - 🏡 Eigentum: Immobilienwert, Hypothek, Hypozins, Unterhalt, Wertentwicklung  
    (Eigenmietwert‑Anzeige nur CHF)
- **Budget‑Aufschlüsselung**
  - Brutto → Steuern → Wohnen → Netto‑Budget

### Währung & Sprache

- **20 Währungen** (u. a. CHF, EUR, USD, GBP, PLN, SEK, NOK, RUB, TRY, INR, CNY, JPY, CAD, AUD, BRL …)
- **21 Sprachen** (EN, DE, FR, ES, IT, PT, NL, PL, RU, TR, SV, DA, NO, FI, CS, HU, RO, EL, UK, HI, ZH)
- **Entkoppelt**: Sprache und Währung frei kombinierbar
- **Tooltips**: Parameter‑ und Navigations‑Tooltips sind übersetzt

---

## DE — Krisen‑Datenbank (1973–2025)

Enthält u. a.:
- Ölkrise 1973
- Volcker‑Rezession
- Black Monday (1987)
- Golfkrieg / frühe 90er
- Asien/LTCM (1997–1998)
- Dotcom (2000)
- Finanzkrise (2008)
- Eurokrise (2011)
- China/Öl‑Schock (2015)
- COVID‑Crash (2020)
- Bärenmarkt 2022
- **Trump‑Zoll‑Krise (2025)**

---

## DE — Schnellstart

### Option 1: Datei öffnen
`index.html` lokal im Browser öffnen.

### Option 2: GitHub Pages
1. `index.html` committen
2. GitHub Pages aktivieren → Deploy aus `main` / root

### Option 3: Lokaler Server
```bash
python3 -m http.server 8080
# http://localhost:8080/
```

---

## DE — Defaults & Ranges (aktuelle Kalibrierung)

| Parameter | Default | Range |
|---|---:|---:|
| Startkapital | 1'200'000 | **währungsabhängig** (z. B. CHF 100k–10M) |
| Dauer | 30 Jahre | 10 – 50 |
| Ziel‑Erbe | 0 | 0 – 5'000'000 |
| Inflation | 1.5% | 0 – 10% |
| Erwartete Rendite | 6.0% | 1 – 20% |
| Pension (monatlich) | 1'800 | 0 – 10'000 |
| Kriegskasse | 10% | 0 – 40% |
| Cash‑Puffer | 2 Jahre | 0 – 6 |
| Max SWR | 4.0% | 2 – 7% |
| Einkommenssteuer | 20% | 0 – 50% |
| Kapitalertragssteuer | 0% | 0 – 35% |
| Vermögenssteuer | 0.20% p.a. | 0 – 2% |

---

## DE — Lizenz
MIT
