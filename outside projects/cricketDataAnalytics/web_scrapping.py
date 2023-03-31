import bs4
import requests
from bs4 import BeautifulSoup
import pandas  as pd


base_url ='https://www.espncricinfo.com/ci/engine/records/team/match_results.html?class=3;id=2023;type=year'

response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

header_row = rows[0]
header_cells = header_row.find_all('th')

headers = [cell.text.strip() for cell in header_cells]

data = []
for row in rows[1:]:
    cells = row.find_all(['td','th'])
    data.append([cell.text.strip() for cell in cells])


df = pd.DataFrame(data, columns=headers)
df.to_csv('match results.csv')
print(df)

