# Content
- [Introduction](#Introduction)  
- [parsing_coin_html()](#parsing-coin-html)  
- [parsing_gecko_html()](#parsing-gecko-html)


# Introduction
This module encapsulates the parsing process for html files from 
'coinmktcap' and 'coingecko' into two classes, `parsing_coin_html()`, 
`parsing_gecko_html()`.

If you want to test the code, call functions in the following ways,

`Parsing(folder).parsing_coin_html()` 

`Parsing(folder).parsing_gecko_html()`

`folder` refers to a directory saving 48hrs data. By default, 

```
folder = 'coinmktcap_html_file'
```
when you call `Parsing(folder).parsing_coin_html()`.

```
folder = 'gecko_html_file'
```
when you call `Parsing(folder).parsing_gecko_html()`.


# parsing coin html
This function helps you parsing html files from 'coinmktcap'.
First, it generates the absolute path of folder where the html files are being saved.
The path is assigned to `self.file_path`.

Then the function extracts the following information from each html file.

| object name | variable name in csv file |
| :-----------: | :---------: |
| round | repetition |
| currency rank | rank |
| currency name | name |
| currency name in URL | url_name |
| currency price | price |
| name abbreviation | abbr |
| 24 hours volume | 24hr_volume |
| marketcap volume | mktcap|
| currency deeplink | deeplink |

Note, the program will parse the `deeplink` only when `repetition` = 1. Clearly,
the `deeplink` for each currency will not change except the designer change the 
source code of this website. Hence, the program only need to parse this for once.

All information will be saved into a csv file `CoinMKT_48hrs_data.csv`. If you open
it with Excel or other productive softwares, you will get a table like this:

|repetition|rank|name|abbr|url_name|price|24hr_volume|mktcap|deeplink|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|1|Bitcoin|BTC|bitcoin|13557.24|29235458764|251205623878|https://coinmarketcap.com/currencies/bitcoin/|


# parsing gecko html
The only reason I use two functions to parse html files from two websites is
that the structures of these two webs are not the same. Hence, I make some changes
when parsing html files with bs4.

