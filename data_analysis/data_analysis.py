import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from analysis_module import DataClean



#['Unnamed: 0' 'repetition' 'rank' 'name' 'abbr' 'url_name' 'price' '24hr_volume' 'mktcap' 'deeplink']

coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
gecko_df = pd.read_csv('Gecko_48hrs_data.csv')

coin_bitcoin = coin_df[coin_df['name'] == 'bitcoin']
gecko_bitcoin = gecko_df[gecko_df['name'] == 'bitcoin']

# clean data for coin and gecko, dataframe()
coin_clean, gecko_clean = DataClean(coin_bitcoin, gecko_bitcoin).clean_rows()


x_axis = [i for i in range(len(coin_clean))]

coin_price = coin_clean.iloc[:, 6].values
gecko_price = gecko_clean.iloc[:, 6].values
print(gecko_clean)
print(gecko_price)


#plt.plot(x_axis, coin_price, c = 'red')
#plt.plot(x_axis, gecko_price, c = 'blue')
#plt.savefig('coin_vs_gecko.png')


plt.scatter(coin_price, gecko_price)
plt.savefig('coin_gecko_scatter.png')











