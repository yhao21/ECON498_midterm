# Content
- [Introduction](#Introduction)  
- [Installation](#Installation)  
    - [Dependency packages](#Dependency-packages)  
- [How to run the program](#How-to-run-the-program)  
- [Configuration](#Configuration)  
    - [Number of pages to scrape](#Number-of-pages-to-scrape)  
    - [Time interval](#Time-interval)  
- [Functionality](#Functionality)  
    - [Step 1 Scrapping 48hrs data](#Step-1-Scrapping-48hrs-data)  
    - [Step 2 Parsing trend data and deeplink](#Step-2-Parsing-trend-data-and-deeplink)
    - [Step 3 Scrapping deeplink for each currency](#Step-3-Scrapping-deeplink-for-each-currency)
    - [Step 4 Parsing deeplink information](#Step-4-Parsing-deeplink-information)
- [Other Documentations](#Other-Documentations)




# Introduction  

This program helps you scrapping data from 
[coinmarketcap](https://coinmarketcap.com/) and 
[coingecko](https://www.coingecko.com/en). You can obtain live-time data 
of cryptocurrencies in a particular time period. Also, the program will download
the deeplink data for each cryptocurrency.


# Installation
You may need to download this package with command

`git clone https://www.github.com/yhao21/ECON4980_midterm`

## Dependency packages
You may need to have python 3.7 or above. You also need some dependency packages,
i.e., requests, selenium, bs4, pandas, numpy, matplotlib.
Install these packages with the following command in the terminal:

`
sudo pip3 install requests selenium bs4 pandas numpy matplotlib
`

or

`
sudo python3 -m pip install requests selenium bs4 pandas numpy matplotlib
`

Before you run this command, you need to know the way to call python or pip in your
computer. For example, if you use python3 and pip3 to run python and pip in the
terminal, you should use

`sudo pip3 install <package name>`

or

`sudo python3 -m pip install <package name>`

However, if you use `python3.8` to run python in terminal, you should install 
these packages with

`sudo pip3.8 install <package name>`

or

`sudo python3.8 -m pip install <package name>`

The reason of using 'python' + version to run python in terminal is probably
because you have installed python with command `sudo altinstall`. 


# How to run the program
You may find the file `MainConsole.py` in the root directory. Run this file in
terminal. This program will automatically do all scrapping and parsing process
for you.


# Configuration
You can customize the program by changing arguments in `MainConsole.py`.


## Number of pages to scrape
You may need to change the arguments in `url_list` in `step 1`

For example, if you only need the first 100 currencies information, which is one page
, you may need to replace the line of `url_list` with
```
url_list = [(url_coin_base + str(i), url_gecko_base + str(i)) for i in range(1,2)]
```

If you need 200th to 500th currencies, you should download page 2 to page 5.
Hence, you need to change `url_list` to

```
url_list = [(url_coin_base + str(i), url_gecko_base + str(i)) for i in range(2,6)]
```


## Time interval
You can choose how many hours data to scrape. Note, time interval is with unit of
15 minutes. It means that the program sleeps for 15 mins after finish each elements
in `url_list`.
For example, if you need 30 mins data, you should revise `Scrapping().folder_setup()`
in `step 1` as the following

```
Scrapping(url_list, folder_name, 0.5).folder_setup()
```

If you need 30 hours data,

```
Scrapping(url_list, folder_name, 48).folder_setup()
```



# Functionality
### Step 1 Scrapping 48hrs data
`url_list` is a list contains several tuples where each tuple contains two URLs. One
is from coinmktcap, the other is from coingecko,

`url_list = [(coin_url, gecko_url), (coin_url, gecko_url), ...]`

Each tuple `(coin_url, gecko_url)` is one page from both websites.
All html files from 'coinmktcap' is saved in directory named `coinmktcap_html_file`.
All html files from 'coingecko' is saved in directory named `gecko_html_file`.

### Step 2 Parsing trend data and deeplink
Parse all html files from `coinmktcap_html_file` and `gecko_html_file`.
The program extracts the following information from html files,

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

Data from 'coinmktcap' will be saved into `CoinMKT_48hrs_data.csv`

Data from 'coingecko' will be saved into `Gecko_48hrs_data.csv`




### Step 3 Scrapping deeplink for each currency
Scrape deeplink for each currency from 'coinmktcap', and save all html files to
directory `coin_500deeplink`.

Scrape deeplink for each currency from 'coingecko', and save all html files to
directory `gecko_500deeplink`.


### Step 4 Parsing deeplink information
Parse html files from `coin_500deeplink` and `gecko_500deeplink` and save 
to `Coin_500Deeplink_Info.csv` and `Gecko_500Deeplink_Info.csv`.
The following information will be saved,

| object name | variable name in csv file |
| :-----------: | :---------: |
| currency name | name |
| currency rank | rank |
| circulating supply | circulating_supply |
| all time high | all_time_high |
| all time low | all_time_low |
| 7 days high | 7_days_high |
| 7 days low | 7_days_low |


# Other Documentations
[documentation for scrapping_module.py](https://github.com/yhao21/ECON498_midterm/blob/master/documentations/docs_scrapping_module.md)
[documentation for parsing_module.py](https://github.com/yhao21/ECON498_midterm/blob/master/documentations/docs_parsing_module.md)
[documentation for deeplink_parsing.py](https://github.com/yhao21/ECON498_midterm/blob/master/documentations/docs_deeplink_parsing.md)




