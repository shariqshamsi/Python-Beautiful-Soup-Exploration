import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')


table = soup.find_all('table')[1]

world_title = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_title]

#print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
    
#print(df)

df.to_csv('companies.csv', index = False)
