# ✈️ Capital Pilot — Strategic Withdrawal Simulation (v6.2)

<p align="center">
  <img src="https://img.shields.io/badge/version-6.2-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Version 6.2">
  <img src="https://img.shields.io/badge/languages-21-a78bfa?style=for-the-badge&labelColor=0f172a" alt="21 Languages">
  <img src="https://img.shields.io/badge/currencies-20-fbbf24?style=for-the-badge&labelColor=0f172a" alt="20 Currencies">
  <img src="https://img.shields.io/badge/offline-100%25-34d399?style=for-the-badge&labelColor=0f172a" alt="Offline Ready">
  <img src="https://img.shields.io/badge/mobile-optimized-fbbf24?style=for-the-badge&labelColor=0f172a" alt="Mobile Ready">
  <img src="https://img.shields.io/badge/export-CSV%20%7C%20JSON%20%7C%20HTML-fb7185?style=for-the-badge&labelColor=0f172a" alt="Export">
  <img src="https://img.shields.io/badge/license-MIT-64748b?style=for-the-badge&labelColor=0f172a" alt="MIT License">
</p>

<p align="center">
  <b>Can you retire early without running out of money?</b><br>
  <i>Kannst du früh in Rente gehen, ohne dass das Geld ausgeht?</i>
</p>

---

## EN — Overview

**Capital Pilot** is a single-file, offline-ready retirement withdrawal simulator. It answers one central question:

> **How much can I spend per month — and will my strategy survive decades of market chaos?**

It models a **three-bucket setup** (ETF Depot + Cash Buffer + War Chest), **taxes**, **housing** (rent vs. ownership with full mortgage modelling), and a **crisis engine** that replays real market history or generates probabilistic random futures. All calculation runs locally in your browser — no server, no account, no data upload.

---

## EN — What's New in v6.2

### 📤 Simulation Data Export — CSV · JSON · HTML Report

A new **Export button** (↓ icon) appears in the Withdrawal Analysis panel. One click opens a modal with three export formats. Everything is generated locally in the browser — no data ever leaves your device.

**CSV — Monthly Detail** (Excel / LibreOffice / Numbers)

Every row is one simulation month. Columns:

| Column | Description |
|---|---|
| Year / Month | Calendar date of the simulation step |
| ETF Depot | ETF portfolio value at end of month |
| Cash Buffer | Cash Buffer balance at end of month |
| War Chest | War Chest balance at end of month |
| Property Net | Net property value (ownership mode only) |
| Total Wealth | Sum of all buckets + property |
| Buy & Hold | Parallel B&H simulation value for same month |
| Strategy vs B&H | Delta: 3-bucket total minus B&H value |
| Drawdown % | Current drawdown from all-time high |
| ETF Monthly Return % | Approximate ETF return for this month |
| Cash Interest | Money-market interest earned by Buffer + War Chest |
| InCrisis Flag | 1 = crisis phase active, 0 = normal |

The file opens with a parameter block (capital, duration, rates, full KPI summary) as comment lines. Uses semicolon separator + UTF-8 BOM for direct compatibility with European Excel, LibreOffice, and Apple Numbers.

**JSON — Full Structured Data**

Machine-readable export with four top-level sections: `meta`, `parameters`, `kpiSummary`, `crisisEvents[]`, and `monthlyData[]`. Ideal for Python (`pandas.read_json()`), Excel Power Query, Power BI, or any custom dashboard.

**HTML Report — Print / Archive**

A self-contained, internet-free printable report. Includes:
- Full parameter table
- 8 KPI cards: End Wealth, B&H End Wealth, Delta, Crises Survived, Rebalancing Events, Buffer Months Used, Drawdown Stop Months, Worst Depot
- Crisis events table with name, date, duration, total drop, recovery, and type
- Yearly milestones table: ETF Depot, Buffer, War Chest, Total Wealth, B&H, Strategy vs B&H delta, Drawdown %, Crisis flag
- Print-ready CSS — use browser Print → Save as PDF for a clean, shareable document

All formats reflect the exact simulation state at export time: timeline, crisis overlay, currency, language, and all parameter values.

---

## EN — What's New in v6.1

### 1. 🏷️ Purchasing Power Label Correction
The KPI previously showed *"real (today)"* — misleading, because the value displayed is the inflation-discounted buying power of your monthly budget **at the end** of the withdrawal period. The label now correctly reads **"real (at end)"** (DE: *"real (am Ende)"*). The sublabel dynamically shows the selected duration, e.g. *"real purchasing power after 30 years"*.

### 2. 🔄 Smart Surplus & Refill Management
When the Max SWR slider caps your budget below the solver's optimum, the monthly difference — the "surplus" — no longer sits idle in the ETF depot. The simulation now routes it through a strict priority waterfall every normal-market month:

**Priority 1: Cash Buffer** (filled to 100% of target) → **Priority 2: War Chest** (filled to 100% of target) → **Priority 3: ETF Depot** (remainder stays here)

Each bucket fill above 1 unit increments the Rebalancing Event counter. The SWR info panel shows the live surplus amount and its current destination in real time.

### 3. 💰 Money-Market Interest on Cash Buckets
Both the Cash Buffer and War Chest now compound at **1.5% p.a.** (monthly compounding), matching realistic current money-market ETF yields (e.g. iShares € Government Bond 0-1yr, Lyxor Smart Cash). Previously modelled at 2.0% p.a. A permanent note in the Safety Limits panel confirms the rate.

### 4. 📊 Extended SWR Transparency Panel
The info box below the SWR slider now shows three additional lines when SWR capping is active: the monthly surplus amount, its current routing destination (Buffer / War Chest / ETF), and the projected legacy impact. The 1.5% cash interest note is always visible — even when SWR is not capped.

### 5. ⚡ Relaxed Rebalancing Logic — Dual Trigger
The original ATH Rebalancing from v6.0 only fired on a strict new all-time high. After a significant correction, the depot can recover strongly for months without technically exceeding its pre-crash ATH — leaving buffers depleted far too long. Rebalancing now fires on two independent conditions:

1. **Strict ATH trigger** (original v6.0): depot exceeds previous all-time high
2. **5% growth trigger** *(new)*: depot has grown more than 5% compared to 12 months ago, AND at least one bucket is below 95% of its target

This dual-trigger ensures post-crisis buffer regeneration happens during recovery — not only once the market has fully reclaimed its peak.

---

## EN — What's New in v6.0

### 🔄 Dynamic ATH Rebalancing (Fair-Weather Logic)
When the ETF depot sets a new all-time high, up to 1.5% of the surplus above ATH is used to refill the Cash Buffer (65% share) and War Chest (35% share) back to their target levels. Solves the core problem of static bucket strategies: after a long bull market, shields can drift well below target — leaving you exposed when the next correction arrives. The number of rebalancing events is tracked and shown in the Withdrawal Analysis panel.

### ⚖️ Opportunity Cost Indicator
A parallel Buy & Hold simulation runs alongside the main 3-bucket strategy using identical starting capital and monthly withdrawals. The results panel shows B&H End Wealth, Strategy End Wealth, and the exact delta. When the strategy trails B&H, a contextual annotation explains that the 3-bucket combination provides behavioural and crisis-protection benefits not captured in a simple wealth comparison — particularly the elimination of forced selling at market bottoms.

### 🌗 Light / Dark Mode Toggle
A ☀️/🌙 toggle button in the top-right control bar. Both themes use the same cohesive colour system. The label is fully translated across all 21 supported languages.

---

## EN — Core Strategy: Why 3 Buckets?

The combination of ETF Depot + Cash Buffer + War Chest is strategically superior to pure Buy & Hold for retirees on four compounding dimensions:

| Problem | 3-Bucket Solution |
|---|---|
| **Sequence-of-Returns Risk** | Cash Buffer covers 2–6 years of expenses — you never sell ETF at the bottom |
| **Crash Opportunity** | War Chest deploys at −18%, −26%, −33% drawdown thresholds — crises become buying opportunities |
| **Behavioural Finance** | 2+ years of living expenses in cash eliminates panic selling — the single biggest destroyer of long-term returns |
| **Perpetual Readiness** | Dual-trigger rebalancing + SWR surplus refill keeps all buckets battle-ready at all times |

The Opportunity Cost Indicator makes the trade-off explicit: in some scenarios, pure B&H wins on raw end wealth. But the 3-bucket strategy wins on **risk-adjusted, behaviourally stable, survivable outcomes** — especially critical in adverse return sequences where sequence risk destroys a pure-ETF retiree's portfolio.

---

## EN — Full Feature Reference

### Simulation Engine

**Monthly loop mechanics:**
- ETF depot compounds with expected return ± random noise (±0.75% per month)
- Crisis return profile: sine-wave drawdown curve + random volatility during crash phases
- Recovery phase: proportional mean-reversion after crisis end
- Wealth tax deducted monthly from total financial wealth
- Property net worth tracked separately and compounded at configured growth rate

**Bucket rules:**
- In crisis + drawdown > 15%: withdrawals pause from ETF, Cash Buffer absorbs all expenses
- In crisis + drawdown ≤ 15%: Cash Buffer used first, ETF only as overflow
- War Chest never used for living expenses — only deployed at specific drawdown thresholds
- SWR surplus flows: Buffer → War Chest → ETF (new in v6.1)
- ATH + 5% growth rebalancing refills both cash buckets from ETF surplus (updated in v6.1)

**War Chest deployment thresholds:**

| Asset type | Weight | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|
| Standard ETF | 80% | −18% | −26% | −33% |
| High-Beta | 20% | −25% | −40% | −50% |

Each tier fires once per crisis and allocates a fixed fraction of remaining War Chest to the ETF depot.

**B&H parallel simulation:**
- Same starting capital (invested + buffer + war chest combined)
- Same monthly withdrawals (inflation-adjusted)
- Same crisis return profile
- No buffers, no drawdown stops — direct comparison benchmark

### Crisis Engine

**Historical mode (← 5Y / 5Y →):** Navigate through real calendar windows. The simulator overlays actual crisis phases as red-shaded chart zones with labelled tags.

**Random forecast mode (↻):** Anchors the simulation start at today. Generates realistic random futures using four crisis archetypes:

| Archetype | Duration | Drop | Recovery |
|---|---|---|---|
| Banking Crisis | 16 months | −55% | 24 months |
| Oil Price Shock | 8 months | −25% | 10 months |
| Pandemic Shock | 3 months | −35% | 6 months |
| Hyperinflation | 18 months | −40% | 30 months |

Placement rules: at least one major crisis per decade, 1–3 smaller shocks per decade, non-overlapping with minimum gap padding. Each click generates a different random future.

### Historical Crisis Database (1973–2025)

| Crisis | Year | Drop | Recovery | Type |
|---|---|---|---|---|
| Oil Crisis / Stagflation | 1973 | −48% | 18 mo | Monetary |
| Volcker Recession | 1980 | −27% | 12 mo | Monetary |
| Black Monday | 1987 | −34% | 20 mo | Liquidity |
| Gulf War Recession | 1990 | −20% | 8 mo | Event-Driven |
| Asian / LTCM Crisis | 1997 | −19% | 6 mo | Liquidity |
| Dotcom Crash | 2000 | −49% | 24 mo | Structural |
| Global Financial Crisis | 2007 | −57% | 24 mo | Structural |
| EU Debt Crisis | 2011 | −19% | 8 mo | Structural |
| China / Oil Shock | 2015 | −14% | 6 mo | Event-Driven |
| COVID-19 Crash | 2020 | −34% | 5 mo | Event-Driven |
| 2022 Bear Market | 2022 | −25% | 12 mo | Monetary |
| Regional Banking Crisis | 2023 | −9% | 3 mo | Liquidity |
| Yen Carry Trade Unwind | 2024 | −10% | 1 mo | Liquidity |
| Trump Tariff Crisis | 2025 | −18% | 8 mo | Event-Driven |

### Tax & Housing Engine

**Taxes (all approximate — for simulation purposes):**
- **Income tax:** applied to pension income + imputed rental value (if ownership + CHF currency)
- **Capital gains tax:** applied to ETF withdrawal × estimated gains ratio (scales with return rate)
- **Wealth tax:** annual rate applied to total financial wealth, deducted monthly
- **Eigenmietwert (CH only):** added to taxable income when currency = CHF and ownership mode is active
- **Tax deductions (ownership):** mortgage interest + maintenance deducted from taxable income

**Housing modes:**
- 🏠 Rent: cold rent + utilities as monthly housing cost
- 🏡 Ownership: mortgage interest + maintenance as monthly cost; property net worth tracked and compounded separately; optional Eigenmietwert (CH)

**Net budget breakdown:**
Gross Budget → minus Taxes → minus Housing Costs → minus Living Costs → **Net Available**

### Solver & Mathematics

- **Newton-Raphson withdrawal solver** iterates to find the maximum monthly withdrawal that leaves the configured target legacy at the end of the period, given expected return, inflation, war chest, and buffer size
- **SWR cap:** if the solver's result exceeds the Max SWR slider, the withdrawal is capped and the surplus is routed into the bucket structure
- **Inflation adjustment:** all withdrawals increase monthly by `(1 + inflation/1200)^month`
- **Dynamic safety net:** when depot falls below 40% of initial value, withdrawals scale down proportionally to preserve longevity
- **Purchasing Power KPI:** nominal monthly budget discounted by `(1 + inflation/100)^years` — shows real value at end of period
- **Stress resistance:** buffer-only coverage months at current monthly need, assuming −50% scenario where War Chest is fully deployed into ETF

### UI & Accessibility

- **21 languages:** EN · DE · FR · ES · IT · PT · NL · PL · RU · TR · SV · DA · NO · FI · CS · HU · RO · EL · UK · HI · ZH
- **20 currencies** with smart browser locale detection and scaled input ranges per currency group
- **Dark / Light mode** — both themes fully print-friendly
- **Mobile optimised** — all sliders, panels, dropdowns, and export modal designed for touch interaction
- **100% offline** — single HTML file, CDN-loaded Chart.js and Google Fonts are the only external dependencies (both cacheable for full offline use)

---

## EN — Getting Started

### Option 1: Open directly
Download `index.html` and open in any modern browser. No installation, no build step.

### Option 2: GitHub Pages
1. Fork or upload `index.html` to a repository
2. Settings → Pages → Deploy from `main` / root
3. Available at `https://your-username.github.io/repo-name/`

### Option 3: Local dev server
```bash
python3 -m http.server 8080
# Open http://localhost:8080/
```

### Option 4: Any static host
Netlify Drop, Vercel, Cloudflare Pages, AWS S3 — drop the single file, instantly live.

---

## EN — Parameter Defaults & Ranges

| Parameter | Default | Range |
|---|---:|---:|
| Starting Capital | 1'200'000 | Currency-dependent (CHF: 100k – 10M) |
| Withdrawal Duration | 30 years | 10 – 50 |
| Target Legacy | 0 | 0 – 5'000'000 |
| Inflation | 1.5% | 0 – 10% |
| Expected Return (ETF) | 6.0% | 1 – 20% |
| Pension / AHV (monthly) | 1'800 | 0 – 10'000 |
| War Chest | 10% | 0 – 40% |
| Cash Buffer | 2 years | 0 – 6 |
| Max SWR | 4.0% | 2 – 7% |
| Income Tax | 20% | 0 – 50% |
| Capital Gains Tax | 0% | 0 – 35% |
| Wealth Tax | 0.20% p.a. | 0 – 2% |
| Cash Bucket Rate | **1.5% p.a.** | fixed |

---

## EN — Architecture

```
index.html  (~2,400 lines, single file)
│
├── HTML
│   ├── Header (title · allocation bar · language / currency / theme pickers)
│   ├── KPI row (Monthly Budget · Cash Buffer · War Chest · Purchasing Power)
│   ├── Left column (Base Parameters · Market & Strategy · Safety Limits)
│   ├── Mid column (Housing · Taxes · Net Budget Breakdown)
│   ├── Main column (Strategy Health · Chart · Withdrawal Analysis · Export button)
│   └── Export Modal (overlay · CSV option · JSON option · HTML Report option)
│
├── CSS
│   ├── Dark / Light theme via CSS custom properties (:root / :root.light-mode)
│   ├── Responsive grid: 1-col mobile → 2-col tablet → 3-col desktop
│   ├── Glass-panel aesthetic (backdrop-filter, subtle borders)
│   └── Export modal + button styles
│
└── JavaScript
    ├── i18n engine (21 languages, dynamic key resolution, fallback to EN)
    ├── Currency engine (20 currencies, scaled ranges, browser locale detection)
    ├── Housing + Tax engine (Eigenmietwert CH-only flag)
    ├── Crisis database (14 events, 1973–2025)
    ├── Crisis engine
    │   ├── Historical navigation (← 5Y / 5Y → with boundary clamping)
    │   └── Random forecast generator (today-anchored, typed archetypes, non-overlapping placement)
    ├── Simulation engine
    │   ├── Newton-Raphson withdrawal solver (150 iterations max)
    │   ├── 3-bucket monthly simulation loop
    │   ├── Drawdown tracker + −15% withdrawal stop rule
    │   ├── Two-tier war chest deployment (std 80% + high-beta 20%)
    │   ├── SWR surplus refill waterfall (Buffer → War Chest → ETF)  ← v6.1
    │   ├── ATH + 5%-growth dual-trigger rebalancing                  ← v6.1
    │   ├── Money-market interest 1.5% p.a. on cash buckets           ← v6.1
    │   ├── Wealth tax monthly deduction
    │   ├── Property net worth tracking + compounding
    │   ├── Dynamic withdrawal reduction safety net (<40% depot)
    │   └── B&H parallel simulation (same capital, same withdrawals)
    ├── Chart engine (Chart.js, crisis zone shading, legacy target line, B&H line)
    ├── Export engine                                                  ← v6.2
    │   ├── buildMonthlyRows()  — shared data preparation
    │   ├── exportCSV()         — semicolon-separated, UTF-8 BOM, param comment header
    │   ├── exportJSON()        — structured: meta / params / kpis / crises / monthly
    │   └── exportHTMLReport()  — standalone printable report with KPI cards + tables
    └── Theme engine (dark/light CSS class toggle, chart colour re-render)
```

---

## EN — Changelog

### v6.2 — Export Engine
- **[NEW]** Export button in Withdrawal Analysis panel header
- **[NEW]** Export modal with three format options and info line
- **[NEW]** CSV export: 13 columns per month, parameter block as comment header, semicolon + BOM for Excel compatibility
- **[NEW]** JSON export: fully structured `meta / parameters / kpiSummary / crisisEvents[] / monthlyData[]`
- **[NEW]** HTML Report: standalone printable report with KPI cards, crisis table, yearly milestones table

### v6.1 — Mathematical & Functional Optimization
- **[FIX]** Purchasing Power KPI label corrected to "real (at end)" with duration-aware sublabel
- **[NEW]** Smart Surplus Refill: SWR-cap surplus actively routed Buffer → War Chest → ETF each month
- **[UPDATED]** Cash bucket interest: 2.0% → 1.5% p.a. (money-market ETF realistic rate)
- **[NEW]** SWR info panel: surplus amount, routing destination, legacy impact, cash interest note
- **[UPDATED]** ATH Rebalancing: dual-trigger added (strict ATH + 5% 12-month growth) for faster post-crisis buffer regeneration

### v6.0 — Bucket Strategy & UX Overhaul
- **[NEW]** Dynamic ATH Rebalancing with event counter
- **[NEW]** Opportunity Cost Indicator (B&H parallel simulation + delta + contextual annotation)
- **[NEW]** Light / Dark mode toggle (translated in all 21 languages)
- **[NEW]** Trump Tariff Crisis (2025), Yen Carry Trade Unwind (2024), Regional Banking Crisis (2023) added to database

### v5.x and earlier
- 21-language i18n system, 20-currency system with locale detection
- Newton-Raphson withdrawal solver
- Historical crisis database (1973–2022)
- Two-tier war chest deployment system
- Tax engine: income, capital gains, wealth tax, Eigenmietwert
- Housing module: rent vs. ownership with full mortgage modelling
- Offline-first single-file architecture

---

## EN — License

MIT — free to use, modify, and distribute. See `LICENSE` for full terms.

---

## EN — Disclaimer

This is a simulation tool for **educational purposes only**. It does not constitute financial, tax, or investment advice. Past performance does not predict future results. Tax calculations are approximations — consult a qualified tax advisor. Always seek professional financial advice before making retirement decisions. The author assumes no liability for decisions made based on this tool.

---
---

# DE — Überblick

**Capital Pilot** ist ein Entnahme-Simulator in einer einzigen HTML-Datei, vollständig offline-fähig und mobil-optimiert. Die zentrale Frage:

> **Wie viel kann ich pro Monat ausgeben — und überlebt meine Strategie Jahrzehnte voller Marktkrisen?**

Das Tool modelliert ein **3-Töpfe-Setup** (ETF-Depot + Cash-Puffer + Kriegskasse), **Steuern**, **Wohnen** (Miete vs. Eigentum mit Hypothek) und eine **Krisen-Engine** mit echter Marktgeschichte oder zufällig generierten Zukunftsszenarien. Alle Berechnungen laufen lokal im Browser — kein Server, kein Account, kein Daten-Upload.

---

## DE — Neu in v6.2

### 📤 Simulations-Daten Export — CSV · JSON · HTML-Report

Ein neuer **Export-Button** (↓ Icon) erscheint im Panel „Auszahlungs-Analyse". Ein Klick öffnet ein Modal mit drei Exportformaten — alles lokal generiert, keine Daten verlassen dein Gerät.

**CSV — Monatliches Detail** (für Excel / LibreOffice / Numbers)
Jede Zeile = 1 Simulationsmonat. 13 Spalten: Jahr, Monat, ETF-Depot, Cash-Puffer, Kriegskasse, Immobilie Netto, Gesamtvermögen, Buy & Hold, Strategie vs. B&H Delta, Drawdown %, ETF Monatsrendite %, Zinsen Cash-Töpfe, Krisen-Flag. Parameterblock als Kommentarkopf, Semikolon-Separator + UTF-8 BOM → direkt in europäischem Excel öffnen.

**JSON — Vollständige Daten** (für Python, Power Query, eigene Dashboards)
Strukturiert mit `meta`, `parameters`, `kpiSummary`, `crisisEvents[]` und `monthlyData[]`. Ideal für `pandas.read_json()`, Power BI oder individuelle Auswertungen.

**HTML-Report — Drucken / Archivieren**
Eigenständige Seite ohne Internetbedarf. Enthält: Parameterübersicht, 8 KPI-Kacheln, Krisentabelle mit Drawdown und Erholungszeit, Jahres-Meilenstein-Tabelle mit ETF, Töpfe, Gesamtvermögen, B&H-Vergleich, Drawdown-% und Krisen-Flag. Druckoptimiertes CSS — als PDF speichern direkt über den Browser-Druckdialog.

---

## DE — Neu in v6.1

**Kaufkraft-Korrektur:** Das KPI-Label lautet jetzt korrekt „real (am Ende)" mit dynamischem Sublabel, z.B. „reale Kaufkraft nach 30 Jahren".

**Smart Surplus Refill:** Der monatliche SWR-Surplus fließt aktiv nach Priorität: Cash-Puffer → Kriegskasse → ETF-Depot. Jede Befüllung inkrementiert den Rebalancing-Zähler. Der aktuelle Betrag und Ziel-Topf werden live im SWR-Panel angezeigt.

**Geldmarkt-Verzinsung:** Beide Cash-Töpfe werden mit **1,5% p.a.** verzinst (realistischer Geldmarkt-ETF, z.B. iShares). Vorher 2,0% p.a.

**Erweitertes SWR-Panel:** Zeigt Surplus-Betrag, Ziel-Topf, Legacy-Auswirkung und dauerhafter Hinweis auf 1,5%-Verzinsung.

**Gelockerte Rebalancing-Logik — Dual-Trigger:** Rebalancing feuert jetzt bei zwei unabhängigen Bedingungen: (1) striktes neues Allzeithoch, oder (2) Depot +5% vs. Vorjahr bei unterfüllten Töpfen. Puffer füllen sich nach Krisen deutlich schneller auf.

---

## DE — Neu in v6.0

**Dynamisches ATH-Rebalancing:** Bei neuem Allzeithoch werden bis zu 1,5% des Überschusses automatisch in Cash-Puffer (65%) und Kriegskasse (35%) umgeschichtet. Verhindert, dass Schutzpuffer in langen Bullenmärkten auf kritische Niveaus schrumpfen.

**Opportunitätskosten-Indikator:** Parallele Buy-&-Hold-Simulation mit identischem Startkapital. Zeigt B&H-Endvermögen, Strategie-Endvermögen und exakten Delta mit kontextueller Erläuterung.

**Hell/Dunkel-Modus:** Umschalter oben rechts, in allen 21 Sprachen übersetzt.

**Krisen-Datenbank erweitert:** Trump Tariff Crisis (2025), Yen Carry Trade Unwind (2024) und Regional Banking Crisis (2023) hinzugefügt.

---

## DE — Warum 3 Töpfe?

| Problem | 3-Töpfe-Lösung |
|---|---|
| **Sequence-of-Returns-Risiko** | Cash-Puffer deckt 2–6 Jahre — kein ETF-Verkauf am Tiefpunkt |
| **Crash-Chance nutzen** | Kriegskasse kauft bei −18% / −26% / −33% nach — Krisen werden zur Chance |
| **Verhaltensfinanzierung** | 2+ Jahre Cash eliminiert Panikverkäufe — der größte Renditekiller langfristig |
| **Perpetuelle Bereitschaft** | Dual-Trigger-Rebalancing + SWR-Surplus hält alle Töpfe dauerhaft gefüllt |

---

## DE — Schnellstart

```bash
# Option 1: Direkt öffnen
# index.html im Browser öffnen — fertig. Kein Build, keine Installation.

# Option 2: Lokaler Server
python3 -m http.server 8080
# http://localhost:8080/

# Option 3: GitHub Pages
# index.html in Repository → Settings → Pages → Deploy from main
```

---

## DE — Haftungsausschluss

Dies ist ein Simulationswerkzeug ausschliesslich zu **Bildungszwecken**. Es stellt keine Finanz-, Steuer- oder Anlageberatung dar. Vergangene Wertentwicklungen sind kein Indikator für zukünftige Ergebnisse. Steuerberechnungen sind Näherungswerte — konsultiere einen qualifizierten Steuerberater. Hole immer professionelle Finanzberatung ein, bevor du Pensionierungsentscheidungen triffst. Der Autor übernimmt keine Haftung für Entscheidungen, die auf Basis dieses Tools getroffen werden.

---

## DE — Lizenz

MIT — kostenlos nutzbar, veränderbar und weiterzugeben.
