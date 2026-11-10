# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Capital Pilot is a retirement withdrawal simulator built as **one self-contained file**: [index.html](index.html) (~6,000 lines of inline CSS and vanilla JS). There is no build step, no package manager, no linter and no test suite. The only external dependencies are Chart.js (jsDelivr CDN) and Google Fonts. [README.md](README.md) is the user-facing docs and changelog (EN, with a German section).

## Running

Open `index.html` directly in a browser, or serve it locally (needed for the live market fetch to behave like production):

```bash
python3 -m http.server 8080   # then open http://localhost:8080/
```

Verification is manual: load the page, change inputs, switch language/currency/theme, toggle historical/random mode, and check the console for errors.

## Layout of index.html

- Lines ~12–308: `<style>` with CSS custom properties; light mode is toggled by `toggleTheme()` / `isLightMode`.
- Lines ~309–674: static HTML markup. Inputs have ids `in-*`; translatable text uses `data-i18n="key"` and tooltips `data-i18n-tip="key"`.
- Lines ~675–5979: a single `'use strict'` script using ES5 style (`var`, `function` declarations, no modules). Keep that style.

Main script sections, in order:

1. **Global state** (`currentLang`, `currentCurrency`, `housingMode`, `simulationMode`, `timelineStartYear/Month`, `activeCrises`, `_lastSim`).
2. **Drawdown Barometer** config and rendering: `DD_ZONES` (0/−6/−13% withdrawal zones), `WC_TRIGGERS` (War Chest tiers at −18/−26/−33%), `buildDDBar`, `buildStrategyBars`, `updateKpiBadges`.
3. **Live market data**: `fetchMarketData()` pulls SPPW.DE from Yahoo Finance through the `PROXIES` CORS proxies with fallback to `ETF_FALLBACK`. Refreshes every 5 min, retries after 2 min on failure. Each fetch's `AbortController` timer must be cleared on both success and failure (a past bug caused the next fetch to be aborted).
4. **i18n**: `LANGS` holds full `en`, `de`, `fr` dictionaries; `LANGS_EXTRA` holds the other 18 languages plus `de`/`fr` additions. At load, `LANGS_EXTRA` is merged into `LANGS`, with new languages seeded from `en`. Look up strings with `T(key)` (falls back to `en`, then the key itself). `setLang()` rewrites all `data-i18n` nodes and then calls `recalc()`.
5. **Crisis data**: `HISTORICAL_CRISES` (name/nameDE, start, duration, drop, recovery) and `FUTURE_TEMPLATES` for random mode (`generateFutureCrises`). `getCrisisName()` localises names.
6. **Helpers**: `el(id)`, the `INP` map of input elements, number/currency formatting (`fmt`, `fmtK`, `fmtCapital`, `CURRENCIES`, `CUR_SCALE`).
7. **Engine**: `solveWithdrawal()` iteratively solves the sustainable withdrawal for a target legacy; `simulate()` runs the monthly loop (ETF depot, Cash Buffer, War Chest, wealth tax, property, crisis returns, ATH rebalancing, SWR-surplus waterfall Buffer → War Chest → ETF) and a parallel buy-and-hold run for the opportunity-cost figure.
8. **UI orchestration**: `recalc()` is the central entry point. Every input's `input` event calls it. It reads `INP`, computes housing and taxes, runs solve + simulate, updates KPIs, and calls `renderChart()`. The last result is stored in `_lastSim` / `_lastLegacy`, which the exporters read.
9. **Export**: `exportCSV` (semicolon-separated + UTF-8 BOM for European Excel), `exportJSON`, `exportHTMLReport` (builds a standalone, localised HTML string).
10. **Init** at the bottom: wires listeners, syncs the timeline so the simulation ends at the current month (never before 1971), runs `setCurrency(detectCurrency())`, `setLang(detectLang())`, then `fetchMarketData` after a short delay.

## Conventions

- **Translation strings are ASCII-only** (umlauts written as `ae/oe/ue`, transliterated pinyin for ZH, no emojis in JS strings). New UI text needs a key in `LANGS.en` and, ideally, all 21 languages. Missing keys silently fall back to English.
- **Bump the version everywhere**: `<title>`, the in-page version note, every language's `expFooter`, the HTML-report subtitle/footer, and the README badges and headings.
- When the strategy thresholds change (drawdown zones, War Chest tiers, interest rates, rebalancing rules), update the README tables too. They document the same numbers.
- Pension income (AHV) is not a portfolio withdrawal. Keep it out of "Total Withdrawal" and "Market Gain" statistics (the v6.3 "K1" fix).
