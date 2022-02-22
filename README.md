# EbayLegoWebscrape
## Lego webscraper for Ebay

I had a LEGO set I bought a couple years ago as an "investment".
It was a bit of an experiment, I hadn't really done any research but I knew certain sets sold for way over list on ebay after they had retired.
I held the set for 3 years, it sat in a closet and then I decided to sell it.
I sold it on ebay for almost 3 times what I paid for it. It was the Ghostbusters Firestation set.

I lost my job as a geologist recently and always wanted to learn to code, so this is a personal project I'm working on as I learn python and a little SQL.

Can I predict what sets will return the largest appreciation?
Wondered what set characteristics make for a good investment - theme? size? figurines?  
Time - is there a sweet spot in terms of ROI vs time since set retirement?

Goals:
1. Scrape Ebay data for set prices 
   1. need set metadata 
      1. date released 
      2. date retired 
      3. theme/subtheme 
      4. MSRP 
      5. no of pieces 
         1. might need to learn APIs, this data is difficult to find
2. Store data in anything except a spreadsheet!
   1. spreadsheets **are not** for data storage
   2. I repeat, spreadsheets are not for data storage
   3. will need to learn some basic SQL
3. Analyze data (Power BI, jupyter?)
   1. Power BI should be easy, star schema?
   2. Jupyter would be fun to try out some basic data science
      1. I can already see some outlier detection would be handy on sale price data
