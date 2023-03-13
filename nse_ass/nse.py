import requests
from bs4 import BeautifulSoup

url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-9999&symbol=BANKNIFTY&symbol=BANKNIFTY&instrument=OPTIDX&date=-&segmentLink=17&segmentLink=17p"

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
option_chain_table = soup.find(id="octable")

# Extract the headers from the table
headers = []
for th in option_chain_table.find_all('th'):
    headers.append(th.text.strip())
    
# Extract the data rows from the table
data = []
for tr in option_chain_table.find_all('tr'):
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    if row:
        data.append(row)