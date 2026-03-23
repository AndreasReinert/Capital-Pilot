# ✈️ Capital Pilot — Strategic Withdrawal Simulation (v6.3)

<p align="center">
  <img src="https://img.shields.io/badge/version-6.3-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Version 6.3">
  <img src="https://img.shields.io/badge/languages-21-a78bfa?style=for-the-badge&labelColor=0f172a" alt="21 Languages">
  <img src="https://img.shields.io/badge/currencies-20-fbbf24?style=for-the-badge&labelColor=0f172a" alt="20 Currencies">
  <img src="https://img.shields.io/badge/offline-100%25-34d399?style=for-the-badge&labelColor=0f172a" alt="Offline Ready">
  <img src="https://img.shields.io/badge/live%20ETF-SPPW.DE-38bdf8?style=for-the-badge&labelColor=0f172a" alt="Live ETF">
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

New in v6.3: a fully live **Withdrawal & War Chest Barometer** powered by real SPPW.DE market data, a corrected 4-formula financial engine, a completely overhauled 21-language system, and a fully localised HTML export report.

---

## EN — What's New in v6.3

### 📡 Live Withdrawal & War Chest Barometer

A new real-time dashboard panel appears directly in the KPI area, showing you where the current market drawdown sits relative to your withdrawal and War Chest strategy — at a glance, every time you open the app.

**Data source:** SPDR MSCI World UCITS ETF (SPPW.DE, ISIN IE00BFY0GT14, TER 0.12%) — the same ETF used as the standard reference index throughout the simulation. Price data is fetched live from Yahoo Finance via two independent CORS proxy services with automatic fallback.

**What the Barometer shows:**

| Element | Description |
|---|---|
| **Drawdown %** | Current distance from 52-week high (AZH), updated every 5 minutes |
| **Kurs / Price** | Last available price (Yahoo Finance, ~15 min delayed for EU markets) |
| **AZH** | All-time / 52-week high, calculated from daily high bar history |
| **Zone label** | Safe / Caution / Cash Only — colour-coded to current drawdown zone |
| **Status dot** | Green = live · Grey = offline / fallback |

**Strategy bars (4-row visual):**

- **Withdrawal bar** (tall): shows the three withdrawal zones — Full ETF withdrawal (0% to −6%), Reduced ETF withdrawal (−6% to −13%), Cash Buffer only (below −13%) — with a live needle marking the current drawdown
- **War Chest 1, 2, 3** (slim bars): show the three deployment tiers at −18%, −26%, −33%, with the exact CHF amount per tier calculated from your current War Chest slider

**Three KPI badges** (Monthly Budget · Cash Buffer · War Chest) update automatically based on the live drawdown:

| Drawdown range | Monthly Budget | Cash Buffer | War Chest |
|---|---|---|---|
| ≥ 0% | ✅ Withdrawal OK | ✅ Refill | ✅ Refill |
| 0% to −6% | ✅ Withdrawal OK | 🟡 Standby | 🟡 Standby |
| −6% to −13% | 🟡 Reduce | 🟡 Standby | 🟡 Standby |
| < −13% | 🔴 Stopped | 🟠 Buffer active | 🟡 Near −18% |
| ≤ −18% | 🔴 Stopped | 🟠 Buffer active | 🔴 DEPLOY TIER 1! |
| ≤ −26% | 🔴 Stopped | 🟠 Buffer active | 🔴 DEPLOY TIER 2! |
| ≤ −33% | 🔴 Stopped | 🟠 Buffer active | 🔴 DEPLOY TIER 3! |

**Offline fallback:** If all proxy services are unreachable, the Barometer shows the most recent known values (SPPW.DE AZH: 42.04 EUR, reference price: 39.47 EUR) with a clear "Offline" status and a link to Deutsche Börse for manual verification.

**Auto-refresh:** Prices reload every 5 minutes while the page is open. On network failure, automatic retry after 2 minutes.

---

### 🔧 Four Financial Formula Corrections

The simulation engine received four accuracy improvements:

**K1 — Total Withdrawal statistic corrected**  
`Total Withdrawal` and `Market Gain` in the Withdrawal Analysis panel previously included pension income (AHV/Rente) — money that never comes from the portfolio. Both figures now correctly show only the ETF depot withdrawals, giving an accurate picture of how much capital was actually consumed.

**K2 — Buffer months display corrected**  
Buffer coverage was previously calculated as `buffer ÷ monthlyETF` — based only on ETF withdrawals. Since the buffer must cover the full monthly need (ETF + pension supplement), coverage is now correctly calculated as `buffer ÷ totalMonthly`. A 3-year buffer set in the slider now shows ~25 months of full coverage rather than a misleadingly high 36.

**M1 — Purchasing Power corrected for indexed pensions**  
The Purchasing Power KPI previously discounted the entire monthly budget (including pension) by inflation. Since Swiss AHV and most public pensions are indexed to inflation, only the ETF withdrawal portion is now discounted. The resulting real purchasing power figure is higher and more accurate.

**M2 — SWR cap path: buffer allocation corrected**  
When the Max SWR slider caps withdrawals below the solver optimum, the buffer and invested capital are now kept at solver-optimal levels rather than being recalculated based on the capped withdrawal amount. This prevents an artificial over-allocation to the ETF depot in capped scenarios.

---

### 🌍 Complete 21-Language Overhaul

The entire i18n system was rebuilt from scratch. All 21 languages now have:

- **188 translation keys** per language — every label, badge, tooltip, warning, and UI string
- **37 export-specific keys** — the HTML Report now renders in the user's active language, including section headings, table headers, crisis names (e.g. "KRISE" / "CRISE" / "KRYZYS"), yearly milestones, and the footer disclaimer
- **Correct browser language detection** — `navigator.language` maps to the right language on first load for all 21 locales including `de-CH`, `fr-CH`, `zh-CN`, `zh-TW`
- **Fixed merge logic bug** — a critical regression caused DE and FR translations to be overwritten by EN fallbacks; all 188 keys now load correctly for every language
- **Rebuilt language dropdown** — persistent click-outside handler (no more "frozen" dropdown after language switch), dropdown rebuilt on each open with the correct active state

Supported languages: **EN · DE · FR · ES · IT · PT · NL · PL · RU · TR · SV · DA · NO · FI · CS · HU · RO · EL · UK · HI · ZH**

---

### 📤 Fully Localised HTML Export Report

The HTML Report export (introduced in v6.2) is now fully translated into all 21 languages. When you export with German active, the report shows "Simulationsbericht", "Jaehrliche Meilensteine", "KRISE", and a German disclaimer. The same applies to all 21 languages.

Additional improvements to the HTML Report:
- Version updated from v6.2 → **v6.3** in subtitle and footer
- Simulation mode translated ("historisch" / "historique" / "historico" etc.)
- Crisis names localised via `getCrisisName()` — shows German names when in DE mode
- Numbers formatted with locale-aware `Intl.NumberFormat`
- Positive/negative delta rendered in green/amber respectively
- Print CSS improved with better typography

---

### 🕐 Improved Live Price Status

The market data status indicator now shows localised delay information in all 21 languages:

| Language | Status text example |
|---|---|
| DE | `Yahoo (~15min verzoegert)` |
| FR | `Yahoo (~15min retarde)` |
| ES | `Yahoo (~15min retrasado)` |
| PL | `Yahoo (~15min opozniony)` |
| ZH | `Yahoo (~15min yanchi)` |

**Fetch reliability fix:** A critical bug caused the Yahoo Finance fetch to silently fail on every refresh after the first successful load. The `AbortController` timeout was never cleared after a successful response, so 8 seconds later it aborted the *next* fetch call — forcing the Barometer offline. The timer is now properly cancelled on both success and failure paths.

---

## EN — What's New in v6.2

### 📤 Simulation Data Export — CSV · JSON · HTML Report

A new **Export button** (↓ icon) in the Withdrawal Analysis panel opens a modal with three export formats. Everything generated locally — no data leaves your device.

**CSV — Monthly Detail** · 13 columns per month (ETF Depot, Buffer, War Chest, Total, B&H, Drawdown %, Crisis flag, …). Semicolon separator + UTF-8 BOM for direct European Excel compatibility.

**JSON — Full Structured Data** · Sections: `meta`, `parameters`, `kpiSummary`, `crisisEvents[]`, `monthlyData[]`. Compatible with `pandas.read_json()`, Power BI, Power Query.

**HTML Report — Print / Archive** · Standalone printable report: parameter table, KPI summary, crisis events table, yearly milestones table. Use browser Print → Save as PDF.

---

## EN — What's New in v6.1

**Purchasing Power label** corrected to "real (at end)" with duration-aware sublabel.

**Smart Surplus Refill:** SWR-cap surplus routed monthly via waterfall: Buffer → War Chest → ETF.

**Money-market interest** on Cash Buffer and War Chest: 1.5% p.a. (was 2.0%).

**ATH Rebalancing dual-trigger:** fires on (1) new all-time high OR (2) depot +5% vs. 12 months ago with underfilled buckets.

---

## EN — What's New in v6.0

**Dynamic ATH Rebalancing** — 1.5% of surplus above ATH refills Buffer (65%) + War Chest (35%).

**Opportunity Cost Indicator** — parallel B&H simulation with identical capital and withdrawals.

**Light / Dark mode toggle** — fully translated in all 21 languages.

**Crisis database extended** — Trump Tariff Crisis (2025), Yen Carry Unwind (2024), Regional Banking Crisis (2023).

---

## EN — Core Strategy: Why 3 Buckets?

| Problem | 3-Bucket Solution |
|---|---|
| **Sequence-of-Returns Risk** | Cash Buffer covers 2–6 years — you never sell ETF at the bottom |
| **Crash Opportunity** | War Chest deploys at −18% / −26% / −33% — crises become buying opportunities |
| **Behavioural Finance** | 2+ years of cash eliminates panic selling — the single biggest destroyer of long-term returns |
| **Perpetual Readiness** | Dual-trigger rebalancing + SWR surplus refill keeps all buckets battle-ready at all times |

---

## EN — Full Feature Reference

### Simulation Engine

**Monthly loop mechanics:**
- ETF depot compounds with expected return ± random noise (±0.75% per month)
- Crisis return profile: sine-wave drawdown curve + random volatility during crash phases
- Recovery phase: proportional mean-reversion after crisis end
- Wealth tax deducted monthly from total financial wealth
- Property net worth tracked separately and compounded at configured growth rate

**Bucket rules (v6.3):**
- Drawdown 0% to −6%: Full ETF withdrawal, Cash Buffer on standby
- Drawdown −6% to −13%: Reduced ETF withdrawal, Cash Buffer supplements
- Drawdown below −13%: **Zero ETF sales** — Cash Buffer covers 100% of expenses
- War Chest deploys at −18% / −26% / −33% thresholds — never used for living expenses
- SWR surplus flows: Buffer → War Chest → ETF (v6.1)
- ATH + 5% growth dual-trigger rebalancing refills both cash buckets (v6.1)

**War Chest deployment thresholds:**

| Asset type | Weight | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|---|
| Standard ETF | 80% | −18% | −26% | −33% |
| High-Beta | 20% | −25% | −40% | −50% |

### Crisis Engine

**Historical mode (← 5Y / 5Y →):** Real calendar windows overlaying actual crisis phases as red-shaded chart zones with labelled tags.

**Random forecast mode (↻):** Anchors at today and generates realistic random futures using four crisis archetypes:

| Archetype | Duration | Drop | Recovery |
|---|---|---|---|
| Banking Crisis | 16 months | −55% | 24 months |
| Oil Price Shock | 8 months | −25% | 10 months |
| Pandemic Shock | 3 months | −35% | 6 months |
| Hyperinflation | 18 months | −40% | 30 months |

### Historical Crisis Database (1973–2026)

| Crisis | Year | Drop | Duration | Recovery | Type |
|---|---|---|---|---|---|
| Oil Crisis / Stagflation | 1973 | −48% | 21 mo | 18 mo | Monetary |
| Volcker Recession | 1980 | −27% | 20 mo | 12 mo | Monetary |
| Black Monday | 1987 | −34% | 3 mo | 20 mo | Liquidity |
| Gulf War Recession | 1990 | −20% | 6 mo | 8 mo | Event-Driven |
| Asian / LTCM Crisis | 1997 | −19% | 5 mo | 6 mo | Liquidity |
| Dotcom Crash | 2000 | −49% | 30 mo | 24 mo | Structural |
| Global Financial Crisis | 2007 | −57% | 17 mo | 24 mo | Structural |
| EU Debt Crisis | 2011 | −19% | 6 mo | 8 mo | Structural |
| China / Oil Shock | 2015 | −14% | 7 mo | 6 mo | Event-Driven |
| COVID-19 Crash | 2020 | −34% | 2 mo | 5 mo | Event-Driven |
| 2022 Bear Market | 2022 | −25% | 10 mo | 12 mo | Monetary |
| Regional Banking Crisis | 2023 | −9% | 2 mo | 3 mo | Liquidity |
| Yen Carry Unwind | 2024 | −10% | 1 mo | 1 mo | Liquidity |
| Trump Tariff Crisis | 2025 | −18% | 4 mo | 2 mo | Event-Driven |
| **Middle East War (Iran)** | **2026** | **−22%** | **6 mo** | **8 mo** | **Geopolitical** |

### Tax & Housing Engine

**Taxes (simulation approximations):**
- Income tax on pension income + imputed rental value (CH only)
- Capital gains tax on ETF withdrawals × estimated gain ratio (scales with return rate)
- Wealth tax: annual rate on total financial wealth, deducted monthly
- Eigenmietwert (CH only): taxed when currency = CHF and ownership mode active
- Mortgage interest + maintenance deductible in ownership mode

**Housing modes:**
- 🏠 **Rent:** cold rent + utilities as monthly housing cost
- 🏡 **Ownership:** mortgage interest + maintenance; property tracked and compounded separately

### Solver & Mathematics

- **Newton-Raphson withdrawal solver** (150 iterations): finds maximum monthly withdrawal leaving configured target legacy at period end
- **SWR cap:** solver result capped at Max SWR slider; surplus routed via waterfall
- **Inflation adjustment:** `(1 + inflation/1200)^month` applied to withdrawals each step
- **Purchasing Power KPI (v6.3 corrected):** only ETF withdrawal discounted by inflation; pension remains real-value (indexed)
- **Total Withdrawal statistic (v6.3 corrected):** shows only ETF depot withdrawals, excluding pension income

### UI & Accessibility

- **21 languages** with browser locale auto-detection (`navigator.language`)
- **20 currencies** with locale-scaled input ranges
- **Dark / Light mode** — both print-friendly
- **Mobile optimised** — touch-friendly sliders, dropdowns, and modal
- **100% offline** — single HTML file; Chart.js and Google Fonts are the only external dependencies (both cacheable)

---

## EN — Getting Started

### Option 1: Open directly
Download `index.html` and open in any modern browser. No installation, no build step.

### Option 2: GitHub Pages
1. Upload `index.html` to a repository
2. Settings → Pages → Deploy from `main`
3. Live at `https://your-username.github.io/repo-name/`

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
| Starting Capital | 1'200'000 | Currency-dependent |
| Withdrawal Duration | 30 years | 10 – 50 |
| Target Legacy | 0 | 0 – 5'000'000 |
| Inflation | 1.5% | 0 – 10% |
| Expected Return (ETF) | 6.0% | 1 – 20% |
| Pension / AHV (monthly) | 1'800 | 0 – 30'000 |
| War Chest | 10% | 0 – 40% |
| Cash Buffer | 2 years | 0 – 6 |
| Max SWR | 4.0% | 2 – 7% |
| Income Tax | 20% | 0 – 50% |
| Capital Gains Tax | 0% | 0 – 35% |
| Wealth Tax | 0.20% p.a. | 0 – 2% |
| Cash Bucket Rate | 1.5% p.a. | fixed |

---

## EN — Architecture

```
index.html  (~6,000 lines, single file, 268 KB)
│
├── HTML
│   ├── Header (title · allocation bar · language / currency / theme pickers)
│   ├── Withdrawal & War Chest Barometer (live ETF · drawdown · strategy bars · badges)  ← v6.3
│   ├── KPI row (Monthly Budget · Cash Buffer · War Chest · Purchasing Power)
│   ├── Left column (Base Parameters · Market & Strategy · Safety Limits)
│   ├── Mid column (Housing · Taxes · Net Budget Breakdown)
│   ├── Main column (Strategy Health · Chart · Withdrawal Analysis · Export button)
│   └── Export Modal (CSV · JSON · HTML Report)
│
├── CSS
│   ├── Dark / Light theme via CSS custom properties (:root / :root.light-mode)
│   ├── Responsive grid: 1-col mobile → 2-col tablet → 3-col desktop
│   ├── Barometer: dd-strip, dd-compact-readout, smb-wrap, smb-row, smb-track  ← v6.3
│   └── Glass-panel aesthetic (backdrop-filter, subtle borders)
│
└── JavaScript (~218 KB)
    ├── i18n engine (21 languages · 188 keys · browser locale detection · EN fallback)  ← v6.3
    ├── Currency engine (20 currencies · locale-scaled ranges · browser detection)
    ├── Market data engine  ← v6.3
    │   ├── fetchMarketData() — Yahoo Finance v8 API via CORS proxies
    │   ├── AZH from 52-week daily high bars
    │   ├── Auto-refresh every 5 min · retry on fail every 2 min
    │   └── AbortController with proper cleanup (no refresh-abort race condition)
    ├── Barometer engine  ← v6.3
    │   ├── buildDDBar() / buildSmbTicks() / buildStrategyBars()
    │   ├── updateDDBar() / updateKpiBadges()
    │   └── 4-row visual: Withdrawal bar + War Chest Tier 1/2/3
    ├── Housing + Tax engine (Eigenmietwert CH-only flag)
    ├── Crisis database (15 events · 1973–2026)
    ├── Crisis engine
    │   ├── Historical navigation (← 5Y / 5Y → with boundary clamping)
    │   └── Random forecast (today-anchored · typed archetypes · non-overlapping)
    ├── Simulation engine
    │   ├── Newton-Raphson withdrawal solver (150 iterations max)
    │   ├── 3-bucket monthly simulation loop
    │   ├── Corrected drawdown zones: 0–6% full · 6–13% reduced · >13% buffer only  ← v6.3
    │   ├── Two-tier war chest deployment (std 80% + high-beta 20%)
    │   ├── SWR surplus refill waterfall (Buffer → War Chest → ETF)
    │   ├── ATH + 5%-growth dual-trigger rebalancing
    │   ├── Money-market interest 1.5% p.a. on cash buckets
    │   ├── Corrected purchasing power (pension excluded from inflation discount)  ← v6.3
    │   ├── Corrected total withdrawal statistic (ETF-only, excl. pension)  ← v6.3
    │   ├── Corrected buffer months (based on full monthly need)  ← v6.3
    │   ├── Corrected SWR-cap buffer allocation  ← v6.3
    │   ├── Wealth tax monthly deduction
    │   ├── Property net worth tracking + compounding
    │   ├── Dynamic withdrawal reduction safety net (<40% depot)
    │   └── B&H parallel simulation
    ├── Chart engine (Chart.js · crisis zone shading · legacy line · B&H line)
    ├── Export engine  ← v6.2 / fully localised v6.3
    │   ├── getParams() / buildRows()  — shared data preparation
    │   ├── exportCSV()       — 13 columns · semicolon · UTF-8 BOM
    │   ├── exportJSON()      — meta / params / kpis / crises / monthly
    │   └── exportHTMLReport() — fully i18n · 21 languages · v6.3 footer
    └── Theme engine (dark/light CSS class toggle · chart colour re-render)
```

---

## EN — Changelog

### v6.3 — Live Barometer, Formula Audit, Full i18n
- **[NEW]** Withdrawal & War Chest Barometer with live SPPW.DE price data
- **[NEW]** 4-row strategy bar: Withdrawal zones + 3 War Chest tiers with live amounts
- **[NEW]** 3 KPI badges with real-time drawdown-driven status (21 states, 21 languages)
- **[NEW]** SPPW.DE (ISIN IE00BFY0GT14, TER 0.12%) as reference ETF — Deutsche Börse Xetra
- **[NEW]** AZH calculated from 52-week daily high bars (more accurate than meta.fiftyTwoWeekHigh)
- **[NEW]** Auto-refresh every 5 min · retry every 2 min on failure · offline fallback with DB link
- **[FIX]** AbortController timer race condition — timer now cleared on success and failure
- **[FIX]** Total Withdrawal / Market Gain: AHV/pension excluded (ETF-only)
- **[FIX]** Buffer months: based on full monthly need (ETF + pension), not ETF-only
- **[FIX]** Purchasing Power: pension excluded from inflation discount (indexed)
- **[FIX]** SWR-cap path: buffer/invested kept at solver-optimal levels
- **[FIX]** i18n merge loop: DE and FR translations no longer overwritten by EN fallbacks
- **[NEW]** 188 translation keys per language · 37 export-specific keys · all 21 languages
- **[NEW]** HTML Report fully localised in all 21 languages (headings, tables, crisis names, footer)
- **[NEW]** `delayedLabel` key — live price status text localised in all 21 languages
- **[FIX]** Language dropdown: persistent click-outside handler (no frozen dropdown after switch)
- **[NEW]** Browser language auto-detection for all 21 locales including de-CH, fr-CH, zh-CN
- **[NEW]** Middle East War (Iran) 2026/02 added to crisis database
- **[UPDATED]** Crisis recovery overlap validation — all 15 crises clean, no chain-blocking

### v6.2 — Export Engine
- **[NEW]** Export button, export modal with three format options
- **[NEW]** CSV: 13 columns/month · semicolon + BOM · param comment header
- **[NEW]** JSON: meta / parameters / kpiSummary / crisisEvents[] / monthlyData[]
- **[NEW]** HTML Report: standalone printable · KPI cards · crisis table · yearly milestones

### v6.1 — Mathematical & Functional Optimisation
- **[FIX]** Purchasing Power label "real (at end)" with duration-aware sublabel
- **[NEW]** Smart Surplus Refill: SWR-cap surplus → Buffer → War Chest → ETF
- **[UPDATED]** Cash bucket interest: 2.0% → 1.5% p.a.
- **[UPDATED]** ATH Rebalancing: dual-trigger (strict ATH + 5% 12-month growth)

### v6.0 — Bucket Strategy & UX Overhaul
- **[NEW]** Dynamic ATH Rebalancing with event counter
- **[NEW]** Opportunity Cost Indicator (B&H parallel simulation + delta)
- **[NEW]** Light / Dark mode toggle (21 languages)
- **[NEW]** Trump Tariff Crisis (2025), Yen Carry Unwind (2024), Regional Banking Crisis (2023)

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

Neu in v6.3: ein vollständig live betriebenes **Entnahme- & Kriegskassen-Barometer** mit echten Marktdaten von SPPW.DE, ein korrigierter 4-Formeln-Rechenmotor, ein komplett überarbeitetes 21-Sprachen-System sowie ein vollständig übersetzter HTML-Export-Report.

---

## DE — Neu in v6.3

### 📡 Live Entnahme- & Kriegskassen-Barometer

Ein neues Echtzeit-Dashboard-Panel erscheint direkt im KPI-Bereich und zeigt auf einen Blick, wo der aktuelle Markt-Drawdown im Verhältnis zur Entnahme- und Kriegskassenstrategie steht.

**Datenquelle:** SPDR MSCI World UCITS ETF (SPPW.DE, ISIN IE00BFY0GT14, TER 0.12%) — derselbe ETF, der als Standardreferenzindex in der gesamten Simulation verwendet wird. Preisdaten werden live von Yahoo Finance über zwei unabhängige CORS-Proxy-Dienste mit automatischem Fallback abgerufen.

**Was der Barometer anzeigt:**

| Element | Beschreibung |
|---|---|
| **Drawdown %** | Aktueller Abstand vom 52-Wochen-Hoch (AZH), alle 5 Minuten aktualisiert |
| **Kurs** | Letzter verfügbarer Preis (Yahoo Finance, ~15 min verzögert für EU-Märkte) |
| **AZH** | Allzeithoch / 52-Wochen-Hoch, berechnet aus täglichen Höchstkurs-Bars |
| **Zonen-Label** | Sicher / Vorsicht / Nur Puffer — farblich nach Drawdown-Zone |
| **Status-Punkt** | Grün = live · Grau = offline / Fallback |

**Strategie-Balken (4-zeilig):**

- **Entnahme-Balken** (hoch): zeigt die drei Entnahme-Zonen — Volle ETF-Entnahme (0% bis −6%), Reduzierte Entnahme (−6% bis −13%), Nur Cash-Puffer (unter −13%) — mit einer Live-Nadel am aktuellen Drawdown
- **Kriegskasse 1, 2, 3** (schmal): zeigen die drei Einsatz-Schwellen bei −18%, −26%, −33% mit dem exakten CHF-Betrag pro Stufe, berechnet aus dem aktuellen Kriegskassen-Regler

**Drei KPI-Badges** (Monatsbudget · Cash-Puffer · Kriegskasse) aktualisieren sich automatisch basierend auf dem Live-Drawdown:

| Drawdown-Bereich | Monatsbudget | Cash-Puffer | Kriegskasse |
|---|---|---|---|
| ≥ 0% | ✅ Entnahme OK | ✅ Auffüllen | ✅ Auffüllen |
| 0% bis −6% | ✅ Entnahme OK | 🟡 Bereitschaft | 🟡 Bereitschaft |
| −6% bis −13% | 🟡 Reduzieren | 🟡 Bereitschaft | 🟡 Bereitschaft |
| < −13% | 🔴 Gestoppt | 🟠 Puffer aktiv | 🟡 Nahe −18% |
| ≤ −18% | 🔴 Gestoppt | 🟠 Puffer aktiv | 🔴 STUFE 1 EINSETZEN! |
| ≤ −26% | 🔴 Gestoppt | 🟠 Puffer aktiv | 🔴 STUFE 2 EINSETZEN! |
| ≤ −33% | 🔴 Gestoppt | 🟠 Puffer aktiv | 🔴 STUFE 3 EINSETZEN! |

**Offline-Fallback:** Wenn alle Proxy-Dienste nicht erreichbar sind, zeigt der Barometer die zuletzt bekannten Werte (SPPW.DE AZH: 42,04 EUR, Referenzkurs: 39,47 EUR) mit einem klaren „Offline"-Status und einem Link zu Deutsche Börse zur manuellen Prüfung.

**Auto-Refresh:** Preise werden alle 5 Minuten neu geladen. Bei Netzwerkfehler automatischer Neuversuch nach 2 Minuten.

---

### 🔧 Vier Formel-Korrekturen im Rechenmotor

**K1 — Gesamtentnahme-Statistik korrigiert**  
„Gesamte Entnahme" und „Marktgewinn" im Analyse-Panel enthielten bislang die Rente/AHV — Geld, das nie aus dem Portfolio kommt. Beide Kennzahlen zeigen jetzt ausschliesslich die ETF-Depot-Entnahmen.

**K2 — Puffer-Monats-Anzeige korrigiert**  
Die Puffer-Abdeckung wurde bisher als `Puffer ÷ monatliche ETF-Entnahme` berechnet. Da der Puffer den vollen monatlichen Bedarf (ETF + Rente) decken muss, wird jetzt korrekt `Puffer ÷ Gesamtbedarf` verwendet. Ein 3-Jahres-Puffer zeigt nun realistisch ~25 Monate statt der irreführend hohen 36 Monate.

**M1 — Kaufkraft für indexierte Renten korrigiert**  
Das Kaufkraft-KPI diskontierte bisher das gesamte Monatsbudget (inkl. Rente) mit Inflation. Da AHV und die meisten öffentlichen Renten inflationsindexiert sind, wird jetzt nur der ETF-Entnahme-Teil diskontiert. Die angezeigte Kaufkraft ist dadurch höher und realistischer.

**M2 — SWR-Cap-Pfad: Pufferzuweisung korrigiert**  
Wenn der Max-SWR-Regler die Entnahme deckelt, werden Puffer und investiertes Kapital jetzt auf dem Solver-optimalen Niveau gehalten, statt auf Basis des gedeckelten Betrags neu berechnet zu werden.

---

### 🌍 Vollständiges 21-Sprachen-System

Das gesamte i18n-System wurde neu aufgebaut. Alle 21 Sprachen haben jetzt:

- **188 Übersetzungsschlüssel** pro Sprache — jedes Label, Badge, Tooltip, jede Warnung und jeder UI-String
- **37 Export-spezifische Schlüssel** — der HTML-Report wird in der aktiven Benutzersprache gerendert (Abschnittsüberschriften, Tabellenkopfzeilen, Krisennamen z.B. „KRISE", Jahresmeilensteine, Footer-Disclaimer)
- **Korrekte Browser-Spracherkennung** — `navigator.language` wählt beim ersten Laden die richtige Sprache für alle 21 Lokale inkl. `de-CH`, `fr-CH`, `zh-CN`
- **Merge-Logik-Bug behoben** — ein kritischer Fehler liess DE und FR durch EN-Fallbacks überschreiben; alle 188 Schlüssel laden jetzt korrekt für jede Sprache
- **Sprach-Dropdown neu aufgebaut** — persistenter Klick-aussen-Handler (kein „eingefrorenes" Dropdown nach Sprachwechsel), Dropdown wird bei jedem Öffnen mit korrektem aktivem Status neu aufgebaut

Unterstützte Sprachen: **EN · DE · FR · ES · IT · PT · NL · PL · RU · TR · SV · DA · NO · FI · CS · HU · RO · EL · UK · HI · ZH**

---

### 📤 Vollständig lokalisierter HTML-Export-Report

Der HTML-Report-Export (eingeführt in v6.2) ist jetzt in alle 21 Sprachen übersetzt. Bei aktiver DE-Einstellung zeigt der Report „Simulationsbericht", „Jaehrliche Meilensteine", „KRISE" sowie einen deutschen Disclaimer-Text. Ebenso für alle weiteren 21 Sprachen.

Weitere Verbesserungen am HTML-Report:
- Version von v6.2 → **v6.3** in Untertitel und Footer aktualisiert
- Simulationsmodus übersetzt („historisch" / „historique" / „historico" etc.)
- Krisennamen lokalisiert via `getCrisisName()` — zeigt deutsche Namen bei DE-Modus
- Zahlen mit lokalem `Intl.NumberFormat` formatiert
- Positives/negatives Delta in Grün/Amber dargestellt

---

### 🕐 Verbesserter Live-Kurs-Status

Der Marktdaten-Status-Indikator zeigt jetzt lokalisierte Verzögerungsinformationen in allen 21 Sprachen:

| Sprache | Status-Text-Beispiel |
|---|---|
| DE | `Yahoo (~15min verzoegert)` |
| FR | `Yahoo (~15min retarde)` |
| ES | `Yahoo (~15min retrasado)` |
| PL | `Yahoo (~15min opozniony)` |
| ZH | `Yahoo (~15min yanchi)` |

**Fetch-Zuverlässigkeits-Fix:** Ein kritischer Bug liess den Yahoo-Finance-Fetch nach dem ersten erfolgreichen Laden bei jedem folgenden Refresh stumm fehlschlagen. Der `AbortController`-Timer wurde nach einer erfolgreichen Antwort nie beendet, sodass er 8 Sekunden später den *nächsten* Fetch abbrach — was den Barometer offline zwang. Der Timer wird jetzt korrekt bei Erfolg und Fehler abgebrochen.

---

## DE — Neu in v6.2

### 📤 Simulations-Daten Export — CSV · JSON · HTML-Report

Ein neuer **Export-Button** (↓ Icon) im Analyse-Panel öffnet ein Modal mit drei Exportformaten — alles lokal, keine Daten verlassen das Gerät.

**CSV — Monatliches Detail** · 13 Spalten pro Monat (ETF-Depot, Puffer, Kriegskasse, Gesamt, B&H, Drawdown %, Krisen-Flag, …). Semikolon + UTF-8 BOM für direkten europäischen Excel-Öffner.

**JSON — Vollständige Daten** · Abschnitte: `meta`, `parameters`, `kpiSummary`, `crisisEvents[]`, `monthlyData[]`. Kompatibel mit `pandas.read_json()`, Power BI, Power Query.

**HTML-Report — Drucken / Archivieren** · Eigenständiger Druckbericht: Parametertabelle, KPI-Zusammenfassung, Krisentabelle, Jahresmeilenstein-Tabelle. Browser-Druck → Als PDF speichern.

---

## DE — Neu in v6.1

**Kaufkraft-Korrektur:** KPI-Label jetzt korrekt „real (am Ende)" mit dynamischem Sublabel, z.B. „reale Kaufkraft nach 30 Jahren".

**Smart Surplus Refill:** SWR-Surplus-Überschuss fliesst monatlich via Wasserfall: Puffer → Kriegskasse → ETF.

**Geldmarkt-Verzinsung** auf Cash-Puffer und Kriegskasse: 1,5% p.a. (war 2,0%).

**ATH-Rebalancing Dual-Trigger:** feuert bei (1) neuem Allzeithoch ODER (2) Depot +5% vs. Vorjahr bei unterfüllten Töpfen.

---

## DE — Neu in v6.0

**Dynamisches ATH-Rebalancing** — 1,5% des Überschusses über ATH befüllt Puffer (65%) + Kriegskasse (35%).

**Opportunitätskosten-Indikator** — parallele B&H-Simulation mit identischem Kapital und identischen Entnahmen.

**Hell/Dunkel-Modus** — in allen 21 Sprachen übersetzt.

**Krisen-Datenbank erweitert** — Trump Tariff Crisis (2025), Yen Carry Unwind (2024), Regional Banking Crisis (2023).

---

## DE — Warum 3 Töpfe?

| Problem | 3-Töpfe-Lösung |
|---|---|
| **Sequence-of-Returns-Risiko** | Cash-Puffer deckt 2–6 Jahre — kein ETF-Verkauf am Tiefpunkt |
| **Crash-Chance nutzen** | Kriegskasse kauft bei −18% / −26% / −33% nach — Krisen werden zur Chance |
| **Verhaltensfinanzierung** | 2+ Jahre Cash eliminiert Panikverkäufe — der grösste Renditekiller langfristig |
| **Perpetuelle Bereitschaft** | Dual-Trigger-Rebalancing + SWR-Surplus hält alle Töpfe dauerhaft gefüllt |

---

## DE — Historische Krisen-Datenbank (1973–2026)

| Krise | Jahr | Einbruch | Dauer | Erholung | Typ |
|---|---|---|---|---|---|
| Ölkrise / Stagflation | 1973 | −48% | 21 Mo. | 18 Mo. | Geldpolitisch |
| Volcker-Rezession | 1980 | −27% | 20 Mo. | 12 Mo. | Geldpolitisch |
| Schwarzer Montag | 1987 | −34% | 3 Mo. | 20 Mo. | Liquidität |
| Golfkrieg | 1990 | −20% | 6 Mo. | 8 Mo. | Ereignis |
| Asienkrise / LTCM | 1997 | −19% | 5 Mo. | 6 Mo. | Liquidität |
| Dotcom-Crash | 2000 | −49% | 30 Mo. | 24 Mo. | Strukturell |
| Finanzkrise | 2007 | −57% | 17 Mo. | 24 Mo. | Strukturell |
| Euro-Schuldenkrise | 2011 | −19% | 6 Mo. | 8 Mo. | Strukturell |
| China / Ölschock | 2015 | −14% | 7 Mo. | 6 Mo. | Ereignis |
| COVID-19-Crash | 2020 | −34% | 2 Mo. | 5 Mo. | Ereignis |
| 2022 Bärenmarkt | 2022 | −25% | 10 Mo. | 12 Mo. | Geldpolitisch |
| Bankencrash | 2023 | −9% | 2 Mo. | 3 Mo. | Liquidität |
| Yen Carry Unwind | 2024 | −10% | 1 Mo. | 1 Mo. | Liquidität |
| Handelskrieg USA | 2025 | −18% | 4 Mo. | 2 Mo. | Ereignis |
| **Nahostkrieg (Iran)** | **2026** | **−22%** | **6 Mo.** | **8 Mo.** | **Geopolitisch** |

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

# Option 4: Beliebiges Static Hosting
# Netlify Drop, Vercel, Cloudflare Pages, AWS S3 — Datei ablegen, sofort live.
```

---

## DE — Haftungsausschluss

Dies ist ein Simulationswerkzeug ausschliesslich zu **Bildungszwecken**. Es stellt keine Finanz-, Steuer- oder Anlageberatung dar. Vergangene Wertentwicklungen sind kein Indikator für zukünftige Ergebnisse. Steuerberechnungen sind Näherungswerte — konsultiere einen qualifizierten Steuerberater. Hole immer professionelle Finanzberatung ein, bevor du Pensionierungsentscheidungen triffst. Der Autor übernimmt keine Haftung für Entscheidungen, die auf Basis dieses Tools getroffen werden.

---

## DE — Lizenz

MIT — kostenlos nutzbar, veränderbar und weiterzugeben.
