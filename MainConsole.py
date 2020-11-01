import os, glob
from scrapping_module import Scrapping, DeepLink, merge_rating_links
from parsing_module import Parsing
from scrapping_module import name_extraction as etr
from scrapping_module import pair_deeplink, check_folder
from deeplink_parsing import ParsingDeepLink




#==============================================================================
# Step 1. Download 48hr data
#==============================================================================

#url_coin_base = 'https://coinmarketcap.com/' 
#url_gecko_base = 'https://www.coingecko.com/en?page=' 
#url_list = [(url_coin_base + str(i), url_gecko_base + str(i)) for i in range(1,6)]
#folder_name = ['coinmktcap_html_file', 'gecko_html_file']
#Scrapping(url_list, folder_name, 48).folder_setup()


#==============================================================================
# Step 2. Parsing data and deeplink
#==============================================================================

#folder = 'coinmktcap_html_file'
#Parsing(folder).parsing_coin_html()
#folder = 'gecko_html_file'
#Parsing(folder).parsing_gecko_html()
#
#deeplink_list = pair_deeplink()






#print('=' * 100 + '\nFinish pairing' + ' [ ' + str(len(deeplink_list)) + ' ] ' + 'URLs...\n' + '=' * 100)
#
#file_names = etr(deeplink_list)




#==============================================================================
# Step 3. Scrapping 500 coins deeplink info
#==============================================================================

### Then you can call scrapping module
### 0.25 for 15 mins. Recall, for loop repeat every 15 mins, and unit of 0.25 is hour. repetition = 0.25*4 = 1 round
### hence, we only need to download these deeplink for once, we need 0.25*4 = 1

#deeplink_folder = ['coin_500deeplink', 'gecko_500deeplink']
#DeepLink(deeplink_list, deeplink_folder,file_names).folder_setup()




#==============================================================================
# Step 4. Parsing deeplinks (!!!! Need to add another parsing structure in coinmktcap deeplink)
#==============================================================================
folder = 'coin_500deeplink'
ParsingDeepLink(folder).parsing_coin_deeplink()
folder = 'gecko_500deeplink'
ParsingDeepLink(folder).parsing_gecko_deeplink()













#==============================================================================
# Step 10. Recovering missing data
#==============================================================================
# re-download data from Error_Log.csv

#check_folder()
#
#folder = 'coin_500deeplink'
#ParsingDeepLink(folder).parsing_coin_deeplink()
#folder = 'gecko_500deeplink'
#ParsingDeepLink(folder).parsing_gecko_deeplink()





