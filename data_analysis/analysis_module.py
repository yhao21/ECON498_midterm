import pandas as pd





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

        print(len(self.coin_df))
        print(len(self.gecko_df))
        return self.coin_df, self.gecko_df


class ComparableData():
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
        
        return df[df['repetition'] == rep].iloc[:, self.col].values
        



    



if __name__ == '__main__':

    coin_df = pd.read_csv('CoinMKT_48hrs_data.csv')
    gecko_df = pd.read_csv('Gecko_48hrs_data.csv')
    
    # coin_rep2 = coin_df with repetition == 2
    # shape = (500, 10)
    #coin_rep2 = coin_df[coin_df['repetition'] == 2]
    #print(coin_rep2.iloc[:, 4].values)

    data_comparable = ComparableData(coin_df, gecko_df, 4).grouping()
    print('len data_comparable: ', len(data_comparable))
    print(data_comparable)

