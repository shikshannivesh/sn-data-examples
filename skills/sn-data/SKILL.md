---
name: sn-data
description: SN Data by Shikshan Nivesh. US company financial statements, revenue by segment, 8-K events, insider trades (Form 4), planned insider sales (Form 144), large holders (13D and 13G), 13F fund holdings, House trades and FINRA short interest. Every figure links to the filing it came from. Use when a question needs a reported figure or filing record for a US-listed company or a 13F fund.
license: MIT (this skill). Data terms at https://shikshannivesh.com/data/licence
---

# SN Data

SN Data by Shikshan Nivesh: US company financial statements, revenue by segment, 8-K events, insider trades (Form 4), planned insider sales (Form 144), large holders (13D and 13G), 13F fund holdings, House trades and FINRA short interest. Every figure links to the filing it came from.

## Get a key

Make a free account at https://shikshannivesh.com/data/developers. A free key answers 250 calls a day on the last five fiscal years. A data plan opens the full record (fiscal years from FY2007, quarters from 2008).

Keep the key in an environment variable, `SN_KEY`. Never print it or put it in a file you share.

## Two ways in

### 1. The remote MCP server (preferred when the client supports MCP)

SN Data is a remote MCP server at `https://shikshannivesh.com/mcp`, with 14 read-only tools. Every answer carries the filing it came from.

```
URL     https://shikshannivesh.com/mcp
Header  Authorization: Bearer $SN_KEY
```

Claude Code:

```bash
claude mcp add --transport http sn-data \
  https://shikshannivesh.com/mcp \
  --header "Authorization: Bearer $SN_KEY"
```

Clients that sign in with OAuth open a page on shikshannivesh.com where the user signs in and presses Connect. Full setup: https://shikshannivesh.com/data/ai

### 2. The REST API

Base URL `https://shikshannivesh.com/api/v1`, header `Authorization: Bearer $SN_KEY`.

| Endpoint | Returns |
|---|---|
| `/companies` | Every company covered |
| `/companies/{ticker}` | One company and its latest figures |
| `/companies/{ticker}/financials` | Income statement, balance sheet, cash flow (`period=annual` or `quarterly`) |
| `/companies/{ticker}/figures` | Revenue, margins, returns, growth, per-share figures (`ids=revenue,net_income,roic`) |
| `/companies/{ticker}/segments` | Revenue by business, product and region |
| `/companies/{ticker}/events` | Every 8-K, by the event it reports |
| `/companies/{ticker}/insider-trades` | Form 4 trades |
| `/companies/{ticker}/planned-insider-sales` | Form 144 notices |
| `/companies/{ticker}/large-holders` | 13D and 13G filings |
| `/companies/{ticker}/congress-trades` | House members' trades |
| `/companies/{ticker}/short-interest` | FINRA short interest |
| `/companies/{ticker}/fund-holders` | Every 13F fund holding the company |
| `/funds`, `/funds/{fund}` | 13F funds and their holdings, with what they opened, added, trimmed and exited |

OpenAPI file: https://shikshannivesh.com/api/v1/openapi.json. Reference: https://shikshannivesh.com/data/developers

```bash
curl -s -H "Authorization: Bearer $SN_KEY" \
  "https://shikshannivesh.com/api/v1/companies/AAPL/financials?period=annual"
```

## How to answer with it

- Quote figures as returned, with the fiscal period, and link the filing each one came from.
- Credit the data as "Data by Shikshan Nivesh" with a link to the page the figure came from.
- Information only, not investment advice. Don't turn the data into a buy or sell call.

## Questions to try

- Compare Apple's revenue over its last three fiscal years with NVIDIA's and cite the 10-Ks.
- Which Apple insiders sold shares this month, and were the sales under a 10b5-1 plan?
- What did Berkshire Hathaway open and exit in its latest 13F?
- Has short interest in Tesla risen at the latest FINRA settlement? Give days to cover.
- Which House members disclosed trades in Microsoft most recently? Link each report.

## Licence

The data is free for personal research with credit ("Data by Shikshan Nivesh") and a link to the page the figure came from. Use at work, showing the data in a product, or bulk AI training needs a licence: https://shikshannivesh.com/data/licence
