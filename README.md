# ✈️ Capital Pilot — Strategic Withdrawal Simulation (v6.0)

<p align="center">
  <img src="https://img.shields.io/badge/version-6.0-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Version 6.0">
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

## EN — What's New in v6.0

### 🔄 Dynamic ATH Rebalancing (Fair-Weather Logic)
When the ETF depot reaches a **new all-time high (ATH)**, the simulation automatically triggers a rebalancing event: a fraction (up to 1.5%) of the surplus above the ATH is used to refill the **Cash Buffer** and **War Chest** back to their target levels. This "fair-weather logic" ensures that prolonged bull markets don't leave your crisis shields depleted. The number of such events is tracked and displayed in the Withdrawal Analysis section.

**Strategic importance:** This solves a critical problem with static bucket strategies — after a long bull market, your buffer and war chest can drift far below their targets, leaving you unprotected when a correction finally arrives. Dynamic rebalancing keeps the 3-bucket combination perpetually "battle-ready."

### ⚖️ Opportunity Cost Indicator
A parallel **Buy & Hold simulation** now runs alongside the main 3-bucket strategy. The results panel shows:
- **B&H End Wealth** — what would happen if you invested 100% in ETF with no buffers
- **Strategy End Wealth** — your actual 3-bucket end wealth
- **Delta** — whether your strategy outperforms or trails pure Buy & Hold

When the strategy trails B&H, a contextual note explains that the 3-bucket combination provides **behavioral and crisis-protection benefits** (no forced selling at the bottom, sleep-at-night factor) that simple wealth comparison doesn't capture. This is crucial context: the strategy's true ROI includes avoided panic-selling losses and psychological stability.

### 🌗 Light / Dark Mode Toggle
A new **Light/Dark mode** toggle button (☀️/🌙) is now available in the top-right control bar, next to the language picker. Both themes use the same cohesive color system — the dark mode is the default professional dashboard look; the light mode offers a clean, print-friendly alternative. The toggle is **fully translated** across all 21 languages.

---

## EN — Overview

**Capital Pilot** is a single-file, offline-friendly retirement withdrawal simulator. It answers one question:  
**How much can I spend per month — and will my strategy survive decades of market chaos?**

It models a **three-bucket setup** (ETF depot + cash buffer + war chest), **taxes**, **housing** (rent vs. ownership), and a **crisis engine** that lets you navigate real history and generate random crisis-driven futures.

---

## EN — Why the 3-Bucket Strategy?

The combination of ETF Depot + Cash Buffer + War Chest is strategically superior to simple Buy & Hold for retirees for three compounding reasons:

| Problem | 3-Bucket Solution |
|---|---|
| **Sequence-of-Returns Risk** | Cash Buffer covers 2–6 years of expenses — you never sell ETF at the bottom |
| **Crash Opportunity** | War Chest buys the dip at -18%, -26%, -33% thresholds — crises become opportunities |
| **Behavioral Finance** | Knowing you have 2+ years of cash eliminates panic selling — the biggest destroyer of long-term returns |
| **Perpetual Readiness** | ATH Rebalancing refills buffers automatically in bull markets — you're always crisis-ready |

The Opportunity Cost Indicator makes the trade-off explicit: in some scenarios, B&H wins on pure numbers. But the 3-bucket strategy wins on **risk-adjusted, behaviorally-stable, survivable outcomes** — especially critical in volatile sequences.

---

## EN — Key Features

### Three-Bucket Withdrawal Strategy

| Bucket | Purpose | Behavior |
|---|---|---|
| 🔵 **ETF Depot** | Growth engine | Compounds with expected return. Withdrawals come from here in normal markets. |
| 🟢 **Cash Buffer** | Crisis shield | Covers expenses when markets crash (withdrawals from ETFs can stop). ATH Rebalancing refills this. |
| 🟡 **War Chest** | Opportunity fund | Reserved for dip-buying at drawdown thresholds; **never used for living expenses**. ATH Rebalancing refills this. |

### Dynamic ATH Rebalancing (NEW in v6.0)
- Triggered every time the ETF depot sets a **new all-time high**
- Uses up to **1.5% of the surplus** above the ATH
- Priority: Buffer first (65%), War Chest second (35%)
- Refills back to 100% of respective target levels
- Rebalancing event count shown in Withdrawal Analysis panel

### Opportunity Cost Indicator (NEW in v6.0)
- **Parallel B&H simulation** using the same total starting capital
- B&H applies the same monthly withdrawals (inflation-adjusted) directly from depot
- End-of-period comparison shows exact delta in your currency
- Contextual annotation explains when strategy protection justifies the trade-off

### Light / Dark Mode Toggle (NEW in v6.0)
- 🌙 Dark: default professional dashboard (deep navy, luminous accents)
- ☀️ Light: clean paper-white UI (high contrast, print-friendly)
- Toggle button in top-right control bar (next to language picker)
- Translated label in all 21 supported languages
- Chart colors and grid adapt automatically

### Crisis Engine (History + Random Forecast)

**History mode (← 5Y / 5Y →)**  
- Scroll through real historical windows and see crisis markers and shading.

**Random forecast mode (↻)**  
- Anchors start at **Today**
- Picks from realistic crisis types: Banking crisis, Oil price shock, Pandemic, Hyperinflation
- Places events across the full horizon: ≥ 1 major crisis per 10 years + smaller crises
- Each click generates a **new, different future**
- **Buy & Hold comparison line** is also randomized with the same crisis overlay

### Tax & Housing
- Income tax, Capital gains tax, Wealth tax
- **Eigenmietwert** applied only when currency = CHF
- 🏠 Rent / 🏡 Own toggle with full property and mortgage modeling
- Net budget breakdown: Gross → Taxes → Housing → Net Available

### Currency & Language
- **20 currencies** | **21 languages** — fully decoupled
- All new features (rebalancing, opportunity cost, theme) fully translated in EN and DE; fallbacks for other languages

---

## EN — Historical Crisis Database (1973–2025)

- 1973 Oil Crisis · Volcker Recession · Black Monday (1987) · Gulf War
- Asian / LTCM Crisis (1997–98) · Dotcom Crash (2000)
- Global Financial Crisis (2008) · EU Debt Crisis (2011)
- China / Oil Shock (2015) · COVID-19 Crash (2020)
- 2022 Bear Market · **Trump Tariff Crisis (2025)**

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

## EN — Defaults & Ranges

| Parameter | Default | Range |
|---|---:|---:|
| Starting Capital | 1'200'000 | **Currency-dependent** (CHF: 100k–10M) |
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
├── CSS  (responsive glass UI, dark/light CSS variables)
└── JS
    ├── i18n (21 languages, incl. new rebalancing/opp-cost/theme keys)
    ├── currency engine (20 currencies, scaled ranges)
    ├── housing + tax engine (CHF-only Eigenmietwert)
    ├── crisis DB (1973–2025 + Trump Tariff Crisis)
    ├── crisis engine (history navigation + random forecast)
    ├── simulation engine
    │   ├── Newton-Raphson solver (withdrawal rate)
    │   ├── 3-bucket simulation (buffer + war chest + drawdown stops)
    │   ├── ATH rebalancing (fair-weather buffer/war chest refill) ← NEW
    │   └── B&H parallel simulation (opportunity cost baseline) ← NEW
    ├── theme engine (dark/light mode toggle) ← NEW
    └── Chart.js rendering (shading + crisis tags + B&H line) ← UPDATED
```

---

## EN — License
MIT

---

# DE — Überblick

**Capital Pilot** ist ein Entnahme-Simulator in einer einzigen HTML-Datei (offline-freundlich). Kernfrage:  
**Wie viel kann ich pro Monat ausgeben — und überlebt meine Strategie Jahrzehnte voller Marktkrisen?**

---

## DE — Neu in v6.0

### 🔄 Dynamisches ATH-Rebalancing (Schönwetter-Logik)
Sobald das ETF-Depot ein **neues Allzeithoch (ATH)** erreicht, löst die Simulation ein Rebalancing-Ereignis aus: Bis zu 1,5% des Überschusses über das ATH werden automatisch genutzt, um den **Cash-Puffer** und die **Kriegskasse** auf ihr Zielniveau aufzufüllen. Diese "Schönwetter-Logik" verhindert, dass Ihre Krisen-Schutzpuffer in langen Bullenmärkten auf ein kritisches Niveau schrumpfen.

**Strategische Bedeutung:** Ohne aktives Rebalancing kann ein langer Bullenmarkt dazu führen, dass Puffer und Kriegskasse weit unter ihr Ziel driften — und Sie beim nächsten Einbruch schutzlos dastehen. Das ATH-Rebalancing hält die 3-Töpfe-Kombination dauerhaft "gefechtsbereit".

### ⚖️ Opportunitätskosten-Indikator
Eine parallele **Buy-&-Hold-Simulation** läuft nun neben der Hauptstrategie. Der Ergebnisbereich zeigt:
- **B&H Endvermögen** — Was wäre passiert bei 100% ETF, ohne Puffer?
- **Strategie Endvermögen** — Ihr tatsächliches 3-Töpfe-Endvermögen
- **Delta** — Ob Ihre Strategie besser oder schlechter als reines Buy & Hold abschneidet

Liegt die Strategie zurück, erscheint ein erläuternder Hinweis: Die 3-Töpfe-Kombination bietet **Verhaltensschutz und Krisenwiderstandsfähigkeit**, die ein einfacher Vermögensvergleich nicht abbildet — insbesondere der Schutz vor Panikverkäufen auf dem Tiefpunkt.

### 🌗 Hell/Dunkel-Umschalter
Ein neuer **Hell/Dunkel-Modus**-Button (☀️/🌙) befindet sich jetzt in der oberen rechten Steuerleiste neben dem Sprachpicker. Beide Themes nutzen dasselbe konsistente Farbsystem und sind in allen 21 Sprachen übersetzt.

---

## DE — Warum 3 Töpfe?

| Problem | 3-Töpfe-Lösung |
|---|---|
| **Sequence-of-Returns-Risiko** | Cash-Puffer deckt 2–6 Jahre — kein ETF-Verkauf am Tiefpunkt |
| **Crash-Chance** | Kriegskasse kauft bei -18%, -26%, -33% nach — Krisen werden zur Chance |
| **Verhaltensfinanz** | 2+ Jahre Cash eliminiert Panikverkäufe — der größte Renditekiller |
| **Perpetuelle Bereitschaft** | ATH-Rebalancing füllt Puffer automatisch auf — immer krisenfest |

---

## DE — Schnellstart

```bash
# Option 1: Direkt öffnen
# index.html im Browser öffnen

# Option 2: Lokaler Server
python3 -m http.server 8080
# http://localhost:8080/
```

---

## DE — Lizenz
MIT

---

## EN — Disclaimer

This is a simulation tool for **educational purposes only**. It does not constitute financial, tax, or investment advice. Past performance does not predict future results. Tax calculations are approximations — consult a qualified tax advisor. Always seek professional financial advice before making retirement decisions. The author assumes no liability for decisions made based on this tool.

---

## DE — Haftungsausschluss

Dies ist ein Simulationswerkzeug ausschliesslich zu **Bildungszwecken**. Es stellt keine Finanz-, Steuer- oder Anlageberatung dar. Vergangene Wertentwicklungen sind kein Indikator für zukünftige Ergebnisse. Steuerberechnungen sind Näherungswerte — konsultiere einen qualifizierten Steuerberater. Hole immer professionelle Finanzberatung ein, bevor du Pensionierungsentscheidungen triffst. Der Autor übernimmt keine Haftung für Entscheidungen, die auf Basis dieses Tools getroffen werden.
