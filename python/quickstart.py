"""SN Data quickstart: Apple's income statement, its latest insider trades,
and what Berkshire Hathaway opened last quarter.

    export SN_API_KEY=sn_live_...   # free key: https://shikshannivesh.com/data/developers
    python quickstart.py
"""
import os
import requests

API = "https://shikshannivesh.com/api/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['SN_API_KEY']}"}


def get(path, **params):
    r = requests.get(f"{API}/{path}", headers=HEADERS, params=params, timeout=60)
    r.raise_for_status()
    return r.json()


# 1. Revenue, net income and free cash flow, last five fiscal years
figs = get("companies/AAPL/figures", ids="revenue,net_income,fcf", period="annual")
years = [p for p in figs["periods"]["annual"]][-5:]
print("Apple, US$ billions")
print("year     " + "".join(f"{f['label']:>16}" for f in figs["figures"]))
for p in years:
    row = "".join(f"{(f['annual'].get(p['end']) or 0) / 1e9:>16.1f}" for f in figs["figures"])
    print(f"{p['label']:<9}{row}")

# 2. The five newest Form 4 trades, each with its filing
trades = get("companies/AAPL/insider-trades")
print("\nApple insider trades")
for t in trades["rows"][:5]:
    print(f"{t['date']}  {t['who']:<24} {t['kind']:<28} {t['shares']:>9,} @ {t['price']}  {t['url']}")

# 3. New positions in Berkshire Hathaway's latest 13F
fund = get("funds/1067983", move="new")
print(f"\nBerkshire Hathaway, new positions in the {fund['fund']['period']} 13F")
for h in fund["holdings"]:
    print(f"{h.get('symbol') or '':<6} {h['name']:<32} US${h['value'] / 1e6:,.1f}m")
