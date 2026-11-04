# SN Data in your AI assistant

SN Data is a remote MCP server at `https://shikshannivesh.com/mcp`. It gives Claude, ChatGPT, Gemini, Claude Code, Codex and any other MCP client 14 read-only tools over US company financial statements, revenue by segment, 8-K events, Form 4 insider trades, Form 144 planned sales, 13D and 13G large holders, 13F fund holdings, House trades and FINRA short interest. Every answer carries the filing it came from.

Full setup with screenshots: https://shikshannivesh.com/data/ai

## Claude (web and desktop)

SN Data is listed in Claude's connector directory: https://claude.ai/directory/sn-data

1. Open the listing and click Connect.
2. Sign in to Shikshan Nivesh and click Connect.
3. In a chat, turn SN Data on in the tools menu and ask about any company.

## ChatGPT (Plus and above)

1. On chatgpt.com, open Plugins, click Add, then Add custom MCP server.
2. Name it SN Data. Connection: Server URL, `https://shikshannivesh.com/mcp`. Authentication: OAuth.
3. Click Connect, sign in to Shikshan Nivesh, then Try in chat.

## Gemini (gemini.google.com)

1. Open Personal Intelligence, then Connected apps, and click Custom.
2. Paste `https://shikshannivesh.com/mcp` and click Next.
3. Sign in to Shikshan Nivesh, click Connect, and keep the name SN Data.

## Claude Code

```bash
export SN_KEY=sn_live_your_key
claude mcp add --transport http sn-data \
  https://shikshannivesh.com/mcp \
  --header "Authorization: Bearer $SN_KEY"
```

## Codex

`~/.codex/config.toml`:

```toml
[mcp_servers.sn_data]
url = "https://shikshannivesh.com/mcp"
bearer_token_env_var = "SN_KEY"
```

## Any other MCP client

```
URL     https://shikshannivesh.com/mcp
Header  Authorization: Bearer sn_live_your_key
```

Clients that sign in with OAuth open a page on shikshannivesh.com where you sign in and press Connect.

## Questions to try

- Compare Apple's revenue over its last three fiscal years with NVIDIA's and cite the 10-Ks.
- Which Apple insiders sold shares this month, and were the sales under a 10b5-1 plan?
- What did Berkshire Hathaway open and exit in its latest 13F?
- Has short interest in Tesla risen at the latest FINRA settlement? Give days to cover.
- Which House members disclosed trades in Microsoft most recently? Link each report.
