import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

##baseurl
url = 'https://www.churchofjesuschrist.org/temples/list?lang=eng'
r = requests.get(url)
soup = BeautifulSoup(r.content)
json_data  = soup.find(id = '__NEXT_DATA__').string
temple_dict = json.loads(json_data)
temple_list = temple_dict['props']['pageProps']['templeList']
temple_df = pd.DataFrame(temple_list)

temple_df.to_csv('data/temples_raw.csv')