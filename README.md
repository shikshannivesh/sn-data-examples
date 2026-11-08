# SN Data examples

Working examples for [SN Data by Shikshan Nivesh](https://shikshannivesh.com/data): US company financial statements, revenue by segment, 8-K events, insider trades (Form 4), planned insider sales (Form 144), large holders (13D and 13G), 13F fund holdings, House trades and FINRA short interest. Every figure links to the filing it came from.

Three ways in:

| | What it is | Start here |
|---|---|---|
| Python | The REST API at `https://shikshannivesh.com/api/v1` | [python/](python/) |
| Excel and Google Sheets | Ready workbooks, or live data with Power Query | [excel/](excel/) |
| AI assistants | A remote MCP server for Claude, ChatGPT, Gemini, Claude Code, Codex | [ai-assistants/](ai-assistants/) |
| Agent skill | A SKILL.md that tells an AI agent how to use SN Data | Four skills (financial statements, insider trades, 13F holdings, 8-K events): [github.com/shikshannivesh/skills](https://github.com/shikshannivesh/skills) |

## Get a key

Make a free account at https://shikshannivesh.com/data/developers. A free key answers 250 calls a day on the last five fiscal years. A data plan opens the full record (fiscal years from FY2007, quarters from 2008).

## Python in one minute

```bash
pip install -r python/requirements.txt
export SN_API_KEY=sn_live_your_key
python python/quickstart.py
```

```
Apple, US$ billions
year              Revenue      Net income  Free cash flow
FY2021              365.8            94.7            93.0
FY2022              394.3            99.8           111.4
FY2023              383.3            97.0            99.6
FY2024              391.0            93.7           108.8
FY2025              416.2           112.0            98.8
```

The script then prints Apple's newest Form 4 trades with their SEC links, and the new positions in Berkshire Hathaway's latest 13F.

`python/insider_purchases.py AAPL MSFT JPM --since 2026-01-01` lists open-market insider purchases for any tickers.

## Endpoints

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

## Licence

The code in this repository is MIT licensed. The data is free for personal research with credit ("Data by Shikshan Nivesh") and a link to the page the figure came from. Use at work, showing the data in a product, or bulk AI training needs a licence: https://shikshannivesh.com/data/licence

Information only, not investment advice.
