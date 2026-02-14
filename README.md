# 🏰 Financial Fortress — Withdrawal Simulation

### *Finanz Festung — Strategische Entnahme-Simulation*

<br>

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Version 4.0">
  <img src="https://img.shields.io/badge/languages-21-a78bfa?style=for-the-badge&labelColor=0f172a" alt="21 Languages">
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

**Financial Fortress** is a single-file, zero-dependency retirement withdrawal simulator that answers the most important question in personal finance: **“How much can I spend per month — and will my money survive 30 years of market chaos?”**

It doesn’t just calculate a number. It **stress-tests your strategy against real historical crises** — the 2008 Financial Crisis, the Dotcom Crash, COVID-19, Black Monday — and shows you exactly how your portfolio, cash buffer, and war chest interact when markets collapse.

-----

**Finanz Festung** ist ein Entnahme-Simulator in einer einzigen Datei, ohne externe Abhängigkeiten, der die wichtigste Frage der persönlichen Finanzplanung beantwortet: **„Wie viel kann ich pro Monat ausgeben — und überlebt mein Geld 30 Jahre Marktchaos?”**

Es berechnet nicht nur eine Zahl. Es **testet deine Strategie gegen echte historische Krisen** — die Finanzkrise 2008, den Dotcom-Crash, COVID-19, Black Monday — und zeigt dir exakt, wie dein Portfolio, dein Cash-Puffer und deine Kriegskasse zusammenspielen, wenn die Märkte einbrechen.

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

|Bucket           |Purpose                                            |Behavior                                                                                                        |
|-----------------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|🔵 **ETF Depot**  |Growth engine — your invested capital              |Compounds at your expected return rate. Monthly withdrawals come from here in normal markets.                   |
|🟢 **Cash Buffer**|Crisis shield — covers expenses during bear markets|X years of living expenses in cash. When markets crash, you withdraw from here instead of selling at the bottom.|
|🟡 **War Chest**  |Opportunity fund — buys the dip                    |Cash reserved to tactically buy cheap when markets panic. Automatically deploys during drops >1.5%.             |

During a crisis, the system **automatically pivots**: withdrawals shift from the ETF to the buffer, while the war chest buys discounted shares. When markets recover, excess growth gradually refills both reserves.

-----

Der Simulator modelliert ein ausgeklügeltes Drei-Topf-System:

|Topf             |Zweck                                      |Verhalten                                                                                       |
|-----------------|-------------------------------------------|------------------------------------------------------------------------------------------------|
|🔵 **ETF-Depot**  |Wachstumsmotor — das investierte Kapital   |Wächst mit der erwarteten Rendite. Monatliche Entnahmen kommen im Normalfall von hier.          |
|🟢 **Cash-Puffer**|Krisenschild — deckt Ausgaben im Bärenmarkt|X Jahre Lebenskosten in Cash. Bei Crash wird von hier entnommen statt am Tiefpunkt zu verkaufen.|
|🟡 **Kriegskasse**|Gelegenheitsfonds — kauft den Dip          |Cash-Reserve für taktische Nachkäufe bei Panik. Automatischer Einsatz bei Einbrüchen >1.5%.     |

In einer Krise **schaltet das System automatisch um**: Entnahmen wechseln vom ETF zum Puffer, während die Kriegskasse vergünstigte Anteile kauft. Bei Erholung füllen Überschüsse beide Reserven schrittweise wieder auf.

<br>

-----

<br>

## 📊 Features — *Funktionen*

### Core Engine — *Kern-Engine*

- **Newton-Raphson Solver** — Analytically solves the withdrawal annuity with circular buffer dependency. Converges in <10 iterations, not a “guess and check” approximation.
- **11 Historical Crises (1975–2025)** — Oil Crisis, Volcker Recession, Black Monday, Gulf War, Asian/LTCM Crisis, Dotcom Crash, Global Financial Crisis, EU Debt Crisis, China/Oil Shock, COVID-19, 2022 Bear Market.
- **Timeline Shifting** — Slide the start year ±5 years to see how early or late crises affect your plan. Start in 1995 and you’ll retire into the Dotcom crash. Start in 2005 and you’ll face the GFC.
- **Inflation-Adjusted Withdrawals** — Your expenses grow with inflation every month. The “Purchasing Power” KPI shows what your nominal budget is actually worth in year 30.
- **Dynamic Withdrawal Reduction** — If your depot drops below 40% of initial value, withdrawals automatically reduce (down to 35% of planned) to prevent a death spiral.
- **Automatic Reserve Refill** — When markets are strong (depot >70% of initial), excess growth quietly replenishes the buffer and war chest.

### Interface — *Oberfläche*

- **21 Languages** — EN, DE, FR, ES, IT, PT, NL, PL, RU, TR, SV, DA, NO, FI, CS, HU, RO, EL, UK, HI, ZH. Auto-detects browser language; falls back to English.
- **Strategy Health Indicator** — One-glance assessment: Fragile → Moderate → Robust. Factors in SWR, allocation balance, and buffer depth.
- **Crisis Tags** — Shows exactly which historical events your portfolio survived in the current simulation.
- **Real-Year Chart Labels** — X-axis shows actual calendar years (e.g., 2007, 2008, 2009) so you can visually map events to portfolio reactions.
- **Legacy Target Line** — Dashed line on chart shows your inheritance goal for visual reference.
- **Warning System** — Real-time alerts for dangerous parameters: SWR >5%, ETF allocation <15%, impossible withdrawal targets.

### Mobile & Deployment — *Mobil & Deployment*

- **Single HTML File** — No build step, no npm, no framework. One file. Done.
- **100% Offline** — Only external dependency is Chart.js from CDN (which can be inlined for fully air-gapped use).
- **GitHub Pages Ready** — Drop the file into a repo, enable Pages, you’re live.
- **Touch-Optimized** — 22px slider thumbs, responsive grid (2-column KPIs on mobile, 4 on desktop), adaptive chart height.
- **PWA Meta Tags** — Add-to-homescreen ready on iOS and Android.

<br>

-----

<br>

## 🚀 Getting Started — *Schnellstart*

### Option 1: Just Open It — *Einfach öffnen*

Download `finanz-festung-v4.html` and open it in any browser. That’s it.

Lade `finanz-festung-v4.html` herunter und öffne die Datei in einem beliebigen Browser. Fertig.

### Option 2: GitHub Pages

```bash
# Create a repository
git init financial-fortress
cd financial-fortress

# Add the file as index.html
cp finanz-festung-v4.html index.html
git add index.html
git commit -m "🏰 Financial Fortress v4"

# Push and enable GitHub Pages in Settings → Pages → main branch
git remote add origin https://github.com/YOUR_USER/financial-fortress.git
git push -u origin main
```

Your simulator is now live at `https://YOUR_USER.github.io/financial-fortress/`

### Option 3: Local Development — *Lokale Entwicklung*

```bash
# Any static server works
python3 -m http.server 8080
# Open http://localhost:8080/finanz-festung-v4.html
```

<br>

-----

<br>

## 🔬 The Math — *Die Mathematik*

### Solver

The core calculation solves for the optimal monthly withdrawal `w` from the ETF depot:

```
Given:
  C = Starting Capital
  K = War Chest = C × warChestPct
  B = Buffer Years × 12 (months)
  r = Monthly Growth Rate (annual / 12)
  n = Duration in Months
  F = (1 + r)^n (compound factor)
  L = Legacy Target (from ETF portion)

Circular dependency:
  buffer = w × B
  invested = C - K - w × B

Annuity equation:
  f(w) = (C - K - w×B) × F - w × (F-1)/r - L = 0

Newton-Raphson:
  f'(w) = -B×F - (F-1)/r    ← constant, converges in 1-2 steps
  w_new = w - f(w) / f'(w)
```

The beauty: `f'(w)` doesn’t depend on `w`, so Newton-Raphson converges essentially in a single step (with guards for edge cases where `invested < 0`).

### Crisis Model

Each historical crisis has four parameters derived from actual S&P 500 / MSCI World data:

|Parameter        |Description                                           |
|-----------------|------------------------------------------------------|
|`totalDrop`      |Total peak-to-trough decline (e.g., -0.57 for the GFC)|
|`durationMonths` |Months from peak to trough                            |
|`recovery`       |Months from trough to previous peak                   |
|`startYear/Month`|Calendar start of the crisis                          |

Monthly returns during a crisis follow a **front-loaded sine curve** — sharp initial drops that gradually flatten toward the bottom — which matches real market behavior better than linear distribution.

### Safe Withdrawal Rate (SWR)

The displayed SWR is calculated as:

```
SWR = (monthlyETF × 12) / totalCapital × 100
```

The classic “4% rule” (Trinity Study) assumed a 30-year period with a 50/50 stock/bond mix. This simulator goes further by modeling real crisis sequences and dynamic withdrawal adjustment.

<br>

-----

<br>

## ⚙️ Parameters — *Parameter*

|Parameter       |Range        |Default  |Description                                    |
|----------------|-------------|---------|-----------------------------------------------|
|Starting Capital|300k – 5M CHF|1’983’000|Total portfolio value at retirement start      |
|Duration        |10 – 50 years|30       |How long your money needs to last              |
|Target Legacy   |0 – 3M CHF   |500’000  |How much you want to leave behind              |
|Inflation       |0 – 5% p.a.  |2.0%     |Annual inflation rate applied to withdrawals   |
|Expected Return |2 – 12% p.a. |7.0%     |Nominal annual return on ETF portfolio         |
|War Chest       |0 – 35%      |16.8%    |Percentage of capital reserved for crash buying|
|Cash Buffer     |0 – 5 years  |3.0      |Years of expenses held in cash                 |
|Pension         |0 – 8’000 CHF|1’500    |Monthly pension income (AHV/PK/Social Security)|

<br>

-----

<br>

## 📱 Browser Support — *Browser-Kompatibilität*

|Browser         |Desktop|Mobile|
|----------------|-------|------|
|Chrome          |✅      |✅     |
|Firefox         |✅      |✅     |
|Safari          |✅      |✅     |
|Edge            |✅      |✅     |
|Samsung Internet|—      |✅     |

<br>

-----

<br>

## 🏗️ Architecture — *Architektur*

```
finanz-festung-v4.html
│
├── HTML Structure
│   ├── Header + Language Picker (Globe Icon)
│   ├── Sidebar: 8 Parameter Sliders + Allocation Bar + Warnings
│   └── Main: KPI Cards → Health Bar → Chart → Stats → Info
│
├── CSS (embedded)
│   ├── CSS Variables for theming
│   ├── Mobile-first responsive grid
│   └── Glass-panel aesthetic with subtle grid background
│
└── JavaScript (embedded)
    ├── i18n System (21 language objects, browser detection)
    ├── Historical Crisis Database (11 events, 1975-2025)
    ├── Newton-Raphson Solver (analytical derivative)
    ├── Simulation Engine (crisis overlay, dynamic withdrawal, refill logic)
    ├── Chart.js Rendering (custom crisis shading plugin, legacy line)
    └── Reactive UI (slider → recalc → render pipeline)
```

<br>

-----

<br>

## 🤝 Contributing — *Mitwirken*

Found a bug? Have an idea? Contributions welcome.

- **Historical data corrections** — More accurate crisis parameters
- **New languages** — Add a language object to the `LANGS` dictionary
- **New features** — Multi-run Monte Carlo overlay, sequence-of-returns risk score, PDF export

<br>

-----

<br>

## ⚠️ Disclaimer — *Haftungsausschluss*

**This is a simulation tool for educational purposes. It is not financial advice.**

Past performance does not predict future results. Historical crisis patterns may not repeat. The solver assumes constant expected returns outside of crises, which is an oversimplification. Real-world factors like taxes, healthcare costs, currency risk, and black swan events are not modeled. Always consult a qualified financial advisor before making retirement decisions.

-----

**Dies ist ein Simulationswerkzeug zu Bildungszwecken. Es stellt keine Finanzberatung dar.**

Vergangene Wertentwicklungen sind kein verlässlicher Indikator für zukünftige Ergebnisse. Historische Krisenmuster müssen sich nicht wiederholen. Der Solver nimmt konstante Renditeerwartungen ausserhalb von Krisen an, was eine Vereinfachung ist. Reale Faktoren wie Steuern, Gesundheitskosten, Währungsrisiken und Black-Swan-Ereignisse werden nicht modelliert. Konsultiere immer einen qualifizierten Finanzberater vor Pensionierungsentscheidungen.

<br>

-----

<br>

<p align="center">
  <b>Built with obsessive attention to financial math and zero dependencies.</b><br>
  <i>Gebaut mit obsessiver Aufmerksamkeit für Finanzmathematik und null Abhängigkeiten.</i>
</p>

<p align="center">
  🏰
</p>
