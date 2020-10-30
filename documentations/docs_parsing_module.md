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

Note, the program will parse the `deeplink` only when `repetition` = 2. Clearly,
the `deeplink` for each currency will not change except the designer change the 
source code of this website. Hence, the program only need to parse this for once.
Note, for any reason, if the html file in the 2nd repetition does not contain
`deeplink`, then you should manually find a repetition that all five html
files constain `deeplink`. Then, you assign this repetition to `repetition`.

If you change the repetition here, then you should also change the value of
`repetition` in `pair_deeplink()` in `scrapping_module.py`

```python
def pair_deeplink():
    df = pd.read_csv('CoinMKT_48hrs_data.csv')
    # change '2' to the repetition number you have chosen
    coin_df = df[df['repetition'] == 2].iloc[:,-1].values

    df = pd.read_csv('Gecko_48hrs_data.csv')
    # change '1' to the repetition number you have chosen
    gecko_df = df[df['repetition'] == 1].iloc[:,-1].values

    return [(coin, gecko) for coin, gecko in zip(coin_df, gecko_df)]
```

All information will be saved into a csv file `CoinMKT_48hrs_data.csv`. If you open
it with Excel or other productivity softwares, you will get a table like this:

|repetition|rank|name|abbr|url_name|price|24hr_volume|mktcap|deeplink|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|1|Bitcoin|BTC|bitcoin|13557.24|29235458764|251205623878|https://coinmarketcap.com/currencies/bitcoin/|


# parsing gecko html
The only reason I use two functions to parse html files from two websites is
that the structures of these two webs are not the same. Hence, I make some changes
when parsing html files with bs4.

