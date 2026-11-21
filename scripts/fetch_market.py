#!/usr/bin/env python3
"""Fetch the SPPW.DE quote from Yahoo Finance and write market.json.

Runs in the GitHub Action (.github/workflows/market-data.yml). Server-side
there is no CORS restriction, so the browser can read the result from
raw.githubusercontent.com without any proxy.

Same logic as parseYahooChart() in index.html:
  current = regularMarketPrice
  azh     = max(daily highs of the last 52 weeks, fiftyTwoWeekHigh)
"""
import json
import sys
import time
import urllib.request
from datetime import datetime, timezone

SYMBOL = "SPPW.DE"
HOSTS = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch_chart():
    last_err = None
    for attempt in range(3):
        for host in HOSTS:
            url = (f"https://{host}/v8/finance/chart/{SYMBOL}"
                   "?range=1y&interval=1d&includePrePost=false")
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
                with urllib.request.urlopen(req, timeout=20) as r:
                    return json.load(r)
            except Exception as e:  # noqa: BLE001 - try next host / retry
                last_err = e
                print(f"{host} attempt {attempt + 1}: {e}", file=sys.stderr)
        time.sleep(5 * (attempt + 1))
    raise SystemExit(f"Yahoo fetch failed: {last_err}")


def main(out_path):
    data = fetch_chart()
    result = data["chart"]["result"][0]
    meta = result["meta"]
    current = meta.get("regularMarketPrice") or meta.get("chartPreviousClose") or meta.get("previousClose")
    if not current or current <= 0:
        raise SystemExit("no price in Yahoo response")

    quote = (result.get("indicators", {}).get("quote") or [{}])[0]
    series = quote.get("high") or quote.get("close") or []
    azh = max([v for v in series if v] or [0])
    azh = max(azh, meta.get("fiftyTwoWeekHigh") or 0, current)

    snapshot = {
        "symbol": SYMBOL,
        "current": round(current, 4),
        "azh": round(azh, 4),
        "currency": meta.get("currency") or "EUR",
        "marketTime": meta.get("regularMarketTime"),
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "Yahoo Finance v8 chart (via GitHub Action)",
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=2)
    print(json.dumps(snapshot))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "market.json")
