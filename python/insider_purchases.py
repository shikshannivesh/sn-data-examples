"""Open-market insider purchases for a list of tickers since a date.

    export SN_API_KEY=sn_live_...
    python insider_purchases.py AAPL MSFT JPM --since 2026-01-01
"""
import argparse
import os
import requests

API = "https://shikshannivesh.com/api/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['SN_API_KEY']}"}

ap = argparse.ArgumentParser()
ap.add_argument("tickers", nargs="+")
ap.add_argument("--since", default="2026-01-01")
args = ap.parse_args()

for ticker in args.tickers:
    r = requests.get(f"{API}/companies/{ticker}/insider-trades",
                     headers=HEADERS, params={"from": args.since}, timeout=60)
    r.raise_for_status()
    buys = [t for t in r.json()["rows"] if "purchase" in t["kind"].lower()]
    print(f"{ticker}: {len(buys)} purchase(s) since {args.since}")
    for t in buys:
        print(f"  {t['date']}  {t['who']} ({t['role']})  {t['shares']:,} @ {t['price']}  {t['url']}")
