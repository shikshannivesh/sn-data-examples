# SN Data in Excel and Google Sheets

## A ready workbook

Every company page on https://shikshannivesh.com/data/companies has an Export menu. Pick Excel and you get the income statement, balance sheet, cash flow and ratios in one workbook, each period named with its filing. Google Sheets, CSV and JSON are in the same menu.

## Live data with Power Query (Excel for Windows and Mac)

This pulls Apple's annual figures straight from the API and refreshes with Data > Refresh All.

1. Data > Get Data > From Other Sources > Blank Query.
2. Home > Advanced Editor, paste the query below, put your key in the first line, click Done.
3. Close & Load.

```
let
    Key = "sn_live_your_key",
    Ticker = "AAPL",
    Source = Json.Document(Web.Contents(
        "https://shikshannivesh.com/api/v1/companies/" & Ticker & "/figures",
        [Query = [ids = "revenue,gross_profit,operating_income,net_income,fcf,eps", period = "annual"],
         Headers = [Authorization = "Bearer " & Key]])),
    Figures = Table.FromList(Source[figures], Splitter.SplitByNothing(), {"f"}),
    Expanded = Table.ExpandRecordColumn(Figures, "f", {"label", "annual"}),
    Long = Table.ExpandTableColumn(
        Table.RemoveColumns(Table.AddColumn(Expanded, "y", each Record.ToTable([annual])), {"annual"}),
        "y", {"Name", "Value"}, {"period_end", "value"}),
    Wide = Table.Pivot(Long, List.Distinct(Long[label]), "label", "value")
in
    Wide
```

Change `Ticker` for another company, or `ids` for other figures. The full list of figure ids is in the API reference: https://shikshannivesh.com/data/developers

Keep the key in the query, never in a cell other people can see.
