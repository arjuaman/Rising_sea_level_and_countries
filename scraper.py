from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_elevation"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table')[1]
rows = table.find_all('tr')
row_list = list()

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)

df_bs = pd.DataFrame(row_list,columns=['Country','Elevation'])
df_bs.set_index('Country',inplace=True)
df_bs.to_csv('beautifulsoup.csv')
