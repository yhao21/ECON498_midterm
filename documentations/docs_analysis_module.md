# Content
- [Introduction](#Introduction)  
- [How to use this module](#How-to-use-this-module)  
    - [DataClean()](#DataClean)  
    - [ComparableData()](#ComparableData)  
    - [Statistics()](#Statistics)  
    - [GraphDiff()](#GraphDiff)  
    - [Compare_192()](#Compare-192)  


# Introduction

This module contains all functionalities I have used for the interpretations.

It contains five main functions:

1. DataClean: Given a particular currency, extract `repetition` data appear in
both `CoinMKT_48hrs_data.csv` and `Gecko_48hrs_data.csv`.

2. ComparableData: Return a dataframe contains currencies appears in both
csv files and each `repetition`.

3. Statistics: Return a list contains three statistics for each currency,
i.e., mean, standard deviation, range (max - min).

4. GraphDiff: Graph 48hrs trend and Head-to-Head(HTH) data for a currency.

5. Compare 192: Return a comprehensive dataframe contains all `Statistics`
and differences for those `Statistics` given data from `CoinMKT_48hrs_data`
and `Gecko_48hrs_data`.

# How to use this module

### DataClean
If you have 2 dataframes, a and b, such that
```
a:
repetition  name   price
   1        aaa     100
   2        bbb     200
   5        eee     500

b:
repetition  name   price
   1        aaa     100
   2        bbb     200
   3        ccc     300
   4        ddd     400
```
`DataClean()` will extract rows with `repetition` appears in both dataframes.

Why we need this? We want to compare the differences of two websites. Hence
we need to compare the data from two websites in the same time periods. For
example, if we want to compare Bitcoin's 48hrs price information from 
two websites, then we need to match the price data one by one based on their
scrapping time. You would not like to match the 1st 15 mins data from 
coinmarketcap with the 20th 15 mins data from coingecko. That is not useful.
And we may miss some data during the scrapping process. Hence, we need to 
extract those `repetitions` appear in both csv files.

Consider dataframe `a` is from coinmarketcap, `b` is from coingecko. Due
to some reasions, we miss the 3rd and 4th repetition from coinmktcap,
and the 5th repetition from coingecko. `DataClean()` will help you extract
the 1st and 2nd `repetition` from both dataframes. Remember, only these two
repetitions are useful.

You can call this function with the following code:
```python
coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
coin_bitcoin = coin_df[coin_df['name'] == 'bitcoin']
gecko_bitcoin = gecko_df[gecko_df['name'] == 'bitcoin']
coin_clean, gecko_clean = DataClean(coin_bitcoin, gecko_bitcoin).clean_rows()
```
`coin_clean` and `gecko_clean` are cleaned dataframes with same repetitions.


### ComparableData

This method return a list of column-values appear in each `repetition` and 
appear in both csv files. Three arguments are required when you call this 
function: `df_base`, `df_compare`, `compare_column`.

`df_base` is the dataframe you want to use as benchmark.

`df_compare` is the dataframe you want to compare with `df_base`.

`compare_column` represents which column you would like to compare.

Let's use `CoinMKT_48hrs_data.csv` as an example.
```
       Unnamed: 0  repetition  rank                    name  abbr url_name      price  24hr_volume    mktcap deeplink
0               0         176   401                vertcoin   VTC      NaN   0.258529      1142379  14778035      NaN
1               1         176   402                    sora   XOR      NaN  42.470000       851839  14864521      NaN
2               2         176   403                    b2bx   B2B      NaN   0.750337        18510  14728970      NaN
3               3         176   404                stakenet   XSN      NaN   0.135342       761475  14604895      NaN
4               4         176   405            celernetwork  CELR      NaN   0.003669      2494990  14580429      NaN
...           ...         ...   ...                     ...   ...      ...        ...          ...       ...      ...
95495       95495          68   496                   rakon   RKN      NaN   0.078221      1767665   9672481      NaN
95496       95496          68   497                monolith   TKN      NaN   0.286013        32560   9670683      NaN
95497       95497          68   498  quantumresistantledger   QRL      NaN   0.132913       188312   9628597      NaN
95498       95498          68   499      moedaloyaltypoints   MDA      NaN   0.491615      1002416   9649854      NaN
95499       95499          68   500          dimensionchain   EON      NaN   0.039207        14320   9597202      NaN
```
If I want to know how many currencies appear in each `repetition`, and
appear in both csv files, I would like to check if their `abbr` satisfy
the requirements above. Why is that? It is because currency name can be
slightly different between two websites, but abbreviations are same.
Clearly, the `abbr` is the 5th column hence we should call this function with
the following code,

```python
coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
```
Note, if you do not obtain all repetition's info for a particular currency due
to technical problems, it will not show up in the list returned by
`ComparableData()`.


### Statistics

This method returns a list containing three statistical values, i.e.,
`mean`, `standard deviation`, `range` (range = max_value - min_value).

For example, if you want to get these statistics for the `price` in the
dataframe above, you can use the following code,

```python
coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
price_list = list(coin_df.iloc[:, 6].values) 
results = Statistics(price_list).trend_statistics()
```

### GraphDiff

This method return two figures for you, i.e., `48hrs trend figure`, and
`HTH figure`.
Here's an example,

![HoloVolume_HTH](https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/figures/HoloVolume_HTH_diff.png)

![HoloVolume_Trend](https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/figures/HoloVolume_Trend_diff.png)


Five arguments are required when you call this function:

1. `coin_df`: dataframe from conimktcap  
2. `gecko_df`: dataframe from coingecko  
3. `trend_pic_name`: A name for the 48hrs trend figure  
4. `HTH_pic_name`: A name for the Head-to-Head figure  
5. `item`: Column you want to graph. It can be `price`, `vol`, and `mktcap`.
You should not enter any value other than these three. Just to remind you,
`price` is for currency's price info. `vol` is for currency's 24hrs Volume.
`mktcap` is for currency's marketcap info.

If you want to graph Bithcoin's price information, use the following code.
And all figures will be save to directory, named `figures`.

```python
coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
gecko_df = pd.read_csv('Gecko_48hrs_data.csv')

coin_bitcoin = coin_df[coin_df['name'] == 'bitcoin']
gecko_bitcoin = gecko_df[gecko_df['name'] == 'bitcoin']

##### Price Diff
trend_name = 'BitcoinPrice_Trend_diff'
hth_name = 'BitcoinPrice_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'price')

##### Volume Diff
trend_name = 'BitcoinVolume_Trend_diff'
hth_name = 'BitcoinVolume_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'vol')

##### MartketCap Diff
trend_name = 'BitcoinMKTCap_Trend_diff'
hth_name = 'BitcoinMKTCap_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'mktcap')
```


### Compare 192

This method reutrns a comprehensive dataframe for comparable data. The 
dataframe contains 10 columns,
```
    Unnamed: 0 coin_name     coin_mean    gecko_mean  mean_diff      coin_std     gecko_std   std_diff  coin_range  gecko_range  range_diff
0            0       DAG  1.292786e+07  5.490097e+07   3.246718  2.720640e+05  0.000000e+00  -1.000000   1521728.0          0.0   -1.000000
1            1      LAMB  1.286296e+07  2.857963e+07   1.221854  2.974316e+05  6.767385e+05   1.275275   1602033.0    3656203.0    1.282227
2            2        ZT  1.406383e+07  2.662083e+07   0.892858  5.010009e+05  9.450627e+05   0.886349   1662978.0    3131425.0    0.883023
3            3       ENG  1.209053e+07  3.522599e+07   1.913520  4.146915e+05  5.511578e+06  12.290791   1677403.0   19477117.0   10.611471
4            4       WOM  2.153536e+07  2.150132e+07  -0.001581  7.060713e+05  7.298588e+05   0.033690   4527554.0    4975063.0    0.098841
5            5      NOIA  2.120332e+07  2.177331e+07   0.026882  8.584852e+05  1.246155e+06   0.451575   3851855.0    5058301.0    0.313212
6            6       GAS  1.386064e+07  1.904992e+07   0.374390  4.016506e+05  5.583112e+05   0.390042   1554614.0    2189565.0    0.408430
7            7      RING  1.189032e+07  1.782445e+07   0.499073  3.232128e+05  2.200912e+06   5.809483   1792774.0   20943546.0   10.682201
8            8       COS  1.284541e+07  1.816397e+07   0.414043  3.107171e+05  5.051443e+05   0.625737   1359907.0    2202328.0    0.619470
9            9       PRQ  1.214840e+07  1.150946e+07  -0.052594  2.201146e+06  2.005767e+06  -0.088762  11301017.0    8937812.0   -0.209114
10          10       FSN  1.229564e+07  1.642599e+07   0.335920  3.187144e+05  3.871448e+05   0.214708   1088554.0    1239402.0    0.138576
11          11       XCM  1.062678e+07  7.970050e+06  -0.250003  2.360809e+05  1.788269e+05  -0.242519   1065320.0    1005055.0   -0.056570
12          12       PPT  1.056987e+07  7.024682e+06  -0.335405  4.505090e+05  2.467214e+05  -0.452350   2291692.0    1223441.0   -0.466141
13          13       ZNN  1.275210e+07  1.492983e+07   0.170774  2.223580e+05  2.877579e+05   0.294120   1353742.0    1768488.0    0.306370
14          14        BZ  1.426265e+07  1.448539e+07   0.015617  1.703316e+05  1.581720e+05  -0.071388    991052.0     950905.0   -0.040509
```

Each dataframe presents three statistics from two websites and 
their difference, given data for a particular `item`. Recall `item` can be
`price`, `volume`, and `mktcap`.
Any `_diff` indicate a percentage difference between statistics from 
conmarketcap and coingecko.
```
mean_diff = (gecko_mean - coin_mean)/coin_mean
std_diff = (gecko_std - coin_std)/coin_std
```
Four arguments are required when you call this function, i.e., `coin_df`, 
`gecko_df`, `data_comparable`, `item`. Note, `data_comparable` is the list
you receive from function `ComparableData()`.
Here's an example to call `Compare_192()`,
```python
coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
price_comp_stats = Compare_192(coin_df, gecko_df, data_comparable, 'price').get_statistics()
```



