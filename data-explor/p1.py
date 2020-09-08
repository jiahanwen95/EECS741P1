import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def convert_currency(value):
    new_value = value.replace('M', '').replace('k','')
    return np.float(new_value)
def convert_currency2(value):
    new_value = value.replace('$', '')
    return new_value
def convert_currency3(value):
    return np.float(value)/(1024*1024)

apple=pd.read_csv("data/external/AppleStore.csv",index_col=0)
google=pd.read_csv("data/external/googleplaystore.csv")

#remove useless data from both data_set, only pick game
apple_game=apple.loc[apple['prime_genre']== 'Games']
google_game=google.loc[google['Category']=='GAME']

google_game=google_game[~google_game['Size'].isin(['Varies with device'])]

google_game=google_game.drop(['Reviews','Installs','Type','Content Rating','Last Updated','Current Ver','Android Ver','Genres'],axis=1)
apple_game=apple_game.drop(['id','ver','currency','rating_count_tot','rating_count_ver','user_rating_ver','cont_rating','sup_devices.num','ipadSc_urls.num','lang.num','vpp_lic'],axis=1)

apple_game.columns=['App','Size','Price','Rating','Category']
apple_game=apple_game[['App','Category','Rating','Size','Price']]

google_game['Price']=google_game['Price'].apply(convert_currency2)
google_game['Size']=google_game['Size'].apply(convert_currency)
apple_game['Size']=apple_game['Size'].apply(convert_currency3)
frames = [apple_game, google_game]
ds = pd.concat(frames)
ds.dropna(axis=0, how='any', inplace=True)
ds = ds.drop_duplicates()

ds['Price']=ds['Price'].astype(float)


ds.plot(x='Rating',y='Price',kind='scatter')

ds.plot(x='Rating',y='Size',kind='scatter')




