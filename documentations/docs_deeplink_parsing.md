# Content
- [Introduction](#Introduction)  
- [parsing_coin_deeplink()](#parsing-coinmktcap-deeplink)  
- [parsing_gecko_deeplink()](#parsing-coingecko-deeplink)  
- [Error Log mechanism](#Error-Log-mechanism)  

# Introduction
This program uses two functions to parse deeplink pages from two webs,
`parsing_coin_deeplink()`, `parsing_gecko_deeplink()`. These two methods
are encapsulated in class called `ParsingDeepLink`. You can invoke these two
functions with

```python
folder = 'coin_500deeplink'
ParsingDeepLink(folder).parsing_coin_deeplink()
```
and
```python
folder = 'gecko_500deeplink'
ParsingDeepLink(folder).parsing_gecko_deeplink()
```
Note, these functions require argument `folder`, which is the directory saving
all deeplink html files from two websites.

# parsing coinmktcap deeplink
This function will first generate the file path by `init_file()`. The path is
assigned to `self.file_path`.

Then, it will parse each html file in the directory. The following information will
be saved to `Coin_500Deeplink_Info.csv`.

| object name | variable name in csv file |
| :-----------: | :---------: |
| currency name | name |
| currency rank | rank |
| circulating supply | circulating_supply |
| All time high | all_time_high |
| All time low | all_time_low |
| 7 days high | 7_days_high |
| 7 days low | 7_days_low |

Note, 'coinmktcap' has two structures for different currencies. Hence, this function
uses `try/except` format during the parsing process, so that the program can
automatically select the suitable parsing template.

If the page does NOT contain the required information in the above table, the
program will invoke the `Error Log` mechanism, and only save `name`
to the csv file.

The program DOES NOT fill in 'No info' or 'None' when data are missing because
this currency is not useful if the website does not have its data at this time.
The purpose of this project is to compare the difference between these two websites.
Hence, it is not meaningful to compare such currency from two websites where
one of them does not contain the required information.

Note, sometimes the website does not contain the required information because
it is updating the its data. Hence, these data are available if you download them
later, i.e., 5 minutes later.

# parsing coingecko deeplink
This function is designed as same as `parsing_coin_deeplink()`, except it only have
one parsing template.

# Error Log mechanism

![error_log](https://github.com/yhao21/ECON498_midterm/blob/master/pic/error_log.png)
As discussed above, the website may not contain the require data for particular 
currency at this time. If so, `save_to_log()` will be invoked. This function trace
back to `500deeplinks.csv`, find the name of currency that is as same as the one
with missing data. Save its `name` and `deeplinks` to `Error_Log.csv`.
