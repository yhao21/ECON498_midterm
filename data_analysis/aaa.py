import pandas as pd


df = pd.read_csv('CoinMKT_48hrs_data.csv')

df = df[df['abbr'] == 'XRP'].values
print(len(df))
