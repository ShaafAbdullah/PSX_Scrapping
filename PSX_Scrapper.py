"""
Created on Sun Jul 12 17:51:32 2020
@author: SHAAFABDULLAH
"""
from bs4 import BeautifulSoup as soup
import requests
news_time=datetime.datetime.now()
fileName = "psx_scraping.csv"
f = open(fileName,"w")
headers = "SCRIP, LDCP, OPEN, HIGH, LOW, CURRENT, CHANGE, VOLUME, ""\n"
f.write(headers)
url_to_scrape = "https://www.psx.com.pk/market-summary/"

try:
    client_page = requests.get(url_to_scrape)
except:
    print("Request aborted due to unknown reason!")

page_html = client_page.text
client_page.close()
#parse html recieved
page_soup = soup(page_html,"html.parser")
#retrieving tables from parsed html
tables = page_soup.find_all("table")

for table in tables[1:(len(tables)-1)]:
        rows=table.find_all("tr")[1:]
        for row in rows[1:]:

            columns = row.find_all("td")[:]
            for column in columns:
                data = column.text
                data = data.replace(","," ")
                data = data.replace("\n"," ")
                f.write(data+", ")
            f.write("\n")
f.close()
