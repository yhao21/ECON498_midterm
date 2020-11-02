import pandas as pd
import numpy as np
import os, math
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
from analysis_module import DataClean, ComparableData, Statistics
from analysis_module import GraphDiff, Compare_192


def Trend_HTH():
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





def go_192():
    #=========================
    # Get comparable currencies
    #=========================
    if not os.path.exists('statistics_figures'):
        os.mkdir('statistics_figures')

    coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
    gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
    data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
    ###['coin_name', 'coin_mean', 'gecko_mean', 'mean_diff', 'coin_std', 'gecko_std',
    ###'std_diff', 'coin_range', 'gecko_range', 'range_diff']
    price_comp_stats = Compare_192(coin_df, gecko_df, data_comparable, 'price').get_statistics()
    vol_comp_stats = Compare_192(coin_df, gecko_df, data_comparable, 'vol').get_statistics()
    mktcap_comp_stats = Compare_192(coin_df, gecko_df, data_comparable, 'mktcap').get_statistics()
    print(mktcap_comp_stats)

    price_comp_stats.to_csv('Price_Comparable_statistics.csv')
    vol_comp_stats.to_csv('Volume_Comparable_statistics.csv')
    mktcap_comp_stats.to_csv('Mktcap_Comparable_statistics.csv')

    name = price_comp_stats.iloc[:, 0].values
    # number matches the order for each currency in name (list)
    x_axis = [i for i in range(len(name))]

    ##=========================
    ## Diff in mean among price, vol, mktcap
    ##=========================
    
    ### >>> price_mean
    price_coin_mean = price_comp_stats.iloc[:, 1].values
    price_gecko_mean = price_comp_stats.iloc[:, 2].values

    plt.scatter(x_axis, price_coin_mean, c = 'blue')
    plt.scatter(x_axis, price_gecko_mean, c = 'red')
    plt.savefig('statistics_figures/Price_Mean_Comparable_statistics.png')
    plt.clf()

    ### >>> price_std
    price_coin_std = price_comp_stats.iloc[:, 4].values
    price_gecko_std = price_comp_stats.iloc[:, 5].values

    plt.scatter(x_axis, price_coin_std, c = 'blue')
    plt.scatter(x_axis, price_gecko_std, c = 'red')
    plt.savefig('statistics_figures/Price_std_Comparable_statistics.png')
    plt.clf()

    ### >>> price_range
    price_coin_range = price_comp_stats.iloc[:, 7].values
    price_gecko_range = price_comp_stats.iloc[:, 8].values

    plt.scatter(x_axis, price_coin_range, c = 'blue')
    plt.scatter(x_axis, price_gecko_range, c = 'red')
    plt.savefig('statistics_figures/Price_range_Comparable_statistics.png')
    plt.clf()

    ### >>> vol_mean
    vol_coin_mean = vol_comp_stats.iloc[:, 1].values
    vol_gecko_mean = vol_comp_stats.iloc[:, 2].values

    plt.scatter(x_axis, vol_coin_mean, c = 'blue')
    plt.scatter(x_axis, vol_gecko_mean, c = 'red')
    plt.savefig('statistics_figures/Volume_Mean_Comparable_statistics.png')
    plt.clf()

    ### >>> vol_std
    vol_coin_std = vol_comp_stats.iloc[:, 4].values
    vol_gecko_std = vol_comp_stats.iloc[:, 5].values

    plt.scatter(x_axis, vol_coin_std, c = 'blue')
    plt.scatter(x_axis, vol_gecko_std, c = 'red')
    plt.savefig('statistics_figures/Volume_std_Comparable_statistics.png')
    plt.clf()

    ### >>> vol_range
    vol_coin_range = vol_comp_stats.iloc[:, 7].values
    vol_gecko_range = vol_comp_stats.iloc[:, 8].values

    plt.scatter(x_axis, vol_coin_range, c = 'blue')
    plt.scatter(x_axis, vol_gecko_range, c = 'red')
    plt.savefig('statistics_figures/Volume_range_Comparable_statistics.png')
    plt.clf()

    ### >>> mktcap_mean
    mktcap_coin_mean = mktcap_comp_stats.iloc[:, 1].values
    mktcap_gecko_mean = mktcap_comp_stats.iloc[:, 2].values

    plt.scatter(x_axis, mktcap_coin_mean, c = 'blue')
    plt.scatter(x_axis, mktcap_gecko_mean, c = 'red')
    plt.savefig('statistics_figures/MKTcap_Mean_Comparable_statistics.png')
    plt.clf()

    ### >>> mktcap_std
    mktcap_coin_std = mktcap_comp_stats.iloc[:, 4].values
    mktcap_gecko_std = mktcap_comp_stats.iloc[:, 5].values

    plt.scatter(x_axis, mktcap_coin_std, c = 'blue')
    plt.scatter(x_axis, mktcap_gecko_std, c = 'red')
    plt.savefig('statistics_figures/MKTcap_std_Comparable_statistics.png')
    plt.clf()

    ### >>> mktcap_range
    mktcap_coin_range = mktcap_comp_stats.iloc[:, 7].values
    mktcap_gecko_range = mktcap_comp_stats.iloc[:, 8].values

    plt.scatter(x_axis, mktcap_coin_range, c = 'blue')
    plt.scatter(x_axis, mktcap_gecko_range, c = 'red')
    plt.savefig('statistics_figures/MKTcap_range_Comparable_statistics.png')
    plt.clf()
    
    
    


if __name__ == '__main__':
    go_192()




    #Trend_HTH()




