import pandas as pd
import numpy as np
import os, math
from matplotlib import pyplot as plt
from analysis_module import DataClean, ComparableData, Statistics
from analysis_module import GraphDiff


#=========================
# coinmktcap vs coingecko: 48hrs data of bitcoin, rank top 5
#=========================

#['Unnamed: 0' 'repetition' 'rank' 'name' 'abbr' 'url_name' 'price' '24hr_volume' 'mktcap' 'deeplink']

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



#=========================
# coinmktcap vs coingecko: 48hrs data of XRP, Rank top 10
#=========================


coin_bitcoin = coin_df[coin_df['abbr'] == 'XRP']
gecko_bitcoin = gecko_df[gecko_df['abbr'] == 'XRP']
print(coin_bitcoin)
print(gecko_bitcoin)

##### Price Diff
trend_name = 'XRPPrice_Trend_diff'
hth_name = 'XRPPrice_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'price')

##### Volume Diff
trend_name = 'XRPVolume_Trend_diff'
hth_name = 'XRPVolume_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'vol')

##### MartketCap Diff
trend_name = 'XRPMKTCap_Trend_diff'
hth_name = 'XRPMKTCap_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'mktcap')


#=========================
# coinmktcap vs coingecko: 48hrs data of Holo, Rank around 100
#=========================


coin_bitcoin = coin_df[coin_df['abbr'] == 'HOT']
gecko_bitcoin = gecko_df[gecko_df['abbr'] == 'HOT']

##### Price Diff
trend_name = 'HoloPrice_Trend_diff'
hth_name = 'HoloPrice_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'price')

##### Volume Diff
trend_name = 'HoloVolume_Trend_diff'
hth_name = 'HoloVolume_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'vol')

##### MartketCap Diff
trend_name = 'HoloMKTCap_Trend_diff'
hth_name = 'HoloMKTCap_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'mktcap')


#=========================
# coinmktcap vs coingecko: 48hrs data of B2BX, Rank around 300-400
#=========================


coin_bitcoin = coin_df[coin_df['abbr'] == 'B2B']
gecko_bitcoin = gecko_df[gecko_df['abbr'] == 'B2B']

##### Price Diff
trend_name = 'B2BXPrice_Trend_diff'
hth_name = 'B2BXPrice_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'price')

##### Volume Diff
trend_name = 'B2BXVolume_Trend_diff'
hth_name = 'B2BXVolume_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'vol')

##### MartketCap Diff
trend_name = 'B2BXMKTCap_Trend_diff'
hth_name = 'B2BXMKTCap_HTH_diff'
GraphDiff(coin_bitcoin, gecko_bitcoin, trend_name, hth_name, 'mktcap')





#=========================
# Get comparable currencies
#=========================
#df_coin_mktcap = pd.DataFrame()
#df_gecko_mktcap = pd.DataFrame()
#
##['Unnamed: 0' 'repetition' 'rank' 'name' 'abbr' 'url_name' 'price' '24hr_volume' 'mktcap' 'deeplink']
#data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
#print(data_comparable)
#### statistics in coinmktcap's data
### item = one currency, item_df = this currency's trend data
#for item in data_comparable:
#    coin_item_df = coin_df[coin_df['abbr'] == item]
#    gecko_item_df = gecko_df[gecko_df['abbr'] == item]
#    # only need currencies with 192 repetitions
#    if coin_item_df.shape[0] == 192:
#        price = coin_item_df.iloc[:, 6].values
#        vol = coin_item_df.iloc[:, 7].values
#        mktcap = coin_item_df.iloc[:, 8].values
#
#        ## [mean, std, max_val, min_val, data_range]
#        price_statistics = Statistics(price).trend_statistics()
#        vol_statistics = Statistics(vol).trend_statistics()
#        mktcap_statistics = Statistics(mktcap).trend_statistics()
#
#
#        df_coin_mktcap = df_coin_mktcap.append({
#            'name':item,
#            'mean':mktcap_statistics[0],
#            'std':mktcap_statistics[1],
#            'range':mktcap_statistics[2],
#            }, ignore_index = True)
#
#        price = gecko_item_df.iloc[:, 6].values
#        vol = gecko_item_df.iloc[:, 7].values
#        mktcap = gecko_item_df.iloc[:, 8].values
#
#        ## [mean, std, max_val, min_val, data_range]
#        price_statistics = Statistics(price).trend_statistics()
#        vol_statistics = Statistics(vol).trend_statistics()
#        mktcap_statistics = Statistics(mktcap).trend_statistics()
#        #print(mktcap_statistics)
#
#        df_gecko_mktcap = df_gecko_mktcap.append({
#            'name':item,
#            'mean':mktcap_statistics[0],
#            'std':mktcap_statistics[1],
#            'range':mktcap_statistics[2],
#            }, ignore_index = True)
#order = ['name', 'mean', 'std', 'range']
#df_coin_mktcap = df_coin_mktcap[order]
#df_gecko_mktcap = df_gecko_mktcap[order]
##print(df_coin_mktcap)
#    
##print(df_gecko_mktcap)
#
#
#
#coin_mktcap_mean = df_coin_mktcap.iloc[:, 1].values
#gecko_mktcap_mean = df_gecko_mktcap.iloc[:, 1].values
#diff_mean = coin_mktcap_mean - gecko_mktcap_mean
#
#
#coin_mktcap_std = df_coin_mktcap.iloc[:, 2].values
#gecko_mktcap_std = df_gecko_mktcap.iloc[:, 2].values
#diff_std = coin_mktcap_std - gecko_mktcap_std
#
#a = 0
#for i in diff_std:
#    if i > 0:
#        a += 1
#print(a)






