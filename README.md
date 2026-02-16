# ✈️ Capital Pilot — Strategic Withdrawal Simulation

### *Strategische Entnahme-Simulation*

<br>

<p align="center">
  <img src="https://img.shields.io/badge/version-5.0-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Version 5.0">
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

<br>

-----

<br>

## 🎯 What Is This? — *Was ist das?*

**Capital Pilot** is a single-file, zero-dependency retirement withdrawal simulator that answers the most important question in personal finance: **"How much can I spend per month — and will my money survive 30 years of market chaos?"**

It doesn't just calculate a number. It **stress-tests your strategy against real historical crises** — the 2008 Financial Crisis, the Dotcom Crash, COVID-19, Black Monday — and shows you exactly how your portfolio, cash buffer, and war chest interact when markets collapse. It models **taxes, housing costs, real estate appreciation**, and uses **sector-specific drawdown logic** with a hard -15% withdrawal stop rule.

-----

**Capital Pilot** ist ein Entnahme-Simulator in einer einzigen Datei, ohne externe Abhängigkeiten, der die wichtigste Frage der persönlichen Finanzplanung beantwortet: **„Wie viel kann ich pro Monat ausgeben — und überlebt mein Geld 30 Jahre Marktchaos?"**

Es berechnet nicht nur eine Zahl. Es **testet deine Strategie gegen echte historische Krisen** — die Finanzkrise 2008, den Dotcom-Crash, COVID-19, Black Monday — und zeigt dir exakt, wie dein Portfolio, dein Cash-Puffer und deine Kriegskasse zusammenspielen, wenn die Märkte einbrechen. Es modelliert **Steuern, Wohnkosten, Immobilienwertsteigerung** und verwendet eine **sektorspezifische Drawdown-Logik** mit harter -15% Entnahme-Stopp-Regel.

<br>

-----

<br>

## 💡 Why This Exists — *Warum das existiert*

Most retirement calculators use averages. Averages lie.

The **sequence of returns** matters more than the average return. Retiring into a 2008-style crash can destroy a plan that looks bulletproof on paper. This simulator lets you **slide the timeline** and watch what happens when the same crisis hits in year 1 vs year 15.

-----

Die meisten Rentenrechner arbeiten mit Durchschnitten. Durchschnitte lügen.

Die **Reihenfolge der Renditen** ist wichtiger als die Durchschnittsrendite. Ein Renteneintritt direkt in eine Krise wie 2008 kann einen Plan zerstören, der auf dem Papier kugelsicher aussieht. Dieser Simulator lässt dich die **Timeline verschieben** und beobachten, was passiert, wenn dieselbe Krise in Jahr 1 oder Jahr 15 kommt.

<br>

-----

<br>

## 🧠 The Three-Bucket Strategy — *Die Drei-Topf-Strategie*

The simulator models a sophisticated three-bucket retirement system:

| Bucket | Purpose | Behavior |
|---|---|---|
| 🔵 **ETF Depot** | Growth engine — your invested capital | Compounds at your expected return rate. Monthly withdrawals come from here in normal markets. |
| 🟢 **Cash Buffer** | Crisis shield — covers expenses during bear markets | X years of living expenses in cash. When markets crash, you withdraw from here instead of selling at the bottom. |
| 🟡 **War Chest** | Opportunity fund — buys the dip | Cash reserved to tactically buy at sector-specific thresholds. **Never used for living expenses.** |

### Advanced Drawdown Logic (v5)

The war chest uses **two-tier, sector-weighted thresholds**:

| Asset Class | Weight | Buy Tiers |
|---|---|---|
| **Standard** (World ETF) | 80% | -18%, -26%, -33% |
| **High-Beta** (Banks/Sectors) | 20% | -25%, -40%, -50% |

Each tier fires **once per crisis** and allocates 20/30/50% (Standard) or 15/30/55% (High-Beta) of the remaining war chest. This prevents shooting the powder too early on minor dips and reserves firepower for true capitulation events.

### The -15% Rule

When the depot drops more than **15% below its all-time high**, ETF withdrawals are **completely stopped**. Living expenses are covered exclusively from the cash buffer. Only when the buffer is empty does a reduced emergency withdrawal (35% of normal) resume from the depot.

-----

### Erweiterte Drawdown-Logik (v5)

Die Kriegskasse nutzt **zweistufige, sektorgewichtete Schwellen**:

| Asset-Klasse | Gewicht | Kauf-Stufen |
|---|---|---|
| **Standard** (Welt-ETF) | 80% | -18%, -26%, -33% |
| **High-Beta** (Banken/Sektoren) | 20% | -25%, -40%, -50% |

Jede Stufe feuert **einmal pro Krise**. Das verhindert, zu früh bei kleinen Dips das Pulver zu verschiessen.

### Die -15%-Regel

Wenn das Depot mehr als **15% unter dem Allzeithoch** liegt, werden ETF-Entnahmen **komplett gestoppt**. Lebenshaltung wird ausschliesslich aus dem Cash-Puffer gedeckt. Erst bei leerem Puffer gibt es eine reduzierte Notentnahme (35%) aus dem Depot.

<br>

-----

<br>

## 📊 Features — *Funktionen*

### Core Engine — *Kern-Engine*

- **Newton-Raphson Solver** — Analytically solves the withdrawal annuity with circular buffer dependency
- **11 Historical Crises (1973–2025)** — Oil Crisis, Volcker Recession, Black Monday, Gulf War, Asian/LTCM Crisis, Dotcom Crash, Global Financial Crisis, EU Debt Crisis, China/Oil Shock, COVID-19, 2022 Bear Market
- **Timeline Shifting** — Slide the start year ±5 years to test crisis timing
- **Inflation-Adjusted Withdrawals** — Expenses grow monthly, "Purchasing Power" KPI shows real value
- **-15% Drawdown Stop** — Hard withdrawal cutoff, forces buffer usage to protect depot
- **Two-Tier War Chest** — Sector-weighted thresholds with one-time-per-crisis activation
- **War Chest Protection** — Never used for living expenses, only for buying the dip
- **Dynamic Withdrawal Reduction** — Auto-reduces to 35% when depot critically low
- **Automatic Reserve Refill** — Excess growth replenishes buffer and war chest in good times

### Tax & Housing — *Steuern & Wohnen*

- **Three Tax Sliders** — Income tax (22%), capital gains (0% CH), wealth tax (0.30% p.a.)
- **Swiss Tax Defaults** — 0% Kapitalertragssteuer, Eigenmietwert as income, mortgage/maintenance deductions
- **Housing Toggle** — 🏠 Rent (rent + utilities) or 🏡 Ownership (mortgage, interest, maintenance, appreciation, imputed rent)
- **Real Estate Tracking** — Property net value in chart, counts toward legacy
- **Net Budget Breakdown** — Gross → Taxes → Housing → Net Available

### Currency & Language — *Währung & Sprache*

- **20 Currencies** — CHF, EUR, USD, GBP, PLN, CZK, HUF, RON, SEK, DKK, NOK, RUB, TRY, UAH, INR, CNY, JPY, CAD, AUD, BRL
- **Independent Pickers** — Currency and language are fully decoupled (German + CHF, English + EUR, etc.)
- **Smart Detection** — `de-CH`→CHF, `de-DE`→EUR, `en-US`→USD, `fr-CH`→CHF. Default: CHF
- **21 Languages** — EN, DE, FR, ES, IT, PT, NL, PL, RU, TR, SV, DA, NO, FI, CS, HU, RO, EL, UK, HI, ZH
- **420 Tooltips** — Every slider has an ⓘ hover-tooltip, translated in all 21 languages

### Interface — *Oberfläche*

- **3-Column Layout** — Parameters | Housing & Taxes | Chart & Analysis (responsive: 3→2→1 columns)
- **Allocation Bar in Header** — ETF / Buffer / War Chest always visible
- **Strategy Health** — Fragile → Moderate → Robust indicator
- **Max SWR Limiter** — Dynamic budget/legacy adjustment when capped
- **Stress Resistance KPI** — Months surviving -50% crash without selling ETFs
- **Drawdown Stop Counter** — Months stopped + war chest buy count
- **Crisis Tags** — Which historical events your portfolio survived

### Deployment — *Deployment*

- **Single HTML File** — No build step, no npm, no framework
- **100% Offline** — Chart.js from CDN (can be inlined)
- **GitHub Pages Ready** — Drop file, enable Pages, done
- **Touch-Optimized** — 22px slider thumbs, responsive grid
- **PWA Ready** — Add-to-homescreen meta tags

<br>

-----

<br>

## 🚀 Getting Started — *Schnellstart*

### Option 1: Just Open It

Download `capital-pilot.html` and open it in any browser. Done.

### Option 2: GitHub Pages

```bash
git init capital-pilot && cd capital-pilot
cp capital-pilot.html index.html
git add . && git commit -m "✈️ Capital Pilot v5"
git remote add origin https://github.com/YOUR_USER/capital-pilot.git
git push -u origin main
```

Live at `https://YOUR_USER.github.io/capital-pilot/`

### Option 3: Local Server

```bash
python3 -m http.server 8080
# → http://localhost:8080/capital-pilot.html
```

<br>

-----

<br>

## 🔬 The Math — *Die Mathematik*

### Solver

```
Given:
  C = Starting Capital,  K = War Chest = C × warChestPct
  B = Buffer Years × 12,  r = Monthly Growth Rate
  n = Duration (months),  F = (1 + r)^n,  L = Legacy Target

Circular dependency:  buffer = w × B,  invested = C - K - w × B

Annuity equation:     f(w) = (C - K - w×B) × F - w × (F-1)/r - L = 0
Newton-Raphson:       f'(w) = -B×F - (F-1)/r  (constant → instant convergence)
```

### Two-Tier War Chest

```
Standard (80%):   -18% → 20%,  -26% → 30%,  -33% → 50%  of remaining
High-Beta (20%):  -25% → 15%,  -40% → 30%,  -50% → 55%  of remaining
Each tier fires ONCE per crisis. Tiers reset for new crises.
```

### Tax Model

```
Income Tax    = (Pension + Imputed Rent - Deductions) × Rate
Capital Gains = ETF Withdrawal × Gains Ratio × CG Rate
Wealth Tax    = Total Wealth × Rate / 12
Net Budget    = Gross - Income Tax - CG Tax - Wealth Tax - Housing
```

### Stress Resistance

```
Months = Cash Buffer / Monthly Withdrawal
(War chest excluded — reserved for buying, never spending)
```

<br>

-----

<br>

## ⚙️ Default Parameters (Swiss Calibration)

| Parameter | Default | Range |
|---|---|---|
| Starting Capital | 1'000'000 CHF | 300k – 5M |
| Duration | 30 years | 10 – 50 |
| Target Legacy | 0 CHF | 0 – 3M |
| Inflation | 1.0% | 0 – 5% |
| Expected Return | 7.0% | 2 – 12% |
| War Chest | 15.0% | 0 – 35% |
| Cash Buffer | 4.0 years | 0 – 5 |
| Pension (AHV/PK) | 1'500 CHF/mt | 0 – 8'000 |
| Max SWR | 5.2% | 2 – 8% |
| Income Tax | 22% | 0 – 100% |
| Capital Gains Tax | 0% (CH) | 0 – 100% |
| Wealth Tax | 0.30% p.a. | 0 – 3% |
| Monthly Rent | 1'500 CHF | 0 – 5'000 |

<br>

-----

<br>

## 🏗️ Architecture

```
capital-pilot.html (~1400 lines, single file)
│
├── HTML
│   ├── Header: Title + Allocation Bar + $ Currency + 🌐 Language
│   ├── Col Left: Base Params + Market Strategy + Safety Limits
│   ├── Col Mid: Housing (Rent/Own) + Taxes (3 sliders) + Net Budget
│   └── Col Right: 4 KPI Cards → Health → Chart → Stats → Info
│
├── CSS (embedded)
│   ├── 3-column responsive grid (1200px/1024px/mobile breakpoints)
│   ├── Housing toggle, tooltip system, budget breakdown
│   └── Dark glass-panel aesthetic
│
└── JavaScript (embedded)
    ├── i18n (21 langs × 80+ keys + 420 tooltips)
    ├── Currency (20 currencies, smart browser detection)
    ├── Crisis DB (11 events, 1973–2025)
    ├── Newton-Raphson Solver
    ├── Simulation Engine
    │   ├── Two-tier war chest (Std -18/-26/-33 + HB -25/-40/-50)
    │   ├── -15% drawdown stop
    │   ├── War chest protection (buy only, never spend)
    │   ├── Wealth tax deduction
    │   ├── Property value tracking
    │   └── Stress resistance calc
    ├── Tax Engine (income/CG/wealth, CH deductions)
    ├── Housing Engine (rent vs own, Eigenmietwert)
    └── Chart.js (crisis shading, legacy line, property line)
```

<br>

-----

<br>

## 🔄 Version History

| Version | Changes |
|---|---|
| **v5.0** | Tax system (3 sliders, CH defaults), housing module (rent/own), real estate tracking, net budget breakdown, two-tier war chest, -15% drawdown stop, war chest protection, stress resistance KPI, 3-column layout, 420 tooltips (21 langs), 20 currencies (independent), allocation bar in header, Swiss calibration |
| **v4.0** | Max SWR limiter, historical crisis timeline (1973–2025), 11 real events |
| **v3.0** | 21 languages, Newton-Raphson solver, three-bucket strategy |
| **v2.0** | Mobile responsive, Strategy Health indicator, crisis tags |
| **v1.0** | Initial release |

<br>

-----

<br>

## ⚠️ Disclaimer — *Haftungsausschluss*

**This is a simulation tool for educational purposes. It is not financial advice.**

Past performance does not predict future results. Tax calculations are approximations — consult a tax advisor for your specific situation. Always consult a qualified financial advisor before making retirement decisions.

-----

**Dies ist ein Simulationswerkzeug zu Bildungszwecken. Es stellt keine Finanzberatung dar.**

Vergangene Wertentwicklungen sind kein verlässlicher Indikator für zukünftige Ergebnisse. Steuerberechnungen sind Näherungswerte — konsultiere einen Steuerberater. Konsultiere immer einen qualifizierten Finanzberater vor Pensionierungsentscheidungen.

<br>

-----

<br>

<p align="center">
  <b>Built with obsessive attention to financial math and zero dependencies.</b><br>
  <i>Gebaut mit obsessiver Aufmerksamkeit für Finanzmathematik und null Abhängigkeiten.</i>
</p>

<p align="center">
  ✈️
</p>
