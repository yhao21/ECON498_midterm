import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os





class DataClean():

    def __init__(self, coin_df, gecko_df, mark = 'repetition'):
        self.coin_rep = None
        self.gecko_rep = None
        self.coin_df = coin_df
        self.gecko_df = gecko_df
        self.mark = mark
        self.delete_rows = []



    def get_repetition(self):
        '''
        This function sort df based on self.mark, i.e., repetition by default
        If you need to sort by other item, assign str to mark.
        '''

        self.coin_df = self.coin_df.sort_values(self.mark).reset_index(drop = True)
        self.gecko_df = self.gecko_df.sort_values(self.mark).reset_index(drop = True)

        # rep = [1,2,3,4,....192]
        self.coin_rep = list(self.coin_df.iloc[:, 1].values)
        self.gecko_rep = list(self.gecko_df.iloc[:, 1].values)
        #print(self.coin_rep)



    def remove_rows(self):
        '''
        Compile rows need to delete (based on self.mark).
        '''

        self.get_repetition()

        for item in self.coin_rep:
            if not item in self.gecko_rep:
                # coin_df need to delete row with 'item'
                self.delete_rows.append(('coin', item))
        for item in self.gecko_rep:
            if not item in self.coin_rep:
                self.delete_rows.append(('gecko', item))
        #print(self.delete_rows)



    def clean_rows(self):
        '''
        Delete rows that appears only in one df.
        We need to make sure both dfs have same rows and comparable data.
        Example:
        df_a = [
            [round, name, price],
            [1, aaa, 100],
            [2, bbb, 200],
            [5, eee, 500],
            ]
        df_b = [
            [round, name, price], 
            [1, aaa, 100],
            [2, bbb, 200],
            [3, ccc, 300],
            ]

        df_a has round = 5 but don't have round = 3
        df_b has round = 3 but don't have round = 5

        Hence, we don't need round = 3 and round = 5 in both df.
        We only need round = 1 and 2.

        This function will delete round 3 and 5 for you.


        example:
        coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
        gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
        
        coin_bitcoin = coin_df[coin_df['name'] == 'bitcoin']
        gecko_bitcoin = gecko_df[gecko_df['name'] == 'bitcoin']

        coin_clean, gecko_clean = DataClean(coin_bitcoin, gecko_bitcoin).clean_rows()
        '''

        self.remove_rows()
        # self.delete_rows = [('gecko', 149), ('gecko', 190)]
        # it will delete row with repetition = 149 in self.gecko_df
        for row in self.delete_rows:
            #print(row[0])
            if row[0] == 'gecko':
                # get row indexing with repetition == 149
                row_index = self.gecko_df[self.gecko_df['repetition'] == row[1]].index.values[0]
                self.gecko_df = self.gecko_df.drop(self.gecko_df.index[row_index])
                # reset index after delete any row
                self.gecko_df = self.gecko_df.sort_values('repetition').reset_index(drop = True)
                #print('\n\n')
                #print(self.gecko_df[self.gecko_df['repetition'] == row[1]])
                #print('len: gecko_df : ', len(self.gecko_df))
            if row[0] == 'coin':
                row_index = self.coin_df[self.coin_df['repetition'] == row[1]].index.values[0]
                self.coin_df = self.coin_df.drop(self.coin_df.index[row_index])
                # reset index after delete any row
                self.coin_df = self.coin_df.sort_values('repetition').reset_index(drop = True)
                #print('\n\n')
                #print(self.coin_df[self.coin_df['repetition'] == row[1]])
                #print('len: coin_df :', len(coin_df))

        #print(len(self.coin_df))
        #print(len(self.gecko_df))
        return self.coin_df, self.gecko_df




class ComparableData():
    '''
    This class return a list of abbr which cointains the abbr of all comparable currencies.
    A comparable currency should appears in 1) all repetitions and 2) dataset from both
    websites.

    An example:

    data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
    
    Remember, data_comparable is a list of abbr.
    '''

    def __init__(self, df_base, df_compare, compare_column):
        self.df_base = df_base
        self.df_compare = df_compare
        # compare_column is a number, in this case, comp_col = abbr of each currency
        self.col = compare_column
        self.data = []
        self.data_backup = None



    def grouping(self):

        # col 1 = repetition
        # need to find the max value of repetition
        rep_list = self.df_base.iloc[:, 1].values
        max_rep = max(rep_list)
        min_rep = min(rep_list)


        # get abbr from df with repetition == 2
        # len = 500
        base_list = list(self.df_base[self.df_base['repetition'] == 2].iloc[:, self.col].values) 
        comp_list = list(self.df_base[self.df_base['repetition'] == 3].iloc[:, self.col].values) 
        self.matching(base_list, comp_list)

        for rep in range(min_rep, max_rep + 1):
            # find dataframe with repetition == rep
            comp_list = self.next_repetition(self.df_base, rep)
            # backup self.data to self.data_backup, use it in method 'self.matching'
            self.data_backup = self.data
            # clear all content in self.data
            self.data = []
            self.matching(self.data_backup, comp_list)

        coin_data = self.data


        self.data = []
        base_list = list(self.df_compare[self.df_compare['repetition'] == 2].iloc[:, self.col].values) 
        comp_list = list(self.df_compare[self.df_compare['repetition'] == 3].iloc[:, self.col].values) 
        self.matching(base_list, comp_list)

        for rep in range(min_rep, max_rep + 1):
            # find dataframe with repetition == rep
            comp_list = self.next_repetition(self.df_compare, rep)
            # backup self.data to self.data_backup, use it in method 'self.matching'
            self.data_backup = self.data
            # clear all content in self.data
            self.data = []
            self.matching(self.data_backup, comp_list)

        gecko_data = self.data


        self.data = []
        self.matching(coin_data, gecko_data)
        coin_comparable = self.data


        # len(coin_data) = 81, based on current data from coinmktcap,
        # 81 currencies appear in each repetition.
        # len(gecko_data) = 449, based on current data from gecko,
        # 449 currencies appear in each repetition

        return self.data



    def matching(self, base_list, comp_list):
        '''
        Compile currencies appear in both list,
        save matching currencies to self.data
        '''
        for item in comp_list:
            # must include condition: not in self.data to avoid same abbr in self.data
            if item in base_list and item not in self.data:
                self.data.append(item)



    def next_repetition(self, df, rep):
        '''
        Return new dataframe with repetition == rep in df
        i.e., a = self.next_repetition(self.df_base, 1)

        Use for loop get rep == i, i = 1, 2, 3,... 192, from coin and gecko df.
        '''
        
        return list(df[df['repetition'] == rep].iloc[:, self.col].values) 
        


class Statistics():

    def __init__(self, data_list):
        self.data = data_list
        self.stat_list = []



    def trend_statistics(self):
        mean = round(np.mean(self.data), 4)
        std = round(np.std(self.data), 4)
        max_val = round(np.max(self.data), 4)
        min_val = round(np.min(self.data), 4)
        data_range = round(max_val - min_val, 4)

        self.stat_list = [mean, std, data_range]


        return self.stat_list



class GraphDiff():
    def __init__(self, coin_df, gecko_df, trend_pic_name, HTH_pic_name, item):
        self.coin = coin_df
        self.gecko = gecko_df
        self.trend_name = trend_pic_name
        self.HTH_name = HTH_pic_name
        self.item = item
        self.col = None
        self.which_item()



    def which_item(self):
        if self.item == 'price':
            self.col = 6
        elif self.item == 'vol':
            self.col = 7
        elif self.item == 'mktcap':
            self.col = 8

        self.graph_coinVSgecko()



    def graph_coinVSgecko(self):
        '''
        Generate two graph for a currency:
        1. plot trend
        '''
        # clean data for coin and gecko, dataframe()
        coin_clean, gecko_clean = DataClean(self.coin, self.gecko).clean_rows()
        x_axis = [i for i in range(len(coin_clean))]
    
        coin_price = coin_clean.iloc[:,self.col].values
        gecko_price = gecko_clean.iloc[:,self.col].values
    
        if not os.path.exists('figures'):
            os.mkdir('figures')

        plt.plot(x_axis, coin_price, c = 'red')
        plt.plot(x_axis, gecko_price, c = 'blue')
        plt.xlabel('repetition/time_period(nth 15 mins)')
        plt.ylabel(self.item)
        plt.title(self.trend_name)
        plt.savefig(os.path.join('figures', self.trend_name + '.png'))
        # Initialize matplotlib after plotting.
        # Avoid overlapping
        plt.clf()
        
        
        ### scatter plot: bitcoin data (coinmktcap vs gecko)
        ### If data are same, it suppose to be a straight line.
        plt.scatter(coin_price, gecko_price)
        plt.xlabel('coinmktcap_' + self.item)
        plt.ylabel('coingecko_' + self.item)
        plt.title(self.HTH_name)
        plt.savefig(os.path.join('figures', self.HTH_name + '.png'))
        plt.clf()



class Compare_192():

    def __init__(self, coin_df, gecko_df, data_comparable, item):
        self.coin = coin_df
        self.gecko = gecko_df
        self.comp = data_comparable
        self.df_coin = pd.DataFrame()
        self.df_gecko = pd.DataFrame()
        self.item = item
        self.col = None
        self.check_item()


    def check_item(self):
        if self.item == 'price':
            self.col = 6
        if self.item == 'vol':
            self.col = 7
        if self.item == 'mktcap':
            self.col = 8


    def get_statistics(self):

        ### statistics in coinmktcap's data
        ## item = one currency, item_df = this currency's trend data
        for item in self.comp:
            coin_item_df = self.coin[self.coin['abbr'] == item]
            gecko_item_df = self.gecko[self.gecko['abbr'] == item]
            # only need currencies with 192 repetitions

            if coin_item_df.shape[0] == 192:
                # can be price, vol, mktcap, depends on 'item'
                item_info = coin_item_df.iloc[:, self.col].values
                ## [mean, std, data_range]
                item_statistics = Statistics(item_info).trend_statistics()

                self.df_coin = self.df_coin.append({
                    'coin_name':item,
                    'coin_mean':item_statistics[0],
                    'coin_std':item_statistics[1],
                    'coin_range':item_statistics[2],
                    }, ignore_index = True)

                item_info = gecko_item_df.iloc[:, self.col].values
                item_statistics = Statistics(item_info).trend_statistics()

                self.df_gecko = self.df_gecko.append({
                    'gecko_name':item,
                    'gecko_mean':item_statistics[0],
                    'gecko_std':item_statistics[1],
                    'gecko_range':item_statistics[2],
                    }, ignore_index = True)

        df = pd.concat([self.df_coin, self.df_gecko], axis = 1)
        df = df.drop(columns = 'gecko_name')
        df['mean_diff'] = (df['gecko_mean'] - df['coin_mean'])/df['coin_mean']
        df['std_diff'] = (df['gecko_std'] - df['coin_std'])/df['coin_std']
        df['range_diff'] = (df['gecko_range'] - df['coin_range'])/df['coin_range']





        order = ['coin_name', 'coin_mean', 'gecko_mean', 'mean_diff', 'coin_std', 'gecko_std', 'std_diff', 'coin_range', 'gecko_range', 'range_diff']
        df = df[order]
        #print(df)

        return df





if __name__ == '__main__':

    coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
    gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
    
    data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
    comp_statistics = Compare_192(coin_df, gecko_df, data_comparable, 'price').get_statistics()
    print(comp_statistics)




    #print('len data_comparable: ', len(data_comparable))
    #print(data_comparable)

