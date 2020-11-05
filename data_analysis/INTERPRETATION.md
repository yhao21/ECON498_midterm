# Content

- [Some Notes](#Some-Notes)  
- [Some Interpretations](#Some-Interpretations)  



# Some Notes
### About Data analysis
The data I use are not perfect. Some pages are not contained in these csv files.
I did not re-download the 48hrs data. It's a good opportunities to practice 
data cleaning with python. All my codes can work with imperfect data.

Besides, I do not make inference based on deeplink data, even though I have
parsed them. Time limitation is one of the main reason. In addition, 
I do find some differences based on the 48hrs data.

# Some Interpretations

It is obvious that top 500 currencies are quite different in two websites, 
even though both webs rank currencies by `mktcap`.

I randomly pick up 4 currencies and plot `48hrs trend graph` and `Head-to-Head (HTH) graph`.
These four currencies are in different ranking interval, i.e.,
- Bitcoin, a representative for top 5 currency.  
- XRP, a representative for top 10 currency.  
- Holo, a representative for ones ranked around 100.  
- B2BX, a representative for ones ranked around 300-400.

`48hrs trend graph` plots the trend with time period on horizontal-axis,
`item` on vertical axis. Time period is from 1 to 192, denoting the nth
15 mins. `item` can be `price`, `volume`, `mktcap`. Note, red line denotes
data from coinmarketcap. Blue line denotes data from coingecko.

`HTH graph` plots `item` with data from coinmarketcap on the horizontal
axis and data from coingecko on the vertical axis. If data from both
websites are close, the scatter plot should be closed to a straight line.

Clearly, `volume` from coinmarketcap are strictly higher than ones from
coingecko, regardless of currency ranking.
`price` info is a little bit tricky. Price info from both websites are closed
for those currencies with higher ranking (popular). It can be quite different
for currencies with lower ranking.

See figures below. You can see other figures [here](https://github.com/yhao21/ECON498_midterm/tree/master/data_analysis/figures)

<center>
<figure>
<img src="https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/figures/BitcoinPrice_Trend_diff.png" />
<img src="https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/figures/BitcoinPrice_HTH_diff.png" />
</figure>
</center>

![](https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/figures/BitcoinVolume_Trend_diff.png)
![](https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/figures/BitcoinVolume_HTH_diff.png)



Let's take a look at the mean, std, range for these `item`. I plot about 40
currencies in figures below. Currency order is on the horizontal axis,
statistics are on the vertical axis. 
Clearly, the mean of `mktcap` based on coinmarketcap's data 
for the first five currencies in my list are quite different with those
based on coingecko's data (red for coinmktcap, blue for coingecko).

Note, the difference between data from coinmktcap and coingecko are large
if the vertical distance between red and blue dots is large.
Other images can be found [here](https://github.com/yhao21/ECON498_midterm/tree/master/data_analysis/statistics_figures)
![](https://github.com/yhao21/ECON498_midterm/blob/master/data_analysis/statistics_figures/MKTcap_Mean_Comparable_statistics.png)










